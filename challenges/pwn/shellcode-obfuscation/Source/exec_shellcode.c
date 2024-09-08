#include <unistd.h>
#include <sys/mman.h>
#include <linux/seccomp.h>
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

    if(prctl(PR_SET_SECCOMP, SECCOMP_MODE_STRICT)) {
        dprintf(2, "WARN: failed to enable seccomp\n");
    }

    asm(
            "call %0"
            :: "ar" (payload)
            );
}