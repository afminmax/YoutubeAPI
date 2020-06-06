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

# load the api key from an ignored git directory - we're not posting this to git!
dataFolder = Path("X:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "gapi.txt"
with open(fileToOpen) as file:
    api_Key = file.read()
print(api_Key)

# paste the interested channel id here.
# later - this will be fetched from a table in a database
channel_id = 'UCZw_mKFPJMpvIWKWWwWpuVA/videos'

yt = YTstats(apikey)
