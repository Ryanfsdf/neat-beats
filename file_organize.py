#! python3

import os
import re

from mutagen.mp3 import EasyMP3
from mutagen.flac import FLAC
from mutagen.mp4 import MP4


def organize_file(file):
    """
    organize_file takes in a file directory and organizes the file into its corresponding folder
    :param file: directory of file
    :return: organizes the music file into a folder in the format 'Artist - Album' in the main directory
    """
    if file.lower().endswith('.mp3') | file.lower().endswith('.flac'):
        if file.lower().endswith('.mp3'):
            audio = EasyMP3(file)

        if file.lower().endswith('.flac'):
            audio = FLAC(file)

        try:
            new_artist = audio['artist']
            new_album = audio['album']
            try:
                os.makedirs(re.sub('[^A-Za-z0-9\s]+', '', str(new_artist)) + ' - ' +
                            re.sub('[^A-Za-z0-9\s]+', '', str(new_album)))
            except:
                pass
            os.rename(file, os.path.join((re.sub('[^A-Za-z0-9\s]+', '', str(new_artist)) + ' - ' +
                                          re.sub('[^A-Za-z0-9\s]+', '', str(new_album))), file))
        except:
            try:
                os.makedirs('000 NO ALBUM SONGS')
            except:
                pass
            try:
                os.rename(file, os.path.join('000 NO ALBUM SONGS', file))
            except:
                print('Could not move ' + file)

    if file.lower().endswith('.m4a'):
        audio = MP4(file)
        try:
            new_artist = audio['\xa9ART']
            new_album = audio['\xa9alb']
            try:
                os.makedirs(re.sub('[^A-Za-z0-9\s]+', '', str(new_artist)) + ' - ' +
                            re.sub('[^A-Za-z0-9\s]+', '', str(new_album)))
            except:
                pass
            os.rename(file, os.path.join((re.sub('[^A-Za-z0-9\s]+', '', str(new_artist)) + ' - ' +
                                          re.sub('[^A-Za-z0-9\s]+', '', str(new_album))), file))
        except:
            try:
                os.makedirs('000 NO ALBUM SONGS')
            except:
                pass
            try:
                os.rename(file, os.path.join('000 NO ALBUM SONGS', file))
            except:
                print('Could not move ' + file)
