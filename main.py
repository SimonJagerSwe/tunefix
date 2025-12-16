# Imports
import argparse
import os
import sys

A_DIR = ""

# Main function
def main():
    get_file_dir(A_DIR)
    identify_files()

# Get file directory
def get_file_dir(A_DIR):
    # Hard-coded file directory, for test
    A_DIR = r"C:\Users\simon\OneDrive\Dokument\Soulseek Downloads\complete\ahyonfelihufs\Awake"
    return A_DIR

# Get file name part to replace
def to_be_replaced():
    ...


# Get file name replacement
def to_replace():
    ...

# Walk through directory to identify files
def identify_files():
    # print(a_dir)
    for root, dirs, files in os.walk(A_DIR):
        # if os.path.basename(root) != "modules":
        #     continue
        # print(f"Root: {root}")
        # print(f"Root type: {type(root)}")
        # print(f"Dirs: {dirs}")
        # print(f"Dirs type: {type(dirs)}")
        print(f"File: {files}")
        # print(f"Files type: {type(files)}")




# Execute main function
if __name__ == "__main__":
    main()