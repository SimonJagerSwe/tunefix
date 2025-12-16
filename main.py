# Imports
import argparse
import os
import sys


dir_arg = rf""

# Main function
def main():
    a_dir = parse_args(dir_arg)
    print(a_dir)
    identify_files(a_dir)


# Parse arguments
def parse_args(dir_arg):
    # print(dir_arg)
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="The directory containing the tracks you want to change the names of")
    parser.add_argument("-r", "--replace", help="Part of title to be replaced")
    # parser.add_argument("-n", "--new", help="New replacement")
    args = parser.parse_args()
    dir_arg = rf"{args.directory}"
    # print(dir_arg)    
    # print(args.replace)
    # print(args.new)
    return dir_arg


# Walk through directory to identify files
def identify_files(a_dir):
    for song in os.listdir(a_dir):
        print(song)


# Execute main function
if __name__ == "__main__":
    main()