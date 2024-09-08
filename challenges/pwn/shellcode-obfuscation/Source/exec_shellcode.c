#include <unistd.h>
#include <sys/mman.h>
#include <linux/filter.h>
#include <linux/seccomp.h>
#include <sys/syscall.h>
#include <string.h>
#include <malloc.h>
#include <linux/prctl.h>
#include <sys/prctl.h>
#include <stdlib.h>
#include <errno.h>

int main(int argc, char **argv)
{
    if(argc < 2) return 1;

    int arg1Length = strlen(argv[1]) - 1;
    if(arg1Length > 720 * 4) return 1;

    int inputLength = arg1Length < 720 * 4 ? arg1Length : 720 * 4;
    unsigned char* payload = malloc(inputLength / 4);
    for(int i = 0; i < inputLength; i += 4) {
        char *ptr;
        payload[i/4] = (unsigned char) strtoul(argv[1] + i + 2, &ptr, 16);
    }

    long page_size = sysconf(_SC_PAGESIZE);
    void *page_start = (void *) ((long) payload & -page_size);
    mprotect(page_start, page_size * 2, PROT_READ | PROT_WRITE | PROT_EXEC);

    struct sock_filter filter[] = {
        BPF_STMT(BPF_LD | BPF_W | BPF_ABS, (offsetof(struct seccomp_data, nr))),
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_write, 0, 2),
        BPF_STMT(BPF_LD | BPF_W | BPF_ABS, (offsetof(struct seccomp_data, args))),
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, 1, 2, 1),
        BPF_JUMP(BPF_JMP | BPF_JEQ | BPF_K, __NR_exit, 1, 0),
        BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_KILL),
        BPF_STMT(BPF_RET | BPF_K, SECCOMP_RET_ALLOW)
    };

    struct sock_fprog prog = {
        .len = (unsigned short)(sizeof(filter) / sizeof(filter[0])),
        .filter = filter
    };

    if(prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)) {
        perror("set_no_new_privs failed");
        return errno;
    }

    if(prctl(PR_SET_SECCOMP, SECCOMP_MODE_FILTER, &prog)) {
        perror("set_seccomp failed");
        return errno;
    }

    asm(
            "call %0"
            :: "ar" (payload)
            );
}