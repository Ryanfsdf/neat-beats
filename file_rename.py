#! python3

import os
import re

from mutagen.mp3 import EasyMP3
from mutagen.flac import FLAC
from mutagen.mp4 import MP4


def rename_file(file):
    """
    rename_file takes in a file directory and renames the file in accordance
        to its actual name from its metadata
    :param file: directory of file
    :return: renames the music file in the format '?Track# Name' and puts
        it in the main directory
    """
    if file.lower().endswith('.mp3'):
        audio = EasyMP3(file)
        try:
            new_name = audio['title']
            if 'tracknumber' in audio:
                new_track_number = re.sub(r'[^0-9]+', '',
                                          str(audio['tracknumber']))
                """
                This part is very arbitrary. Some audio files give the
                track number in the form track#/total-track# while others
                just leave it as the track# by itself. Now, The logic here
                is that every track number with a length of 3 is usually a
                track#/total-track# without the slash. If the length is 4,
                then it is a 2 digit # with track#/total-track# So, to
                verify this, check if the first # is smaller than the second.
                Anything with 2 digits or less means it is most likely
                just the track# with no total-track#. Anything with more than
                4 digits means it uses a different format which is rare enough
                to be ignored.
                """
                if len(new_track_number) == 1:
                    new_track_number = '0' + new_track_number
                if len(new_track_number) == 3:
                    if (int(new_track_number[:1]) <= int(
                            new_track_number[1:])):
                        new_track_number = '0' + new_track_number[:1]
                if len(new_track_number) == 4:
                    if (int(new_track_number[:2]) <= int(
                            new_track_number[2:])):
                        new_track_number = new_track_number[:2]
                if len(new_track_number) >= 5:
                    new_track_number = ''
            else:
                new_track_number = ''
            os.rename(file, new_track_number + ' ' +
                      re.sub('[^A-Za-z0-9\s]+', '',
                             str(new_name)) + '.mp3')
        except KeyError:
            print('Bad Mp3', file)

    if file.lower().endswith('.flac'):
        audio = FLAC(file)
        try:
            new_name = audio['title']
            if 'tracknumber' in audio:
                new_track_number = re.sub(r'[^0-9]+', '',
                                          str(audio['tracknumber']))
                if len(new_track_number) == 1:
                    new_track_number = '0' + new_track_number
                if len(new_track_number) == 3:
                    if (int(new_track_number[:1]) <= int(
                            new_track_number[1:])):
                        new_track_number = '0' + new_track_number[:1]
                if len(new_track_number) == 4:
                    if (int(new_track_number[:2]) <= int(
                            new_track_number[2:])):
                        new_track_number = new_track_number[:2]
                if len(new_track_number) >= 5:
                    new_track_number = ''
            else:
                new_track_number = ''
            os.rename(file, new_track_number + ' ' +
                      re.sub('[^A-Za-z0-9\s]+', '',
                             str(new_name)) + '.flac')
        except KeyError:
            print('Bad Flac', file)

    if file.lower().endswith('.m4a'):
        audio = MP4(file)
        try:
            new_name = audio['\xa9nam']
            if 'trkn' in audio:
                new_track_number = re.sub(r'[^0-9]+', '',
                                          str(audio['trkn']))
                # M4a files attach a 0 at the end of every track number
                # so the slicing needed to be shifted
                if len(new_track_number) == 2:
                    new_track_number = '0' + new_track_number[:1]
                if len(new_track_number) == 3:
                    new_track_number = new_track_number[:2]
                if len(new_track_number) == 4:
                    if (int(new_track_number[:1]) <= int(
                            new_track_number[1:3])):
                        new_track_number = new_track_number[:1]
                if len(new_track_number) == 5:
                    if (int(new_track_number[:2]) <= int(
                            new_track_number[2:4])):
                        new_track_number = new_track_number[:2]
                if len(new_track_number) >= 6:
                    new_track_number = ''
            else:
                new_track_number = ''
            os.rename(file, new_track_number + ' ' +
                      re.sub('[^A-Za-z0-9\s]+', '',
                             str(new_name)) + '.m4a')
        except KeyError:
            print('Bad M4a', file)
