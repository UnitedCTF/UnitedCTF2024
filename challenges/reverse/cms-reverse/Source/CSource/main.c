#define __STDC_WANT_LIB_EXT1__ 1
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <malloc.h>
#include <stdlib.h>

const char* ADMIN_USERNAME = "flag-U5e3nv1r0n3mentV4ria8l3sF0rS3cre7s";

const char *getPassword();

void read(char buf[64]);

int main() {
    bool valid = false;
/*    while (!valid) {
        char username_buf[64];
        printf("%s","Please enter the username: ");
        scanf_s("%s", username_buf);
        valid = strcmp(username_buf, ADMIN_USERNAME) == 0;
        if (valid) {
            printf("Welcome, %s!\n", ADMIN_USERNAME);
        } else {
            printf("This user does not exist!\n");
        }
    }*/
    valid = false;
    while (!valid) {
        char pwd_buf[64];
        printf("%s","Please enter the password: ");
        read(pwd_buf);
        valid = strcmp(pwd_buf, getPassword()) == 0;
        if (valid) {
            printf("Welcome, %s!\n", ADMIN_USERNAME);
        } else {
            printf("This user does not exist!\n");
        }
    }
    return 0;
}

const char *getPassword() {

    char* s = "\x7e\x02\x6c\x04\x01\x25\x04\x71\x2f\x00\x32\x0d\x77\x2d\x57\x77\x7d\x07\x66\x55\x76\x7c\x06\x74\x7d\x56\x6c\x06\x73\x2e\x04\x76\x2b\x03\x31\x0d\x77\x29\x04\x75\x7e\x08\x64\x02\x74\x7f\x05\x25\x7c\x08\x64\x00\x7f\x79\x03\x76\x2f\x07\x6d\x06\x7f\x78\x57\x74\x76\x07\x63\x51\x7e\x78\x0d\x72\x2f\x09\x6c";
    const char* k1 = "\x4e\x30\x54\x34\x46\x4c\x34\x47";
    for (int i = 0; i < 75; i++) {
        s[i] ^= k1[i % strnlen_s(k1, 8)];
    }
    int length = strlen(s);
    char** password = malloc(length * sizeof(char*));
    int y = 0;
    char *hex = malloc(3 * sizeof(char));
    for(int i = 0; i < length; i++) {
        hex[y] = s[i];
        y++;
        if(y == 3){
            y = 0;
            password[i/3] = hex;
            hex = malloc(3 * sizeof(char));
        }
    }
    char* p = malloc((length/3) * sizeof(char));
    for(int i = 0; i < length/3; i++) {
        int sx = strtol(password[i], NULL, 16) / (i < 1 ? 1 : i);
        printf("%d ", sx);
        p[i] = sx ^ k1[i % strnlen_s(k1, 8)];
    }



    printf("\n");
    printf("Password: %s\n", p);
    for(int i = 0; i < length; i++) {
        free(password[i]);
    }
    free(password);
    return s;
}

void read(char buf[]) {
#ifdef __STDC_LIB_EXT1__ // only use swscanf_s if __STDC_LIB_EXT1__ is already defined
    scanf_s ("%s",buf );
#endif
    scanf("%s", buf);
}