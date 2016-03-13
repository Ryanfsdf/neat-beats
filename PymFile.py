#! python3

import os
import re


# TO DO - remove digit in track number for numbers larger than 2 digits
# - make a safety catch to leave song alone if the title is less than 4 characters
# - fix bad files not being put into 000 NO ALBUM SONGS

def check_file(file):
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


def organize_file(file):
    if file.lower().endswith(".mp3") | file.lower().endswith(".flac"):
        if file.lower().endswith(".mp3"):
            from mutagen.mp3 import EasyMP3
            audio = EasyMP3(file)

        if file.lower().endswith(".flac"):
            from mutagen.flac import FLAC
            audio = FLAC(file)

        try:
            new_artist = audio["artist"]
            new_album = audio["album"]
            try:
                os.makedirs(re.sub('[^A-Za-z0-9\s]+', '', str(new_artist)) + " - " +
                            re.sub('[^A-Za-z0-9\s]+', '', str(new_album)))
            except:
                pass
            os.rename(file, os.path.join((re.sub('[^A-Za-z0-9\s]+', '', str(new_artist)) + " - " +
                                          re.sub('[^A-Za-z0-9\s]+', '', str(new_album))), file))
        except:
            try:
                os.makedirs("000 NO ALBUM SONGS")
            except:
                pass
            try:
                os.rename(file, os.path.join("000 NO ALBUM SONGS", file))
            except:
                print("Could not move " + file)

    if file.lower().endswith(".m4a"):
        from mutagen.mp4 import MP4
        audio = MP4(file)

        try:
            new_artist = audio['\xa9ART']
            new_album = audio['\xa9alb']
            try:
                os.makedirs(re.sub('[^A-Za-z0-9\s]+', '', str(new_artist)) + " - " +
                            re.sub('[^A-Za-z0-9\s]+', '', str(new_album)))
            except:
                pass
            os.rename(file, os.path.join((re.sub('[^A-Za-z0-9\s]+', '', str(new_artist)) + " - " +
                                          re.sub('[^A-Za-z0-9\s]+', '', str(new_album))), file))
        except:
            try:
                os.makedirs("000 NO ALBUM SONGS")
            except:
                pass
            try:
                os.rename(file, os.path.join("000 NO ALBUM SONGS", file))
            except:
                print("Could not move " + file)


def type_input(runfunc):
    if runfunc == "run":
        if "yes" == input("Are you sure? Make sure you back up your files first (yes/no):"):
            for dirname, dirnames, filenames in os.walk('.'):
                for subdirname in dirnames:
                    check_file(os.path.join(dirname, subdirname))
                for filename in filenames:
                    check_file(os.path.join(dirname, filename))
            print("Successful")
            type_input(input("organize - Organize all music files into folders for "
                             "their corresponding album/artist name" + os.linesep +
                             "quit - exit the program" + os.linesep +
                             "Type your command:"))
        else:
            type_input(input("run - Collapse all folders and rename music files" + os.linesep +
                             "organize - Organize all music files into folders for "
                             "their corresponding album/artist name" + os.linesep +
                             "quit - exit the program" + os.linesep +
                             "Type your command:"))
    if runfunc == "organize":
        if "yes" == input("Are you sure? Make sure you back up your files first (yes/no):"):
            for dirname, dirnames, filenames in os.walk('.'):
                for subdirname in dirnames:
                    organize_file(os.path.join(dirname, subdirname))
                for filename in filenames:
                    organize_file(os.path.join(dirname, filename))
            print("Successful")
            type_input(input("run - Collapse all folders and rename music files" + os.linesep +
                             "quit - exit the program" + os.linesep +
                             "Type your command:"))
        else:
            type_input(input("run - Collapse all folders and rename music files" + os.linesep +
                             "organize - Organize all music files into folders for "
                             "their corresponding album/artist name" + os.linesep +
                             "quit - exit the program" + os.linesep +
                             "Type your command:"))
    elif runfunc == "quit":
        pass

    else:
        type_input(input("Invalid Command" + ''' " ''' + runfunc + ''' " :'''))


response = input("run - Collapse all folders and rename music files" + os.linesep +
                 "organize - Organize all music files into folders for "
                 "their corresponding album/artist name" + os.linesep +
                 "quit - exit the program" + os.linesep +
                 "Type your command:")
type_input(response)
