# Imports
import argparse
import os
import sys


# Main function
def main():
    a_dir = r"C:\Users\simon\OneDrive\Dokument\Soulseek Downloads\complete\ahyonfelihufs\Awake"
    # get_file_dir(a_dir)
    identify_files(a_dir)

# Get file directory
def get_file_dir(a_dir):
    return a_dir

# Get file name part to replace
def to_be_replaced():
    ...

# Get file name replacement
def to_replace():
    ...

# Walk through directory to identify files
def identify_files(a_dir):
    for song in os.listdir(a_dir):
        print(song)




# Execute main function
if __name__ == "__main__":
    main()