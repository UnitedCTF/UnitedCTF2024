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
    char buf[53] = "\x68\x73\x6d\x65\x0b\x81\x34\x24\x01\x01\x01\x01\x48\xb8\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x50\xbf\x01\x00\x00\x00\x6a\x0b\x5a\x48\x89\xe6\xb8\x01\x00\x00\x00\x48\x31\xc9\xb5\x04\xfe\xc5\xb1\x0e\xfe\xc1\x51\xff\xe4";
    char* bytes = malloc(sizeof(buf));
    memcpy(bytes, buf, sizeof(buf));
    mprotect((void*)((intptr_t)bytes & ~0xFFF), sizeof(buf), PROT_READ|PROT_EXEC|PROT_WRITE);
    int (*exeshell)();
    exeshell = (int (*)()) bytes;
    prctl(PR_SET_SECCOMP, SECCOMP_MODE_STRICT);
    (int)(*exeshell)();
}