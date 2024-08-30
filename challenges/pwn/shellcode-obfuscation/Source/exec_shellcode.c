#include <unistd.h>
#include <sys/mman.h>
#include <linux/seccomp.h>
#include <string.h>
#include <malloc.h>
#include <linux/prctl.h>
#include <sys/prctl.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    char buf[3];
    scanf("%s", buf);
    int length = strtol(buf, NULL, 10);
    char *bytes = malloc(sizeof(char) * length);
    read(0, bytes, length);
    mprotect((void *)((intptr_t)bytes & ~0xFFF), sizeof(char) * length, PROT_READ | PROT_EXEC);
    int (*exeshell)();
    exeshell = (int (*)())bytes;
    prctl(PR_SET_SECCOMP, SECCOMP_MODE_STRICT);
    (int)(*exeshell)();
}