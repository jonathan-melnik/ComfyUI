#!/bin/bash

# Check if the target directory is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <target-directory>"
    exit 1
fi

# Define folders for symlinks
folders=("output" "input" "models" "temp" "user")

# Target directory (where original folders are located)
target_dir="$1"

# Create symlinks in the current directory pointing to the target directory
for folder in "${folders[@]}"; do
    ln -sfn "$target_dir/$folder" "$folder"
    echo "Symlink created: $folder -> $target_dir/$folder"
done
