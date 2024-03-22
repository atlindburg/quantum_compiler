#!/bin/bash

# Check if an input file was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_c_file>"
    exit 1
fi

input_file="$1"
filename=$(basename -- "$input_file")
extension="${filename##*.}"
filename="${filename%.*}"

# Ensure the file is a .c file
if [ "$extension" != "c" ]; then
    echo "The file must be a .c file"
    exit 1
fi

# Directory where the header file will be saved
include_dir="./include"

# Ensure the include directory exists
if [ ! -d "$include_dir" ]; then
    echo "The include directory does not exist, creating it now..."
    mkdir -p "$include_dir"
fi

# Output header file path
header_file="${include_dir}/${filename}.h"

# Create or overwrite the header file
echo "#ifndef ${filename^^}_H" > "$header_file"
echo "#define ${filename^^}_H" >> "$header_file"
echo "" >> "$header_file"

# Extract and append function declarations from the C file to the header file
grep -oP 'void\s+\w+\([^)]*\)\s*;' "$input_file" >> "$header_file"

# Append closing endif
echo "" >> "$header_file"
echo "#endif // ${filename^^}_H" >> "$header_file"

echo "Header file generated at $header_file"

