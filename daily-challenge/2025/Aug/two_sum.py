#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: two_sum.py
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Author: Akshaykumar Gunari
Created: 2025-08-06
Last Modified: 2025-08-06
Version: 1.0.0
Python: 3.8+

This script outputs the indices of two numbers in an array whose sum is equal to the given target.

Execution: python file_name.py

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

# Add the directory containing ak_utils.py to the system path
sys.path.insert(0, get_git_root())
import python_utils
from python_utils import ak_utils

def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]

def main():
    ak_utils.__status__ = "Completed"
    ak_utils.print_provenance()
    indices = two_sum([2, 7, 11, 15], 9)
    print(indices)

if __name__ == "__main__":
    main()
