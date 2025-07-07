#include "ak_utils.hpp"

static std::string PROGRAM_NAME = "ak_utils";

void set_program_name(const std::string& new_name) {
    PROGRAM_NAME = new_name;
}

void print_provenance() {
    std::cout << "\n***********************************************\n";
    std::cout << "Program: " << PROGRAM_NAME << "\n";
    std::cout << "Author: " << AUTHOR << "\n";
    std::cout << "Copyright: " << COPYRIGHT << "\n";
    std::cout << "Credits: " << CREDITS << "\n";
    std::cout << "License: " << LICENSE << "\n";
    std::cout << "Version: " << VERSION << "\n";
    std::cout << "Maintainer: " << MAINTAINER << "\n";
    std::cout << "Email: " << EMAIL << "\n";
    std::cout << "Status: " << STATUS << "\n";
    std::cout << "***********************************************\n\n";
}

void clear_input_buffer() {
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}
