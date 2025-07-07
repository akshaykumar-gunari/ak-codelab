#!/bin/bash

# Function to print usage
print_usage() {
    echo "Usage: $0 <command> <source_file.(c|cpp)>"
    echo "Commands:"
    echo "  run       - Compile and run the file"
    echo "  clean     - Remove the compiled binary"
    exit 1
}

# Ensure a command is provided
if [ -z "$1" ]; then
    print_usage
fi

COMMAND=$1
SOURCE_FILE=$2

# Find the root of the Git repository
GIT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

if [ -z "$GIT_ROOT" ]; then
    echo "Error: Not inside a Git repository!"
    exit 1
fi

# Check file extension
EXT="${SOURCE_FILE##*.}"

if [ "$EXT" != "c" ] && [ "$EXT" != "cpp" ]; then
    echo "Error: Source file must be .c or .cpp!"
    exit 1
fi

# Pick compiler and flags based on extension
if [ "$EXT" == "c" ]; then
    COMPILER="gcc"
    STD="-std=c99"
    HEADER_EXT="h"
    UTILS_SRC="ak_utils.c"
elif [ "$EXT" == "cpp" ]; then
    COMPILER="g++"
    STD="-std=c++17"
    HEADER_EXT="hpp"
    UTILS_SRC="ak_utils.cpp"
fi

# Handle 'clean' command
if [ "$COMMAND" == "clean" ]; then
    if [ -z "$SOURCE_FILE" ]; then
        echo "Error: Please provide the source file for cleanup!"
        exit 1
    fi
    OUTPUT_FILE="${SOURCE_FILE%.*}"
    if [ -f "$OUTPUT_FILE" ]; then
        rm "$OUTPUT_FILE" ak_utils.o
        echo "Cleaned up $OUTPUT_FILE and ak_utils.o"
    else
        echo "No compiled binary found for $SOURCE_FILE"
    fi
    exit 0
fi

# Ensure a source file is provided for 'run'
if [ -z "$SOURCE_FILE" ]; then
    print_usage
fi

# Check if the file exists
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: File '$SOURCE_FILE' not found!"
    exit 1
fi

# Find ak_utils header
HEADER_PATH=$(find "$GIT_ROOT" -type f -name "ak_utils.$HEADER_EXT" | head -n 1)

if [ -z "$HEADER_PATH" ]; then
    echo "Error: ak_utils.$HEADER_EXT not found anywhere in the repository!"
    exit 1
fi

HEADER_DIR=$(dirname "$HEADER_PATH")

# Find ak_utils source file
UTILS_PATH=$(find "$GIT_ROOT" -type f -name "$UTILS_SRC" | head -n 1)

if [ -z "$UTILS_PATH" ]; then
    echo "Error: $UTILS_SRC not found!"
    exit 1
fi

# Output file name
OUTPUT_FILE="${SOURCE_FILE%.*}"

# Compile ak_utils
$COMPILER -c "$UTILS_PATH" -I"$HEADER_DIR" -Wall -Wextra "$STD" -o ak_utils.o

# Compile main
$COMPILER -o "$OUTPUT_FILE" "$SOURCE_FILE" ak_utils.o -I"$HEADER_DIR" -Wall -Wextra "$STD" || exit 1

echo "Compilation successful! Running $OUTPUT_FILE..."
./"$OUTPUT_FILE"
