#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: file_name.py
Description: <Description>
Author: Akshaykumar Gunari
Created: 2025-03-04
Last Modified: 2025-03-04
Version: 1.0.0
Python: 3.8+

Detailed description in one to two lines.

Execution: python file_name.py

"""
import sys
import os
import subprocess
import python_utils

def get_git_root():
    try:
        git_root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).strip().decode()
        # Get the absolute path of the directory containing python_utils.py
        return os.path.abspath(os.path.join(git_root, ".tools/global/"))
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None  # Not in a Git repository or Git is not installed

# Add the directory containing python_utils.py to the system path
sys.path.insert(0, get_git_root())
import python_utils

def main():
    python_utils.__status__ = "Under Development"
    python_utils.print_provenance()

if __name__ == "__main__":
    main()
