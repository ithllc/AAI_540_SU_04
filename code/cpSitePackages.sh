#!/bin/bash

# Directory containing the packages
src_dir="/opt/conda/lib/python3.10/site-packages"
# Destination directory
dest_dir="/home/sagemaker-user/python/lib/python3.10"

# Ensure the destination directory exists
mkdir -p "$dest_dir"

# Read each line from requirements.txt
while IFS= read -r line; do
    # Extract the package name (before '==')
    pkg_name=$(echo "$line" | cut -d'=' -f1)
    
    # Check if a directory for the package exists in the site-packages
    if [ -d "$src_dir/$pkg_name" ]; then
        # Copy the package directory to the destination
        cp -r "$src_dir/$pkg_name" "$dest_dir"
    fi
done < requirements.txt