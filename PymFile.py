#! python3

import os


def check_file(file):
    if file.endswith(".mp3"):
        from mutagen.mp3 import EasyMP3
        audio = EasyMP3(file)
        new_name = audio["title"]
        os.rename(file, str(new_name) + ".mp3")
    if file.endswith(".flac"):
        from mutagen.flac import FLAC
        try:
            audio = FLAC(file)
            new_name = audio["title"]
            os.rename(os.path.join('.', file), os.path.join('.', str(new_name) + '.flac'))
        except KeyError:
            print("Bad Flac", file)
    if file.endswith(".m4a"):
        from mutagen.mp4 import MP4
        audio = MP4(file)
        new_name = audio['\xa9nam']
        os.rename(os.path.join('.', file), os.path.join('.', str(new_name) + '.m4a'))

for dirname, dirnames, filenames in os.walk('.'):
    for subdirname in dirnames:
        check_file(os.path.join(dirname, subdirname))
    for filename in filenames:
        check_file(os.path.join(dirname, filename))