#ifndef AK_UTILS_HPP
#define AK_UTILS_HPP

#include <iostream>
#include <string>
using namespace std;

// Metadata constants
constexpr const char* AUTHOR = "Akshaykumar Gunari";
constexpr const char* COPYRIGHT = "Copyright 2025, AK World";
constexpr const char* CREDITS = "Akshaykumar Gunari";
constexpr const char* LICENSE = "GPL-3.0";
constexpr const char* VERSION = "1.0.0";
constexpr const char* MAINTAINER = "Akshaykumar Gunari";
constexpr const char* EMAIL = "akshaygunari@gmail.com";
constexpr const char* STATUS = "Under Development";

// Function declarations
void set_program_name(const std::string& new_name);
void print_provenance();
void clear_input_buffer();

#endif // AK_UTILS_HPP

