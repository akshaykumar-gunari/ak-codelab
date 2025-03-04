#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: image_normalized_histogram.py
Description: This script computes the histogram and normalized histogram of an image.
Author: Akshaykumar Gunari
Created: 2025-03-04
Last Modified: 2025-03-04
Version: 1.0.0
Python: 3.8+

This script computes the histogram and normalized histogram of a given grayscale image.
The normalized histogram is obtained by dividing the pixel frequency by the total number of pixels,
resulting in values between 0 and 1.

Key Features:
- Reads an image and converts it to grayscale (if not already).
- Computes the histogram of pixel intensities.
- Normalizes the histogram to make it independent of image size.
- Displays both the original and normalized histograms.


Execution: python image_normalized_histogram.py

"""
import sys
import os
import subprocess

import cv2
import numpy as np
import matplotlib.pyplot as plt

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

def main():
    ak_utils.__status__ = "Completed"
    ak_utils.print_provenance()
    # Load a grayscale image
    image = cv2.imread('text_document.jpg', cv2.IMREAD_GRAYSCALE)
    #image = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

    # Compute the histogram
    histogram, bins = np.histogram(image.flatten(), bins=256, range=[0,256])

    # Normalize the histogram
    total_pixels = image.size
    normalized_histogram = histogram / total_pixels

    # Plot the histograms
    plt.figure(figsize=(10,4))
    plt.subplot(1, 2, 1)
    plt.plot(histogram, color='black')
    plt.title('Original Histogram')

    plt.subplot(1, 2, 2)
    plt.plot(normalized_histogram, color='black')
    plt.title('Normalized Histogram')

    plt.show()

if __name__ == "__main__":
    main()
