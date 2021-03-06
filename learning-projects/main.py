# REFERENCES:
# http://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html
##
# https://developers.google.com/youtube/v3/guides/implementation/search
##

# import the path module to traverse directories
from pathlib import Path
# load the build library
from googleapiclient.discovery import build
# import the youtube stats class
from youtube_statistics import YTstats
# import youtube_statistics

# load the api key from an ignored git directory - we're not posting this to git!
dataFolder = Path("X:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "gapi.txt"
with open(fileToOpen) as file:
    api_key = file.read()
# print(api_key)

# paste the interested channel id here.
# later - this will be fetched from a table in a database
# hardcoded to start
channel_id = 'UCbXgNpp0jedKWcQiULLbDTA'

yt = YTstats(api_key, channel_id)
yt.get_channel_statistics()

# the youtube api only allows for 50 items worth of videos per returned page
# we have to build further functionality to loop through all video result pages to get all the videos
yt.get_channel_video_data()

yt.dump()
