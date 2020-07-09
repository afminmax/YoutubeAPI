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

from connections import Connections


# S2-READING THE API KEY
dataFolder = Path("X:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "gapi.txt"
with open(fileToOpen) as file:
    api_key = file.read()
print('the youtube api key to be used is: ' + api_key)

# S3-GETTING THE DB INFO AND SETTING UP THE CONNECTION
fileToOpen = dataFolder / "dbc.txt"
with open(fileToOpen) as file:
    dbc_key = file.read()
myClient = MongoClient(dbc_key)
db = myClient['channelsDB']
collection = db['ytchannels']
print('the db key to be used is: ' + dbc_key)

print(type(db))
print(db)

print(type(collection))
print(collection)


# S4-Query each video direct from DB
# this method chosen over creating a separate list, because
# a seperate list may be deconstructed due to system/memory crash.
# if iterated across the db, failure can only happen in the record
# being processed.


for record in collection.find({}, {'_id': 1, 'ytcId': 1, 'displayName': 1, 'viewCount': 1}):
    print('Querying channel ' +
          record['displayName'] + ' with channel ID of: ' + record['ytcId'] + ' and system ID of: ' + str(record['_id']))
    yt = ChannelStats(api_key, record['ytcId'])
    # print(yt)
    channelStatistics = yt.get_channel_statistics()
    print(channelStatistics['viewCount'])

    # july 8 - end, already broken here - break is in mongo from stack dump

    yt.update_channel_statistics()

    print(channelStatistics)
    print()
    print('the view count for ' +
          record['displayName'] + ' is: ' + channelStatistics['viewCount'])
    if (int(channelStatistics['viewCount']) == record['viewCount']):
        print('viewcounts match')
    elif (int(channelStatistics['viewCount']) > record['viewCount']):
        print('the current view count is: ' +
              str(record['viewCount']) + '. The new view count is: ' + channelStatistics['viewCount'])

        collection.update_one({'_id': record['_id']}, {
                              '$set': {'viewCount': int(channelStatistics['viewCount'])}})
        print('the new updated view count is: ' +
              channelStatistics['viewCount'])
    # print()
    # yt.update_channel_statistics()


# *************************************************

# OLD QUERY METHOD
# # query the channel ids from mongodb into a temp dictionary (this will later have switches)
# channelList = []
# for item in collection.find({}, {"_id": 0, "ytcId": 1, 'displayName': 1}):
#     print(item)
#     channelList.append(item)
# channelList
# channelList[0]['ytcId']

# # query each video from list
# for channelName, channelId in channelList.items():
#     print('Querying channel ' +
#           channelName + ' with channel ID of: ' + channelId)
#     yt = ChannelStats(api_key, channelId)
#     # print(yt)
#     channelStatistics = yt.get_channel_statistics()
#     print(channelStatistics)
