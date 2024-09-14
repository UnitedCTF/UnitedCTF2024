#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char global_secret[] = "312493148856567829373678711575994142322696845";
char global_secret2[] = "827399265857154623183952768944466359211773148";
char global_secret3[] = "919162158663732957414778262548913849453352678";
char global_secret4[] = "756851654229339475288494117593672181498336276";

char* global_secret_ptr = global_secret;
char* global_secret_ptr2 = global_secret2;
char* global_secret_ptr3 = global_secret3;
char* global_secret_ptr4 = global_secret4;

char FLAG1[] = "flag-undocumented_functions_are_fun";
char FLAG2_ENC[] =   "\x2f\x14\x57\x5e\x55\x30\x4b\x5e\x17\x1c\x57\x2a\x15\x24\x0d\x2c\x72\x1c\x16\x5a\x29\x1e\x2e\x32\x16\x77";
const int FLAG2_LEN = 26;
char FLAG2_KEY[] = "Na10cZ14xJ3QwmrJ4xz0JHPDxp7";
//char FLAG2[] = "flag-such_crypto_much_wow";
//char FLAG3[] = "flag-symbolic_execution_is_op";

#pragma GCC push_options
#pragma GCC optimize ("O0")

#pragma optimize( "", off )
char* XOR(char* a, char* b, unsigned int len) { //XOR two strings together and return result

    char* c = (char*)malloc(len + 1);
    memset(c, 0, len + 1);

    for (int i = 0; i < len; ++i) {
        c[i] = a[i] ^ b[i];
    }

    return c;
}

char* XOR_ADD(char* a, char* b, unsigned int len) { //XOR two strings together and return result

    char* c = (char*)malloc(len + 1);
    memset(c, 0, len + 1);

    for (int i = 0; i < len; ++i) {
        c[i] =(a[i] ^ b[i]) + 7;
    }

    return c;
}


void print_hex(const char* s)
{
    while (*s)
    {
        printf("%02x", ((unsigned int) *s) %256);
        s++;
    }
    printf("\n");
}

// Function to reverse a string and store the result in a new string
char* reverseString(const char* str) {
    int length = strlen(str);

    // Allocate memory for the reversed string
    char* reversed = (char*)malloc((length + 1) * sizeof(char));
    if (reversed == NULL) {
        printf("Memory allocation failed!\n");
        return NULL;
    }

    // Reverse the string
    for (int i = 0; i < length; i++) {
        reversed[i] = str[length - i - 1];
    }
    reversed[length] = '\0'; // Null-terminate the reversed string

    return reversed;
}

int complex_function(int x, int y, int z) {

    int L = 256;
    if (!('a' <= x && x <= 'z')) {
        printf("Try again.\n");
        exit(1);
    }
    int a = x - 'a';
    int b = (a + (z * y)) % L;
    int c = b + 'a';

    // Additional unnecessary calculations
    int d = ((c - 'a') * y) % L;
    int e = (d + 5 + (y * z)) % L;
    int f = (e + y + z) % L;
    int g = (f * y) % L;

/* Removed because it makes angr too slow
    // More unnecessary calculations
    int h = ((g - 'a') * z) % L;
    int i = (h + (z * y * 3)) % L;
    int j = (i + y * 2 + z) % L;
    int k = (j * z) % L;

    // Even more unnecessary calculations
    int m = ((k - 'a') * (y + z)) % L;
    int n = (m + (y * z)) % L;
    int o = (n + z + y) % L;
    int p = (o * (y + z)) % L;

    // Additional unnecessary transformation
    a = p + 'a';
    */

    a = c + 'a';
    a = ((a - 'a' + (L * y)) % ('z' - 'a' + 1)) + 'a';
    return a;
}

