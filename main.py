# Imports
import argparse
import os


dir_arg = rf""
pre_arg = f""
str_arg = f""
s_list = []
ext_list = []
stripped_list = []


# Main function
def main():
    args = parse_args(dir_arg)
    d_arg = args[0]
    p_arg = args[1]
    s_arg = args[2]
    print(f"File directory: {d_arg}")
    print(f"Number of initial characters to remove: {p_arg}")
    print(f"Part of titles to remove: {s_arg}")
    print(type(p_arg))
    if p_arg != "None":
        print("Removal argumet appears to be an integer")
        p_arg = int(p_arg)
    print(p_arg)
    print(type(p_arg))
    s_list = identify_files(d_arg)
    print(s_list)
    ext_list = fix_extension(s_list)
    print(ext_list)
    stripped_name = remove_string(ext_list, s_arg)
    print(stripped_list)
    print(s_list[0][0:5])
    if s_list[0][0:5] == "01 - ":
        print("Song number format already valid")
        rename(d_arg, stripped_name)
    else:
        print("Renaming files")
        trunc_list = remove_prefix(ext_list, p_arg)
        print(trunc_list)
        new_list = add_prefix(trunc_list)
        print(new_list)
        rename(d_arg, new_list)
    print("Renaming succesfull!")


# Parse arguments
def parse_args(dir_arg):
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="The directory containing the tracks you want to change the names of")
    parser.add_argument("-p", "--prefix", help="Number of initial characters to remove")
    parser.add_argument("-s", "--string_strip", help="Part to strip")
    args = parser.parse_args()
    dir_arg = rf"{args.directory}"
    pre_arg = f"{args.prefix}"
    str_arg = f"{args.string_strip}"
    return dir_arg, pre_arg, str_arg


# Walk through directory to identify files
def identify_files(d_arg):
    for song in os.listdir(d_arg):
        print(song.title())
        song = song.title()
        s_list.append(song)
    return s_list


def fix_extension(s_list):
    # print(s_list)
    for song in s_list:
        song_ext = song[-3:]
        song = song.strip(song_ext)
        song_name = f"{song}mp3"
        print(song_name)
        ext_list.append(song_name)
    return ext_list


def remove_prefix(ext_name, p_arg):
    truncated_list = []
    print(p_arg)
    print(type(p_arg))
    if p_arg != "None":
        if type(p_arg) == int:
            print("p_arg is int")
            for tune in ext_name:
                prefix = tune[:p_arg + 1]
                print(prefix)
                truncated_tune = tune.strip(prefix)
                print(truncated_tune)
                truncated_list.append(truncated_tune)
        else:
            for tune in ext_name:
                truncated_tune = tune.strip(p_arg)
                print(truncated_tune)
                truncated_list.append(truncated_tune)
    else:
        for tune in ext_name:
            prefix = tune[:3]
            truncated_tune = tune.strip(prefix)
            print(truncated_tune)
            truncated_list.append(truncated_tune)
    return truncated_list


def remove_string(ext_list, s_arg):
    # print(ext_list)
    print(s_arg)
    for song in ext_list:
        print(song)
        stripped_song = song.replace(s_arg, "")
        print(stripped_song)
        stripped_list.append(stripped_song)
    return stripped_list

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


def rename(d_arg, new_list):
    print(d_arg)
    n = 0
    for tune in os.listdir(d_arg):
        print(f"{tune}")
        if tune[-1] != "3":
            tune = f"{tune}3"
        os.rename(f"{d_arg}\\{tune}", f"{d_arg}\\{new_list[n]}")
        n += 1
    
    

# Execute main function
if __name__ == "__main__":
    main()
