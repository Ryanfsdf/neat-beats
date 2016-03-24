#! python3

import os
import get_input

# TO DO - clean up exceptions in file_organize


response = input('run - Collapse all folders and rename music files' +
                 os.linesep +
                 'organize - Organize all music files into folders for '
                 'their corresponding album/artist name' + os.linesep +
                 'quit - exit the program' + os.linesep +
                 'Type your command: ')

get_input.type_input(response)
