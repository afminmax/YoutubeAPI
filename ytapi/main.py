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

# S3-GET LIST OF CHANNELS & THEIR YOUTUBE UNIQUE ID's
# Currently read from handmade json list to get things started.
# Later, section 3 will get the list from either MongoDB or TinyDB
channelList = {}
with open('channels.json') as json_file:
    data = json.load(json_file)
    for channel in data:
        channelList.update({channel['channelName']: channel['channelId']})
print(channelList)


# S4-GET
for channel in data:
    print('Querying channel ' +
          channel['channelName'] + ' with channel ID of: ' + channel['channelId'])
    yt = ChannelStats(api_key, channel['channelId'])
    # print(yt)
    print(yt.get_channel_statistics())


# stop point - read the statistics, compare and update the json file.
