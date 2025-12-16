# Imports
import argparse
import os
import sys

a_dir = r"C:\Users\simon\OneDrive\Skrivbord\Musik\Chick Corea Elektric Band\1990 - Inside Out"

def main():
    # print(a_dir)
    for root, dirs, files in os.walk(a_dir):
        # if os.path.basename(root) != "modules":
        #     continue
        print(f"Root: {root}")
        # print(f"Root type: {type(root)}")
        print(f"Dirs: {dirs}")
        # print(f"Dirs type: {type(dirs)}")
        print(f"File: {files}")
        # print(f"Files type: {type(files)}")



if __name__ == "__main__":
    main()