#! python3

import os
import get_input


# TO DO - remove digit in track number for numbers larger than 2 digits
# - make a safety catch to leave song alone if the title is less than 4 characters?
# - fix bad files (files with no metadata) not being put into 000 NO ALBUM SONGS


response = input("run - Collapse all folders and rename music files" + os.linesep +
                 "organize - Organize all music files into folders for "
                 "their corresponding album/artist name" + os.linesep +
                 "quit - exit the program" + os.linesep +
                 "Type your command:")

get_input.type_input(response)
