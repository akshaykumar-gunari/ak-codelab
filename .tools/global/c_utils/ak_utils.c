#include "ak_utils.h"

const char *PROGRAM_NAME = "ak_utils";
void set_program_name(const char *new_name) {
    PROGRAM_NAME = new_name;  // Modify the pointer
}

void print_provenance() {
    printf("\n***********************************************\n");
    printf("Program: %s\n", PROGRAM_NAME);
    printf("Author: %s\n", AUTHOR);
    printf("Copyright: %s\n", COPYRIGHT);
    printf("Credits: %s\n", CREDITS);
    printf("License: %s\n", LICENSE);
    printf("Version: %s\n", VERSION);
    printf("Maintainer: %s\n", MAINTAINER);
    printf("Email: %s\n", EMAIL);
    printf("Status: %s\n", STATUS);
    printf("***********************************************\n\n");
}

void clear_input_buffer() {
    while (getchar() != '\n');  // Clear the buffer
}
