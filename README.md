# File renamer
# This script contains three functions and takes up to three arguments:
### "-d" is the path to the directory containing the files to be renamed, takes a string.
### "-p" is the prefix you want to remove (for instance other enumeration types), takes an integer representing how many characters will be stripped from the start of the file name.
### "-s" is a string to be stripped from anywhere in the file name.
## Usage example: 
Given the provided example file name: '[01] - Artist Name - Song Name', and our desired outcome: 01 - Song Name', applying the following cmd prompt:

python main.py -d '/.../artist/album' -p 7 -s 'Artist Name - '

will yield the following result:
'-d "/.../artist/album"' will provide the location of all the files
'-p 7' will select the undesired enumeration of "[01] - ", leaving us with 'Artist Name - Song Name'
'-s "Artist Name - "' will strip everything down to just the song name
The script will then enumerate the songs based on the order in the directory, so some form of original enumeration ("Artist Name - Track Number - Song Name", "[Track Number] - Artist Name - Song Name", "Track Number - Song Name" etc.) will be needed to begin with, otherwise songs will be enumerated in alphabetical order.
