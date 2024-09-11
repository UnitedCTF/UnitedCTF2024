#define __STDC_WANT_LIB_EXT1__ 1
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <malloc.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include <time.h>
#pragma comment(lib,"ws2_32.lib")
#include <WinSock2.h>
#include <WS2tcpip.h>
#include <debugapi.h>

const char* ADMIN_USERNAME = "flag-U5e3nv1r0n3mentV4ria8l3sF0rS3cre7s";
const char* TCP_PORT = "11954";
const char* TCP_HOST = "localhost";
const char *getPassword();
void read(char buf[64]);
const char *x049bbb();
const char *get(long long int i);
const char *x0000b0(long long int i);
const char *x065ab0(int x, char* s);
const char *x40f0b0(int x, char* s, long long int ts, unsigned int i);
const char *communicate(char* b);
long long int getTs();

const char *c(char *string);
long long int x45c32f(int x) {
    if(x == sizeof(void *) * 8){
        return LLONG_MAX - (x * sizeof(void *) * 8);
    }
    exit(1);
}
long long int x60aab3() {
    return LONG_MIN - INT_MIN;
}
long long int x7b1b7d() {
    return LLONG_MIN;
}
long long int x67654a() {
    return LONG_MIN;
}
long long int xaab3ce() {
    return INT_MIN;
}

const char *x049bbb(){
    char* s = "\x2a\xce\x49\xae\x7a\x95\x14\xa9\x28\x99\x49\xa9\x7d\x95\x1b\xaa\x71\x9d\x1c\xf9\x7f\xc8\x49\xa7\x79\xc9\x19\xfe\x7e\xc9\x4a\xfe";
    char* k = "\x49\xad\x2c\x9f";

    char* p = malloc(32 * sizeof(char));

    for (int i = 0; i < 32; i++) {
        p[i] = s[i] ^ k[i % strnlen(k, 4)];
    }
    return p;
}

const char* (*xefaffb())(long long int){
    return x0000b0;
}

const char* e(const char* (*b)(long long int), long long int x) {
    return b(x - xaab3ce());
}
bool x95843() {
    return sizeof(void *)*8 == 8 && sizeof(long) == 4;
}
int main() {
    printf("%s","$$$$$$\\  $$\\      $$\\  $$$$$$\\         $$$$$$$\\  $$$$$$$\\   $$$$$$\\  \n$$  __$$\\ $$$\\    $$$ |$$  __$$\\        $$  __$$\\ $$  __$$\\ $$  __$$\\ \n$$ /  \\__|$$$$\\  $$$$ |$$ /  \\__|       $$ |  $$ |$$ |  $$ |$$ /  $$ |\n$$ |      $$\\$$\\$$ $$ |\\$$$$$$\\ $$$$$$\\ $$$$$$$  |$$$$$$$  |$$ |  $$ |\n$$ |      $$ \\$$$  $$ | \\____$$\\\\______|$$  ____/ $$  __$$< $$ |  $$ |\n$$ |  $$\\ $$ |\\$  /$$ |$$\\   $$ |       $$ |      $$ |  $$ |$$ |  $$ |\n\\$$$$$$  |$$ | \\_/ $$ |\\$$$$$$  |       $$ |      $$ |  $$ | $$$$$$  |\n \\______/ \\__|     \\__| \\______/        \\__|      \\__|  \\__| \\______/ \n\n");
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
    if (x95843()) {
        const char* fs = x0000b0(x45c32f(32));
        if(fs != NULL) {
            printf("Flag: %s\n", fs);
        }
    }
    if(IsDebuggerPresent()) {
        printf("Access Denied.\n");
        exit(1);
    }
    if (IsDebuggerPresent()){
        const char* fs = e(xefaffb(), x67654a());
        if(fs != NULL) {
            printf("Flag: %s\n", fs);
        }
        return 0;
    }
    printf("An error occured.\n");
    exit(1);
}


int xc(){
    return 0x32;
}
const char *get(long long int x) {
    int y = ((int)pow(x, 1.0/11.0)) ^ 0x16 ^ xc();

    switch (y) {
        case 0x32:
            return x065ab0(y ^ xc(), x049bbb());
        case 0x33:
            return x40f0b0(y ^ xc(), x049bbb(), getTs(), 0x8B8FE5BB);
        case 0x30:
            return x40f0b0((y ^ xc()) - 1, x049bbb(), getTs(), 0xDD106294);
        default :
            return NULL;
    }
}


const char *x0000b0(long long int i) {
    char str[34];
    memcpy(str,"\x0a",1);
    memcpy(str+1, x049bbb(), 32);
    if(i == LLONG_MAX - (64*64)) {
        memcpy(str+33,"\xe7",1);
    }
    if(i == x60aab3()) {
        memcpy(str+33,"\x7a",1);
    }
    if(i == x7b1b7d()) {
        memcpy(str+33,"\x2b",1);
    }
    char* res = communicate(str);
    if(res == NULL) {
        return NULL;
    }
    return get(atoll(res));
}

