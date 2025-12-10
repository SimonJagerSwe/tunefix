# Imports
import argparse
import os
import sys

# Test arguments
# -d "C:\Users\simon\OneDrive\Dokument\Soulseek Downloads\complete\ahyonfelihufs\Awake"
# -r "0{n} "
# -n "0{n} - "
# -d "C:\Users\simon\OneDrive\Dokument\Soulseek Downloads\complete\ahyonfelihufs\Awake" -r "0{n} " -n "0{n} - "


parser = argparse.ArgumentParser(
    prog="TuneFix",
    description="This fixes the names of sound files to conform with a given standard"
)

# Take arguments for album location
parser.add_argument("-d", default=r"", help="Directory of album to fix", type=str)

# Take arguments for string to replace
# parser.add_argument("-r", default="", help="File part to replace", type=str)

# Take arguments for new name
 #parser.add_argument("-n", default="", help="New file part", type=str)

# Initialise args
args = parser.parse_args()
print(args)


# Find files

# Apply changes to file

