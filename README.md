# NeatBeats

NeatBeats renames all the music files in a folder to the actual title of the song from its metadata and organizes them
into folders neatly named by their album names. 
Extremely helpful for organizing a lot of music files downloaded from the internet, which often have obscure file names. 
This program essentially extracts the actual title/album/artist/tracknumber from a song and incorporates it into the actual file/folder name.
Works by using Mutagen 1.3.1 to extract the metadata and also regex to standardize all the file names

HOW TO USE:
Place a music folder in the file directory as neatbeats.py and execute the python file. This will give you a list of commands of what you would like to do. Type in your commands and let it do the rest!

UPCOMING:
  * include support for more music files (Currently supports m4a, mp3, flac)
  * make it more user friendly (a GUI once I learn how to use Tkinter)
  * more options such as organizing by artist name, etc.


~NeatBeats turns this~
![Alt text](https://github.com/Ryanfsdf/NeatBeats/blob/master/Sample1.png "")

~Into this~
![Alt text](https://github.com/Ryanfsdf/NeatBeats/blob/master/Sample2.png "")


This is done by extracting the metadata from an audio file. This is particularily useful since a lot of songs downloaded
from the internet tend to have inconsistent conventions for naming the files, whereas the metadata is generally the same
regardless of where the song is downloaded from.