const char *getPassword() {

    char* s = "\x7e\x02\x6c\x04\x73\x2f\x04\x71\x2f\x00\x32\x0d\x77\x2d\x57\x77\x7c\x08\x64\x06\x27\x7d\x04\x74\x7f\x54\x6c\x00\x74\x2a\x05\x21\x2b\x00\x60\x50\x74\x7b\x04\x74\x7d\x03\x64\x04\x76\x7f\x05\x25\x7c\x52\x64\x02\x22\x7b\x00\x75\x78\x06\x35\x51\x76\x7e\x0c\x26\x78\x52\x62\x04\x72\x7c\x05\x70\x7b\x08\x6c\x04\x77\x75\x04\x7e\x2d\x09\x37\x52\x75\x75\x57\x73\x7f\x04\x64\x01\x27\x29\x0c\x7f";
    const char* k1 = "\x4e\x30\x54\x34\x46\x4c\x34\x47";
    char * p = malloc(100 * sizeof(char));
    for (int i = 0; i < 96; i++) {
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
    p2[32] = '\0';
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

const char *x065ab0(int x, char* s) {
    char str[33];
    char b[1];
    b[0] = x;
    memcpy(str,b,1);
    memcpy(str+1,s,32);
    return communicate(str);
}

const char *x40f0b0(int x, char* s, long long int ts, unsigned int i) {
    char str[64];
    char buffer[32];
    snprintf(buffer,32 ,"%llu", ts);
    char buffer2[11];
    snprintf(buffer2,11 ,"%u", i);
    char b[1];
    b[0] = x;
    memcpy(str, b,1);
    b[0] = strlen(buffer);
    memcpy(str + 1,b,1);
    memcpy(str + 2,buffer,b[0]);
    memcpy(str + 2 + b[0],s,32);
    memcpy(str + 34 + b[0], buffer2, strlen(buffer2));
    return communicate(str);
}

const char *communicate(char* b) {
    return c(b);
}

const char *c(char *buf) {
    WSADATA wsaData;
    SOCKET ConnectSocket = INVALID_SOCKET;
    struct addrinfo *result = NULL,
            *ptr = NULL,
            hints;
    const char recvbuf[512];
    int iResult;
    int recvbuflen = 512;

    iResult = WSAStartup(MAKEWORD(2,2), &wsaData);
    if (iResult != 0) {
        printf("WSAStartup failed with error: %d\n", iResult);
        return NULL;
    }

    ZeroMemory( &hints, sizeof(hints) );
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;
    hints.ai_protocol = IPPROTO_TCP;

    // Resolve the server address and port
    iResult = getaddrinfo(TCP_HOST, TCP_PORT, &hints, &result);
    if ( iResult != 0 ) {
        printf("getaddrinfo failed with error: %d\n", iResult);
        WSACleanup();
        return NULL;
    }

    // Attempt to connect to an address until one succeeds
    for(ptr=result; ptr != NULL ;ptr=ptr->ai_next) {

        // Create a SOCKET for connecting to server
        ConnectSocket = socket(ptr->ai_family, ptr->ai_socktype,
                               ptr->ai_protocol);
        if (ConnectSocket == INVALID_SOCKET) {
            printf("socket failed with error: %d\n", WSAGetLastError());
            WSACleanup();
            return NULL;
        }

        // Connect to server.
        iResult = connect( ConnectSocket, ptr->ai_addr, (int)ptr->ai_addrlen);
        if (iResult == SOCKET_ERROR) {
            closesocket(ConnectSocket);
            ConnectSocket = INVALID_SOCKET;
            continue;
        }
        break;
    }

    freeaddrinfo(result);

    if (ConnectSocket == INVALID_SOCKET) {
        printf("Unable to connect to server!\n");
        WSACleanup();
        return NULL;
    }

    iResult = send( ConnectSocket, buf, (int)strlen(buf), 0 );
    if (iResult == SOCKET_ERROR) {
        printf("send failed with error: %d\n", WSAGetLastError());
        closesocket(ConnectSocket);
        WSACleanup();
        return NULL;
    }

    iResult = shutdown(ConnectSocket, SD_SEND);
    if (iResult == SOCKET_ERROR) {
        printf("shutdown failed with error: %d\n", WSAGetLastError());
        closesocket(ConnectSocket);
        WSACleanup();
        return NULL;
    }
    int total = 0;
    do {
        iResult = recv(ConnectSocket, (char*)recvbuf, recvbuflen, 0);
        if ( iResult > 0 )
            total += iResult;
    } while( iResult > 0 );
    closesocket(ConnectSocket);
    WSACleanup();

    // Copy the received buffer to a new buffer that is null terminated
    char* recvbuf2 = malloc((total + 1) * sizeof(char));
    for (int i = 0; i < total; i++) {
        recvbuf2[i] = recvbuf[i];
    }
    recvbuf2[total] = '\0';
    return recvbuf2;
}
