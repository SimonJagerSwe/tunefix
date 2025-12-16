# Imports
import argparse
import os
import sys


# Main function
def main():
    # a_dir = r"C:\Users\simon\OneDrive\Dokument\Soulseek Downloads\complete\ahyonfelihufs\Awake"
    a_dir = rf""
    parse_args(a_dir)
    print(a_dir)
    identify_files(a_dir)

# Parse arguments
def parse_args(a_dir):
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="The directory containing the tracks you want to change the names of")
    parser.add_argument("-r", "--replace", help="Part of title to be replaced")
    # parser.add_argument("-n", "--new", help="New replacement")
    args = parser.parse_args()
    a_dir = rf"{args.directory}"
    print(rf"{args.directory}")
    # print(a_dir)    
    print(args.replace)
    # print(args.new)

    return a_dir



# Walk through directory to identify files
def identify_files(a_dir):
    for song in os.listdir(a_dir):
        print(song)




# Execute main function
if __name__ == "__main__":
    main()