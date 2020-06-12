# MAIN.PY
# This is an application that collects popular youtube learning channels and displays and makes recommendations

# S1-IMPORTS
from YTchannelStats import ChannelStats
from pathlib import Path
from googleapiclient.discovery import build
import json
import dns.resolver  # this is in fact the dnspython package
import pymongo
from pymongo import MongoClient


# S2-READING THE API KEY
dataFolder = Path("X:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "gapi.txt"
with open(fileToOpen) as file:
    api_key = file.read()
# print('the api key to be used is: ' + api_key)

# S3-GETTING THE DB INFO AND SETTING UP THE CONNECTION
fileToOpen = dataFolder / "dbc.txt"
with open(fileToOpen) as file:
    dbc_key = file.read()
myClient = MongoClient(dbc_key)
db = myClient['channelsDB']
collection = db['ytchannels']
# print('the db key to be used is: ' + dbc_key)


# S3 GET LIST OF CHANNELS & THEIR UNIQUE YOUTUBE ID's
# Currently read from handmade json list to get things started.
# Later, section 3 will get the list from either MongoDB or TinyDB
# channelList = {}   # dictionary to hold channel name & id for querying
# with open('channels.json') as json_file:
#     data = json.load(json_file)
#     for channel in data:
#         channelList.update({channel['channelName']: channel['channelId']})
# print(channelList)

# query the channel ids from mongodb into a temp dictionary (this will later have switches)
channelList = []
for item in collection.find({}, {"_id": 0, "ytcId": 1, 'displayName': 1}):
    print(item)
    channelList.append(item)
channelList
channelList[0]['ytcId']


# query each video
for record in channelList:
    print('Querying channel ' +
          record['displayName'] + ' with channel ID of: ' + record['ytcId'])

    yt = ChannelStats(api_key, record['ytcId'])
    # print(yt)
    channelStatistics = yt.get_channel_statistics()
    print(channelStatistics)


# get statistics
# update the channels statistics in the database


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
