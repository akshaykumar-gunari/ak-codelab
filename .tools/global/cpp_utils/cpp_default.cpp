#include "ak_utils.hpp"

int main() {
    const std::string CURRENT_PROGRAM_NAME = "Current CPP Program";

    set_program_name(CURRENT_PROGRAM_NAME);
    print_provenance();

    return 0;
}
