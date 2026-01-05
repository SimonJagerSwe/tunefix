# Imports
import argparse
import os
import sys


dir_arg = rf""
s_list = []


# Main function
def main():
    a_dir = parse_args(dir_arg)
    print(a_dir)
    s_list = identify_files(a_dir)
    print(s_list)
    # print(remove_prefix(s_list))
    trunc_list = remove_prefix(s_list)
    # print(trunc_list)
    fixed_list = add_prefix(trunc_list)
    rename(a_dir, fixed_list)


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
        s_list.append(song)
    return s_list


def remove_prefix(s_list):
    truncated_list = []
    for tune in s_list:
        prefix = tune[:3]
        # print(prefix)
        truncated_tune = tune.strip(prefix)
        # print(truncated_tune)
        truncated_list.append(truncated_tune)
    # print(truncated_list)
    return truncated_list


def add_prefix(trunc_list):
    n = 1
    fixed_list = []
    for tune in trunc_list:
        if n < 10:
            prefix = f"0{n}"
        else:
            prefix = f"{n}"
        new_tune = f"{prefix} - {tune}"
        print(new_tune)
        fixed_list.append(new_tune)
        n += 1
    return fixed_list


def rename(a_dir, fixed_list):
    print(a_dir)
    # print(fixed_list)
    n = 0
    for tune in os.listdir(a_dir):
        print(tune)
        os.rename(f"{a_dir}\\{tune}", f"{a_dir}\\{fixed_list[n]}")
        n += 1
    

# Execute main function
if __name__ == "__main__":
    main()