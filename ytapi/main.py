# MAIN.PY
# This is an application that collects popular youtube learning channels and displays and makes recommendations

# S1-IMPORTS
from YTchannelStats import ChannelStats
from pathlib import Path
from googleapiclient.discovery import build
import json
import dns.resolver  # this is in fact the dns python package
import pymongo
import datetime
from pymongo import MongoClient
from connections import Connections


# S2-READING THE API KEY
dataFolder = Path("Z:/YoutubeAPI/keys/")
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

# S4-Query each video direct from DB
# this method chosen over creating a separate list, because
# a seperate list may be deconstructed due to system/memory crash.
# if iterated across the db, failure can only happen in the record
# being processed.

startTS1 = datetime.datetime.now()
for record in collection.find({}, {'_id': 1, 'ytcId': 1, 'displayName': 1, 'channelCounts.viewCount': 1}):
    print('Querying channel ' +
          record['displayName'] + ' with channel ID of: ' + record['ytcId'] + ' and system ID of: ' + str(record['_id']) +
          ', with a view count of: ' + str(record['channelCounts'][0].get('viewCount')))

    yt = ChannelStats(api_key, record['ytcId'])
    channelStatistics = yt.get_channel_statistics()
    # print(channelStatistics)
    ytViewCount = int(channelStatistics['viewCount'])
    print(ytViewCount)
    print('\n')

    if (int(channelStatistics["viewCount"]) == record['channelCounts'][0].get('viewCount')):
        print('viewcounts match')
    elif (int(channelStatistics['viewCount']) > record['channelCounts'][0].get('viewCount')):
        print('Viewcounts do not match and update to be done. The current db view count is: ' +
              str(record['channelCounts'][0].get('viewCount')) + '. The new view count is: ' + channelStatistics['viewCount'])

        collection.update_one({'_id': record['_id']}, {
                              '$set': {'channelCounts.0.viewCount': int(channelStatistics['viewCount'])}})
        print('the new updated view count is: ' +
              channelStatistics['viewCount'])
    print('\n')

endTS1 = datetime.datetime.now()
elapsedTime1 = endTS1 - startTS1
print(elapsedTime)

# ****************************************************************************************************************************#

startTS2 = datetime.datetime.now()
for record in collection.find({}, {'_id': 1, 'ytcId': 1, 'displayName': 1, 'channelCounts.viewCount': 1}):
    dbChannelId = record['_id']
    dbYtChannelId = record['ytcId']
    dbChannelDisplayName = record['displayName']
    dbChannelViewCount = record['channelCounts'][0].get('viewCount')

    print('Querying channel ' +
          dbChannelDisplayName + ' with YT channel ID of: ' + dbYtChannelId + ' and system ID of: ' + str(dbChannelId) +
          ', with a view count of: ' + str(dbChannelViewCount))

    yt = ChannelStats(api_key, record['ytcId'])
    channelStatistics = yt.get_channel_statistics()
    # print(channelStatistics)

    ytViewCount = int(channelStatistics['viewCount'])
    print(ytViewCount)
    print('\n')

    if (ytViewCount == dbChannelViewCount):
        print('viewcounts match')
    elif (ytViewCount > dbChannelViewCount):
        print('Viewcounts do not match and update to be done. The current db view count is: ' +
              str(dbChannelViewCount) + '. The new view count is: ' + str(ytViewCount))

        collection.update_one({'_id': dbChannelId}, {
                              '$set': {'channelCounts.0.viewCount': ytViewCount}})
        print('the new updated view count is: ' + ytViewCount)
    print('\n')

endTS2 = datetime.datetime.now()
elapsedTime2 = endTS2 - startTS2
print(elapsedTime2)
