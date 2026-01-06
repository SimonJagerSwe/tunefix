# Imports
import argparse
import os
# import sys


dir_arg = rf""
rep_arg = f""
s_list = []


# Main function
def main():
    args = parse_args(dir_arg)
    d_arg = args[0]
    p_arg = args[1]
    print(d_arg)
    print(p_arg)
    s_list = identify_files(d_arg)
    # print(s_list)
    trunc_list = remove_prefix(s_list, p_arg)
    print(trunc_list)
    print(trunc_list[0][0:5])
    if trunc_list[0][0:5] != "01 - ":
        fixed_list = add_prefix(trunc_list)
    else:
        fixed_list = trunc_list
    print(trunc_list)
    print(fixed_list)
    # rename(d_arg, fixed_list)
    print("Renaming succesfull!")


# Parse arguments
def parse_args(dir_arg):
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="The directory containing the tracks you want to change the names of")
    parser.add_argument("-r", "--replace", help="Final index of replacement")
    args = parser.parse_args()
    dir_arg = rf"{args.directory}"
    rep_arg = f"{args.replace}"
    return dir_arg, rep_arg


# Walk through directory to identify files
def identify_files(d_arg):
    for song in os.listdir(d_arg):
        print(song)
        s_list.append(song)
    return s_list


def remove_prefix(s_list, p_arg):
    print(bool(p_arg == None))
    print(p_arg)
    truncated_list = []
    if p_arg:
        for tune in s_list:
            truncated_tune = tune.strip(p_arg)
            print(truncated_tune)
            truncated_list.append(truncated_tune)
    else:
        for tune in s_list:
            prefix = tune[:3]
            truncated_tune = tune.strip(prefix)
            truncated_list.append(truncated_tune)
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


def rename(d_arg, fixed_list):
    print(d_arg)
    n = 0
    for tune in os.listdir(d_arg):
        print(tune)
        # if tune[1] == "3":
        #   os.rename(f"{d_arg}\\{tune}", f"{d_arg}\\{fixed_list[n]}3")
        os.rename(f"{d_arg}\\{tune}", f"{d_arg}\\{fixed_list[n]}")
        n += 1
    

# Execute main function
if __name__ == "__main__":
    main()
