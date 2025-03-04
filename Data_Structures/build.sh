#!/bin/bash

# Function to print usage
print_usage() {
    echo "Usage: $0 <command> <source_file.c>"
    echo "Commands:"
    echo "  run       - Compile and run the C file"
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

# Handle 'clean' command
if [ "$COMMAND" == "clean" ]; then
    if [ -z "$SOURCE_FILE" ]; then
        echo "Error: Please provide the source file for cleanup!"
        exit 1
    fi
    OUTPUT_FILE="${SOURCE_FILE%.c}"
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

# Find ak_utils.h anywhere in the Git repo
HEADER_PATH=$(find "$GIT_ROOT" -type f -name "ak_utils.h" | head -n 1)

if [ -z "$HEADER_PATH" ]; then
    echo "Error: ak_utils.h not found anywhere in the repository!"
    exit 1
fi

# Extract the directory of ak_utils.h
HEADER_DIR=$(dirname "$HEADER_PATH")

# Find ak_utils.c and compile it if needed
ak_utils_C=$(find "$GIT_ROOT" -type f -name "ak_utils.c" | head -n 1)

if [ -z "$ak_utils_C" ]; then
    echo "Error: ak_utils.c not found!"
    exit 1
fi

# Get output file name (remove .c extension)
OUTPUT_FILE="${SOURCE_FILE%.c}"

# Compile ak_utils.c first
gcc -c "$ak_utils_C" -I"$HEADER_DIR" -Wall -Wextra -std=c99 -o ak_utils.o

# Compile the provided C file and link with ak_utils.o
gcc -o "$OUTPUT_FILE" "$SOURCE_FILE" ak_utils.o -I"$HEADER_DIR" -Wall -Wextra -std=c99 || exit 1

# Run the compiled program
echo "Compilation successful! Running $OUTPUT_FILE..."
./"$OUTPUT_FILE"

