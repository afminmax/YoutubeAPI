# MAIN.PY
# This is an application that collects popular youtube learning channels and displays and makes recommendations

# S1-IMPORTS
from YTchannelStats import ChannelStats
from pathlib import Path
from googleapiclient.discovery import build
import json
from tinydb import TinyDB, Query

# S2-READING THE API KEY
dataFolder = Path("X:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "gapi.txt"
with open(fileToOpen) as file:
    api_key = file.read()
print('the api key to be used is: ' + api_key)

# S3 GET LIST OF CHANNELS & THEIR UNIQUE YOUTUBE ID's
# Currently read from handmade json list to get things started.
# Later, section 3 will get the list from either MongoDB or TinyDB
# channelList = {}   # dictionary to hold channel name & id for querying
# with open('channels.json') as json_file:
#     data = json.load(json_file)
#     for channel in data:
#         channelList.update({channel['channelName']: channel['channelId']})
# print(channelList)


# build query here:
# get the ytcId and displayName for each document
Channel = Query()
db.search(Channel.ytcId)

# S4-GET THE CURRENT CHANNEL VIDEO AND SUBSCRIBER COUNTS
for channelName, channelId in channelList.items():
    print('Querying channel ' +
          channelName + ' with channel ID of: ' + channelId)
    yt = ChannelStats(api_key, channelId)
    # print(yt)
    channelStatistics = yt.get_channel_statistics()
    print(channelStatistics)


# stop point - install mongodb
# stop point - read the statistics, compare and update the json file.
