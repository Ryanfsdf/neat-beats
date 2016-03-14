#! python3

import os
import re


def rename_file(file):
    if file.lower().endswith(".mp3"):
        try:
            from mutagen.mp3 import EasyMP3
            audio = EasyMP3(file)
            new_name = audio["title"]
            new_track_number = audio["tracknumber"]
            os.rename(file, re.sub('[^A-Za-z0-9\s]+', '', str(new_track_number)) + " " +
                      re.sub('[^A-Za-z0-9\s]+', '', str(new_name)) + ".mp3")
        except:
            try:
                from mutagen.mp3 import EasyMP3
                audio = EasyMP3(file)
                new_name = audio["title"]
                os.rename(file, re.sub('[^A-Za-z0-9\s]+', '', str(new_name)) + ".mp3")
            except:
                print("Bad Mp3", file)

    if file.lower().endswith(".flac"):
        try:
            from mutagen.flac import FLAC
            audio = FLAC(file)
            new_name = audio["title"]
            new_track_number = audio["tracknumber"]
            os.rename(file, re.sub('[^A-Za-z0-9\s]+', '', str(new_track_number)) + " " +
                      re.sub('[^A-Za-z0-9\s]+', '', str(new_name)) + ".flac")
        except:
            print("Bad Flac", file)

    if file.lower().endswith(".m4a"):
        try:
            from mutagen.mp4 import MP4
            audio = MP4(file)
            new_name = audio['\xa9nam']
            new_track_number = audio["trkn"]
            os.rename(file, re.sub('[^A-Za-z0-9\s]+', '', str(new_track_number)) + " " +
                      re.sub('[^A-Za-z0-9\s]+', '', str(new_name)) + ".m4a")
        except:
            print("Bad m4a", file)