# MAIN.PY
# This is an application that collects popular youtube learning channels and displays and makes recommendations

# S1-IMPORTS
from YTchannelStats import ChannelStats
from pathlib import Path
from googleapiclient.discovery import build
import json

# S2-READING THE API KEY
dataFolder = Path("X:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "gapi.txt"
with open(fileToOpen) as file:
    api_key = file.read()
print('the api key to be used is: ' + api_key)

# S3-TEST CHANNEL DATA
# Youtube channels have unique Id's, this small list is used for initial testing
# Later, section 3 will be generalized for use with either MongoDB or TinyDB

with open('channels.json') as json_file:
    data = json.load(json_file)
    for channel in data:
        print('Querying channel ' +
              channel['channelName'] + ' with channel ID of: ' + channel['channelId'])
        yt = ChannelStats(api_key, channel['channelId'])
        # print(yt)
        print(yt.get_channel_statistics())


# stop point - read the statistics, compare and update the json file.
