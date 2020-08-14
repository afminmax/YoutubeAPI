# Part 2 - Searching Channels

# import the path module to traverse directories
from pathlib import Path
# load the build library
from googleapiclient.discovery import build

# load the api key
dataFolder = Path("X:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "gapi.txt"
with open(fileToOpen) as file:
    apiKey = file.read()
print(apiKey)

# building the service
# service name: youtube
# add more tomorrow.
