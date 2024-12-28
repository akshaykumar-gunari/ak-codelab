#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Metadata as module-level variables
__author__ = "Akshaykumar Gunari"
__copyright__ = "Copyright 2024, AK World"
__credits__ = ["Akshaykumar Gunari"]
__license__ = "GPL-3.0"
__version__ = "1.0.0"
__maintainer__ = "Akshaykumar Gunari"
__email__ = "akshaygunari@gmail.com"
__status__ = "Under Development"

def print_provenance():
  print("***********************************************")
  print(f"Author: {__author__}")
  print(f"Copyright: {__copyright__}")
  print(f"Credits: {', '.join(__credits__)}")
  print(f"License: {__license__}")
  print(f"Version: {__version__}")
  print(f"Maintainer: {__maintainer__}")
  print(f"Email: {__email__}")
  print(f"Status: {__status__}")
  print("***********************************************\n")
