#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: linear_search.py
Description: Implementation of Linear Search Algorithm
Author: Akshaykumar Gunari
Created: 2024-12-28
Last Modified: 2024-12-28
Version: 1.0.0
Python: 3.8+

Linear search is a simple searching algorithm that checks each element in an array one by one until it finds the desired value. It compares the target value with each element in the array, returning its index if found or -1/None otherwise..

Execution: python linear_search.py

"""
import sys
import os
import subprocess

def get_git_root():
    try:
        git_root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).strip().decode()
        # Get the absolute path of the directory containing python_utils.py
        return os.path.abspath(os.path.join(git_root, ".tools/global/"))
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None  # Not in a Git repository or Git is not installed

# Add the directory containing python_utils.py to the system path
sys.path.insert(0, get_git_root())
from python_utils import ak_utils

def linear_search(list_x, element):
    len_x = len(list_x)
    found = -1
    for i in range(len_x):
        if element == list_x[i]:
            found = 1
            return i + 1
    return found

def main():
    ak_utils.print_provenance()
    list_x = [x for x in range(20)]
    print(list_x)
    element = 6
    position = linear_search(list_x, element)
    if -1 != position:
        print("Element", element, "found at position:", position, "\n")
    else:
        print("Element", element, "not present in the list")

if __name__ == "__main__":
    main()
