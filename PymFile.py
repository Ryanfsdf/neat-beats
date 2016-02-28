#! python3

import os
import re


def check_file(file):
    if file.lower().endswith(".mp3"):
        try:
            from mutagen.mp3 import EasyMP3
            audio = EasyMP3(file)
            new_name = audio["title"]
            new_artist = audio["artist"]
            new_track_number = audio["tracknumber"]
            new_album = audio["album"]
            os.rename(file, re.sub('[^A-Za-z0-9]+', '', str(new_album)) + "_" +
                      re.sub('[^A-Za-z0-9]+', '', str(new_name)) + "_" +
                      re.sub('[^A-Za-z0-9]+', '', str(new_track_number)) + "_" +
                      re.sub('[^A-Za-z0-9]+', '', str(new_artist)) + ".mp3")

        except:
            try:
                from mutagen.mp3 import EasyMP3
                audio = EasyMP3(file)
                new_name = audio["title"]
                new_artist = audio["artist"]
                os.rename(file, re.sub('[^A-Za-z0-9]+', '', str(new_album)) + "_" +
                          re.sub('[^A-Za-z0-9]+', '', str(new_name)) + "_" +
                          re.sub('[^A-Za-z0-9]+', '', str(new_artist)) + ".mp3")
            except:
                try:
                    from mutagen.mp3 import EasyMP3
                    audio = EasyMP3(file)
                    new_name = audio["title"]
                    new_artist = audio["artist"]
                    os.rename(file, re.sub('[^A-Za-z0-9]+', '', str(new_name)) + "_" +
                              re.sub('[^A-Za-z0-9]+', '', str(new_artist)) + ".mp3")
                except:
                    print("Bad Mp3", file)
    if file.lower().endswith(".flac"):
        try:
            from mutagen.flac import FLAC
            audio = FLAC(file)
            new_name = audio["title"]
            new_artist = audio["artist"]
            new_track_number = audio["tracknumber"]
            new_album = audio["album"]
            os.rename(file, re.sub('[^A-Za-z0-9]+', '', str(new_album)) + "_" +
                      re.sub('[^A-Za-z0-9]+', '', str(new_name)) + "_" +
                      re.sub('[^A-Za-z0-9]+', '', str(new_track_number)) + "_" +
                      re.sub('[^A-Za-z0-9]+', '', str(new_artist)) + ".flac")
        except:
            print("Bad Flac", file)
    if file.lower().endswith(".m4a"):
        try:
            from mutagen.mp4 import MP4
            audio = MP4(file)
            new_name = audio['\xa9nam']
            new_artist = audio['\xa9ART']
            new_track_number = audio["trkn"]
            new_album = audio['\xa9alb']
            os.rename(file, re.sub('[^A-Za-z0-9]+', '', str(new_album)) + "_" +
                      re.sub('[^A-Za-z0-9]+', '', str(new_name)) + "_" +
                      re.sub('[^A-Za-z0-9]+', '', str(new_track_number)) + "_" +
                      re.sub('[^A-Za-z0-9]+', '', str(new_artist)) + ".m4a")
        except:
            print("Bad m4a", file)

for dirname, dirnames, filenames in os.walk('.'):
    for subdirname in dirnames:
        check_file(os.path.join(dirname, subdirname))
    for filename in filenames:
        check_file(os.path.join(dirname, filename))