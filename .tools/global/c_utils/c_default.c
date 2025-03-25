#include <stdio.h>
#include <stdlib.h>
#include "ak_utils.h"  // Include ak_utils.h

#define CURRENT_PROGRAM_NAME "Current Program Name"

int main() {

    set_program_name(CURRENT_PROGRAM_NAME);
    print_provenance();  // Call provenance function

    return 0;
}
