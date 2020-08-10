# MAIN.PY
# This is an application that collects popular youtube learning channels and displays and makes recommendations

# S1-IMPORTS
# Project classes:
from YTchannelStats import ChannelStats
from YTchannelDbOps import ChannelDbOps
# External/Python classes
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
    dbc_key = file.read()x1
myClient = MongoClient(dbc_key)
db = myClient['channelsDB']
collection = db['ChannelMetadata']
print('the db key to be used is: ' + dbc_key)


# S4-QUERY YOUTUBE FOR THE STATISTICS OF EACH CHANNEL IN THE DATABASE

startTS = datetime.datetime.now()
for record in collection.find({}, {'_id': 1, 'ytcId': 1, 'displayName': 1,
                                   'channelCounts.viewCount': 1,
                                   'channelCounts.commentCount': 1,
                                   'channelCounts.subscriberCount': 1,
                                   'channelCounts.videoCount': 1, }):

    # parse collection dictionaries and set various dabatase counts to
    # variables to make for easier reading and updating
    dbChannelId = record['_id']
    dbYtChannelId = record['ytcId']
    dbChannelDisplayName = record['displayName']
    dbChannelViewCount = record['channelCounts'][0].get('viewCount')
    dbChannelCommentCount = record['channelCounts'][0].get('commentCount')
    dbChannelSubscriberCount = record['channelCounts'][0].get(
        'subscriberCount')
    dbChannelVideoCount = record['channelCounts'][0].get('videoCount')

    # optional - brief status message, later set to logging
    print('Querying channel ' +
          dbChannelDisplayName + ' with YT channel ID of: ' + dbYtChannelId + ' and system ID of: ' + str(dbChannelId) +
          ', with a view count of: ' + str(dbChannelViewCount))

    # instantiate a channel object for the channel - calls class "ChannelStats"
    ytChannelFetch = ChannelStats(api_key, record['ytcId'])
    # save the returned fresh Youtube channel data to a dictionary
    fetchedChannelStatistics = ytChannelFetch.get_channel_statistics()
    # parse the fresh Youtube channel data to variables for easier reading and updating
    ytViewCount = int(fetchedChannelStatistics['viewCount'])
    ytCommentCount = int(fetchedChannelStatistics['commentCount'])
    ytSubscriberCount = int(fetchedChannelStatistics['subscriberCount'])
    ytVideoCount = int(fetchedChannelStatistics['videoCount'])

    print('yt view Count: ' + str(ytViewCount) +
          ' || db view count: ' + str(dbChannelViewCount))
    print('yt comment Count: ' + str(ytViewCount) +
          ' || db comment count: ' + str(dbChannelCommentCount))
    print('yt subscriber Count: ' + str(ytViewCount) +
          ' || db subscriber count: ' + str(dbChannelSubscriberCount))
    print('yt view Count: ' + str(ytVideoCount) +
          ' || db video count: ' + str(dbChannelVideoCount))
    print('\n')

    # pass db and collection to the class ChannelDbOps and print the objects to test they are passed
    # ChannelDbOps(db, collection).__str__()

    # create an instance of the dbOps object
    cdops = ChannelDbOps(db, collection)
    # cdops.__str__()

    valyew = cdops.peek(dbChannelId)
    print(valyew)
    x = 727
    cdops.update(dbChannelId, x)

    valx = cdops.peek(dbChannelId)
    print(valx)

endTS = datetime.datetime.now()
elapsedTime = endTS - startTS
print(elapsedTime)

# if (ytViewCount == dbChannelViewCount):
#     print('viewcounts match')
# elif (ytViewCount > dbChannelViewCount):
#     print('Viewcounts do not match and update to be done. The current db view count is: ' +
#           str(dbChannelViewCount) + '. The new live view count from YT is: ' + str(ytViewCount))

#     collection.update_one({'_id': dbChannelId}, {
#                           '$set': {'channelCounts.0.viewCount': ytViewCount}})
#     updatedDbChannelViewCount = collection.find_one({'_id': dbChannelId}, {
#                                                     'channelCounts.viewCount': 1}).get('channelCounts')[0]['viewCount']
#     print('the new updated db view count is: ' +
#           str(updatedDbChannelViewCount))

#     collection.update_one(
#         {'_id': 3}, {'$set': {'channelCounts.0.lastUpdate': datetime.datetime.utcnow()}})

#     collection.update_one(
#         {'_id': 3}, {'$set': {'lastUpdate': datetime.datetime.utcnow()}})

# print('\n')
