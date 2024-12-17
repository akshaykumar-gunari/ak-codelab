#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: bubble_sort.py
Description: Bubble Sort Algorithm Implementation
Author: Akshaykumar Gunari
Created: 2024-12-17
Last Modified: 2024-12-17
Version: 1.0.0
Python: 3.8+

This is a simple implementation of Bubble Sort Algorithim

Execution: python bubble_sort.py

"""

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

from typing import List, Union

def bubble_sort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Perform bubble sort on the input list.
    Args:
        arr (List[Union[int, float]]): Input list of numbers to be sorted
    Returns:
        List[Union[int, float]]: Sorted list in ascending order
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        # Flag to optimize by detecting if any swap happened
        swapped = False
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    return arr

def main():
    print_provenance()
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array: ", array)
    sorted_array = bubble_sort(array)
    print("Sorted array:", sorted_array)

if __name__ == "__main__":
    main()