#pragma optimize( "", off )
void chal3_init1() {

    char* str;
    global_secret[0] = global_secret2[1];
    global_secret[2] = global_secret2[7];
    global_secret[6] = global_secret2[2];
    global_secret[1] = global_secret2[6];
    global_secret[4] = global_secret2[4];
    global_secret[15] = global_secret2[3];
    global_secret[9] = global_secret2[0];

    srand(*((unsigned int *) global_secret));  
    int randnum = rand();
 
    str = reverseString(global_secret);

    str[0] = randnum % 256;
    str[1] = (randnum >> 8 ) % 256;
    str[2] = (randnum >> 16) % 256;
    str[3] = (randnum >> 24) % 256;
    XOR(global_secret4, str, 45);
}

#pragma optimize( "", off )
void chal3_init2() {

    int i = 42;
    srand(*((unsigned int*)global_secret2));
    int randnum = rand();
    char* str;
    global_secret3[24] = global_secret[5];
    global_secret3[13] = global_secret[22];
    global_secret3[12] = global_secret[23];
    global_secret3[4] = global_secret[15];
    global_secret3[5] = global_secret2[4];
    global_secret3[8] = global_secret[3];
    global_secret3[1] = global_secret[6];


    str = reverseString(global_secret);
    // TODO: maybe change this to something different and weirder than shift
    str[0] = randnum  % 256;
    str[1] = (randnum >> 8) % 256;
    str[2] = (randnum >> 16) % 256;
    str[3] = (randnum >> 24) % 256;
    reverseString(global_secret);
}

char* complex_function_wrapper(char* buffer) {
#define LEN_USERDEF 21

    chal3_init1();
    chal3_init2();

    for (int i = 0; i < LEN_USERDEF; ++i) {
        buffer[i] = complex_function(buffer[i], * (global_secret_ptr4 + (*(global_secret_ptr4 + i) % 40) ), ((unsigned int)*(global_secret_ptr + i) + *(global_secret_ptr2 + ((i * 2) )) + *(global_secret_ptr3 + ((i * 2) )))%256);
        }
    return buffer;
}

#pragma optimize( "", off )
void chal3() {
#define LEN_USERDEF 21
#define USERDEF "nndrdylrsmvzswybaxlul"
#define BUFLEN LEN_USERDEF+1
    char buffer[BUFLEN];
    char buffercopy[BUFLEN];
    printf("=============================\nDecryption key recovery function activated. \nEnter the admin password: ");

    scanf("%21s", buffer);
    memcpy(buffercopy, buffer, BUFLEN);

    complex_function_wrapper(buffer);

    //puts(buffer);
    if (strcmp(buffer, USERDEF)) {
        printf("Try again.\n");
    }
    else {
        printf("File decryption key recovered: flag-%.8s_%.9s_%.2s_%.2s\n", buffercopy, buffercopy+8, buffercopy+17, buffercopy+19);
    }
}

void chal2() {

    // INPUT key or input flag?
    char userinput[FLAG2_LEN];
    char* result = 0;
    printf("DEBUG ENABLED\n");

    //printf("Encryption key: %s\n", FLAG2_KEY_REVERSED);
    printf("Encrypted debug password: ");
    print_hex(FLAG2_ENC);

    printf("Enter the decrypted debug password: ");
    scanf("%27s", userinput);

    result = XOR_ADD(FLAG2_KEY, userinput, FLAG2_LEN);
    //print_hex(result);
    if (!memcmp(result, FLAG2_ENC, FLAG2_LEN))
    {
        printf("Authentification successful. Flag: %s\n", userinput);
    }
    else
    {
        printf("Authentification failed.");
        exit(1);
    }

}
int main(int argc, char* argv[]) {

    if (argc == 2)
    {
        if (!strcmp(argv[1], "--debug-enable"))
        {
            printf("Flag: %s\n", FLAG1);

            chal2();
            chal3();
            return 0;
        }

    }

    printf("Unauthorized access detected, shutting down...");


    return 0;
}


#pragma GCC pop_options

/*
Après un incident de ransomware, ce binaire mystérieux a été découvert sur le poste de la victime. 
Il s'agit d'un programme de débogage qui a été oublié par l'attaquant et qui pourrait aider à récupérer les fichiers affectés. 
Votre mission est de trouver les clés secrètes cachées à l'intérieur.
*/
