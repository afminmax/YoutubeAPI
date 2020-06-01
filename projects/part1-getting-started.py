# hello, thus begins a new python adventure

# import the path module to traverse directories
from pathlib import Path
# load the build library
from apiclient.discovery import build

# load the api key
dataFolder = Path("X:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "gapi.txt"
with open(fileToOpen) as file:
    apikey = file.read()
print(key)

youtube = build('youtube', 'v3', developerKey=apikey)
