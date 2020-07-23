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

# S4-QUERY YOUTUBE FOR THE STATISTICS OF EACH CHANNEL IN THE DATABASE

startTS = datetime.datetime.now()
for record in collection.find({}, {'_id': 1, 'ytcId': 1, 'displayName': 1, 'channelCounts.viewCount': 1}):
    dbChannelId = record['_id']
    dbYtChannelId = record['ytcId']
    dbChannelDisplayName = record['displayName']
    dbChannelViewCount = record['channelCounts'][0].get('viewCount')

    print('Querying channel ' +
          dbChannelDisplayName + ' with YT channel ID of: ' + dbYtChannelId + ' and system ID of: ' + str(dbChannelId) +
          ', with a view count of: ' + str(dbChannelViewCount))

    ytChannelFetch = ChannelStats(api_key, record['ytcId'])
    fetchedChannelStatistics = ytChannelFetch.get_channel_statistics()
    ytViewCount = int(fetchedChannelStatistics['viewCount'])
    print(ytViewCount)
    print('\n')

    if (ytViewCount == dbChannelViewCount):
        print('viewcounts match')
    elif (ytViewCount > dbChannelViewCount):
        print('Viewcounts do not match and update to be done. The current db view count is: ' +
              str(dbChannelViewCount) + '. The new live view count from YT is: ' + str(ytViewCount))

        collection.update_one({'_id': dbChannelId}, {
                              '$set': {'channelCounts.0.viewCount': ytViewCount}})
        updatedDbChannelViewCount = collection.find_one({'_id': dbChannelId}, {
                                                        'channelCounts.viewCount': 1}).get('channelCounts')[0]['viewCount']
        print('the new updated db view count is: ' +
              str(updatedDbChannelViewCount))
    print('\n')

endTS = datetime.datetime.now()
elapsedTime = endTS - startTS
print(elapsedTime)
