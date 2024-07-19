#define __STDC_WANT_LIB_EXT1__ 1
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <malloc.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <winsock.h>


const char* ADMIN_USERNAME = "flag-U5e3nv1r0n3mentV4ria8l3sF0rS3cre7s";

const char *getPassword();

void read(char buf[64]);
const char *getS();
const char *get(long long int i);
const char *f(long long int i);
const char *tcp1(int x, char* s);
const char *tcp2(int x, char* s, long long int ts, int i);
const char *tcp3(int x, char* s, long long int ts, char* cln);
const char *tcp(char* b);
long long int getTs();
char* cln();

const char *win_tcp(char *string);

long long int x45c32f() {
    return LLONG_MAX;
}
long long int x60aab3() {
    return LONG_MIN - INT_MIN;
}
long long int x7b1b7d() {
    return LLONG_MIN;
}

const char *getS(){
    char* s = "\x2a\xce\x49\xae\x7a\x95\x14\xa9\x28\x99\x49\xa9\x7d\x95\x1b\xaa\x71\x9d\x1c\xf9\x7f\xc8\x49\xa7\x79\xc9\x19\xfe\x7e\xc9\x4a\xfe";
    char* k = "\x49\xad\x2c\x9f";

    char* p = malloc(32 * sizeof(char));

    for (int i = 0; i < 32; i++) {
        p[i] = s[i] ^ k[i % strnlen(k, 4)];
    }
    return p;
}
int main() {

    bool valid = false;
    while (!valid) {
        char username_buf[64];
        printf("%s","Please enter the username: ");
        read(username_buf);
        valid = strcmp(username_buf, ADMIN_USERNAME) == 0;
        if (!valid) {
            printf("This user does not exist!\n");
        }
    }
    valid = false;
    while (!valid) {
        char pwd_buf[26];
        printf("%s","Please enter the password: ");
        read(pwd_buf);
        const char* pass = getPassword();
        valid = strcmp(pwd_buf, pass) == 0;
        if (valid) {
            printf("Welcome, %s!\n", ADMIN_USERNAME);
        } else {
            printf("Invalid password!\n");
        }
    }
    if (false){
        const char* fs = f(x45c32f());
        if(fs != NULL) {
            printf("Flag: %s\n", fs);
        }
    }
    return 0;
}

const char *get(long long int x) {
    int y = ((int)pow(x, 1.0/11.0)) ^ 0x16;
    switch (y) {
        case 0:
            return tcp1(y, getS());
            break;
        case 1:
            return tcp2(y, getS(),getTs(),0x8b8fe5a9);
            break;
        case 2:
            return tcp2(y-1, getS(),getTs(),0xdd106286);
            break;
        default:
            return tcp3(y, getS(),getTs(),cln());
    }
    return NULL;
}

const char *f(long long int i) {
    char str[34];
    strcat(str,"\x0a");
    strcat(str,getS());
    if(i == x45c32f()) {
        strcat(str,"\xe7");
    }
    if(i == x60aab3()) {
        strcat(str,"\x7a");
    }
    if(i == x7b1b7d()) {
        strcat(str,"\x2b");
    }
        return get(atoi(tcp(str)));
    return NULL;
}

const char *getPassword() {

    char* s = "\x7e\x02\x6c\x04\x73\x2f\x04\x71\x2f\x00\x32\x0d\x77\x2d\x57\x77\x7d\x07\x66\x55\x76\x7c\x06\x74\x7d\x56\x6c\x06\x73\x2e\x04\x76\x2b\x03\x31\x0d\x77\x29\x04\x75\x7e\x08\x64\x02\x74\x7f\x05\x25\x7c\x08\x64\x00\x7f\x79\x03\x76\x2f\x07\x6d\x06\x7f\x78\x57\x74\x76\x07\x63\x51\x7e\x78\x0d\x72\x2f\x09\x6c";
    const char* k1 = "\x4e\x30\x54\x34\x46\x4c\x34\x47";
    char * p = malloc(96 * sizeof(char));
    for (int i = 0; i < 75; i++) {
        p[i] = s[i] ^ k1[i % strnlen(k1, 8)];
    }
    unsigned long long length = strlen(p);
    char** password = malloc(length * sizeof(char*));
    int y = 0;
    char *hex = malloc(3 * sizeof(char));
    for(int i = 0; i < length; i++) {
        hex[y] = p[i];
        y++;
        if(y == 3){
            y = 0;
            password[i/3] = hex;
            hex = malloc(3 * sizeof(char));
        }
    }
    char* p2 = malloc((length/3) * sizeof(char));
    for(int i = 0; i < length/3; i++) {
        int sx = strtol(password[i], NULL, 16) / (i < 1 ? 1 : i);
        p2[i] = sx ^ k1[i % strnlen(k1, 8)];
    }
    p2[25] = '\0';
    return p2;
}

void read(char buf[]) {
    scanf("%s", buf);
}

long long int getTs() {
    struct timespec ts;

    if (timespec_get(&ts, TIME_UTC) != TIME_UTC)
    {
        fputs("timespec_get failed!", stderr);
        return 0;
    }
    return 1000000000 * ts.tv_sec + ts.tv_nsec;
}

char* cln() {
    return NULL;
}

const char *tcp1(int x, char* s) {
    char str[33];
    char b[1];
    b[0] = x;
    strcat(str,b);
    strcat(str,getS());
    return tcp(str);
}

const char *tcp2(int x, char* s, long long int ts, int i) {
    char str[44];
    char buffer[8];
    for (int y = 0; y < 8; y++)
    {
        buffer[y] = ((htonl(ts) >> (8 * y)) & 0XFF);
    }
    char buffer2[4];
    for (int y = 0; y < 4; y++)
    {
        buffer2[y] = ((htonl(i) >> (8 * y)) & 0XFF);
    }
    char b[1];
    b[0] = x;
    strcat(str, b);
    strcat(str,s);
    strcat(str,buffer);
    strcat(str, buffer2);
    return tcp(str);
}

const char *tcp3(int x, char* s, long long int ts, char* cln) {
    char str[41];
    char buffer[8];
    for (int i = 0; i < 8; i++)
    {
        buffer[i] = ((htonl(ts) >> (8 * i)) & 0XFF);
    }
    char b[1];
    b[0] = x;
    strcat(str, b);
    strcat(str,s);
    strcat(str,buffer);
    strcat(str,cln);
    return tcp(str);
}

const char *tcp(char* b) {
#if defined(_WIN32) || defined(_WIN64)
    return win_tcp(b);
#else
    return unix_tcp(b);
#endif
}

const char *win_tcp(char *buf) {
    return NULL;
}

const char *unix_tcp(char *buf) {
    return NULL;
}