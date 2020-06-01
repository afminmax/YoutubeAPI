# Part 1 - Project Setup

##
# http://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html
##
# https://developers.google.com/youtube/v3/guides/implementation/search
##

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

# building the service object
# need three things minimum: (1)api service name, (2)version, (3) apikey
youtube = build('youtube', 'v3', developerKey=apiKey)

request = youtube.channels().list(
    part='statistics',
    forUsername='schafer5'
)

response = request.execute()
response
