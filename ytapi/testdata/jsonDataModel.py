# here, create reference lookups to access various levels of the JSON channel document
# added equivalent mongodb reference db lookup as well
# would be nice to have

import pymongo
from pymongo import MongoClient
import json
from pathlib import Path

# MAKE LOCAL JSON CONNECTION
with open('mdb-channel-document.json') as json_file:
    jsonFileData = json.load(json_file)
print(jsonFileData)
print(type(jsonFileData))

# MAKE MONGODB CONNECTION
dataFolder = Path("X:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "dbc.txt"
with open(fileToOpen) as file:
    dbc_key = file.read()
myClient = MongoClient(dbc_key)
db = myClient['channelsDB']
collection = db['ytchannels']
print('the db key to be used is: ' + dbc_key)
print(db)
print(collection)

# ---------------------------------------------------------------------------------
# 1-LOOK AT ALL ITEMS (SELECT *)
# outputs all data in json object
# json
for record in jsonFileData:
    print(jsonFileData[record])
    print('\n')

# mongodb
for record in collection.find():
    print(record)
    print('\n')

# ---------------------------------------------------------------------------------
# 2-LOOK AT THE FIRST ITEM (SELECT (*) TOP 1)
# outputs all data in json object
# json - this is known by looking at the data. how to get first ordinal?? TBD
jsonFileData["ElderFox Documentaries"]

# mongodb
print(collection.find_one())

# ---------------------------------------------------------------------------------
# 3-GET THE ID OF A SINGLE CHANNEL
# get the id of one channel, in this case the first which is the zeroth item...
# json
jsonFileData['ElderFox Documentaries']['_id']

# mongodb
# The second parameter of the find() method is an object describing which fields to
# include in the result. Using find_one() gets the first channel.
collection.find_one({}, {'_id': 1})

# ---------------------------------------------------------------------------------
# 4-GET THE ID OF ALL CHANNELS
# json
for record in jsonFileData:
    print(jsonFileData[record]['_id'])

# mongodb
for record in collection.find({}, {'_id': 1}):
    print(record)
    print('\n')

# ---------------------------------------------------------------------------------
# 5-GET THE YOUTUBE ID OF ALL CHANNELS
# json
for record in jsonFileData:
    print(jsonFileData[record]['ytcId'])

# mongodb
for record in collection.find({}, {'_id': 1, 'ytcId': 1}):
    print(record)
    print('\n')

# ---------------------------------------------------------------------------------
# 6-GET THE YOUTUBE ID & CHANNEL NAME OF ALL CHANNELS
# json
for record in jsonFileData:
    print(jsonFileData[record]['ytcId'] + ' ' +
          jsonFileData[record]['displayName'])

# mongodb
for record in collection.find({}, {'_id': 1, 'ytcId': 1, 'displayName': 1}):
    print(record)
    print('\n')

# ---------------------------------------------------------------------------------
# 7-GET THE YOUTUBE ID & VIEW COUNT OF A SINGLE CHANNEL
# Traverse into a channel array
# json
jsonFileData['ElderFox Documentaries']['channelCounts'][0]['viewCount']

# mongodb
# hint - must use dot notation to get to sub-docs
collection.find_one({}, {'channelCounts.viewCount': 1})

# ---------------------------------------------------------------------------------
# 8-GET THE YOUTUBE ID & VIEW COUNT OF MULTIPLE CHANNELS
# Traverse into a channel array
# json
for record in jsonFileData:
    print(jsonFileData[record]['channelCounts'][0]['viewCount'])

# mongodb
# hint - must use dot notation to get to sub-docs
for record in collection.find({}, {'channelCounts.viewCount': 1}):
    print(record)

# ---------------------------------------------------------------------------------
# 9-COMPARE VALUES FROM JSON TO MONGODB
# comparing by variable comparison
x = jsonFileData['ElderFox Documentaries']['_id']
y = collection.find_one({}, {'_id': 1})
y.get('_id')
if x == y.get('_id'):
    print('they are equal')
else:
    print('they are not equal')

# comparing by raw operations
# note, that to access the value in the returned value from the mongodb query,
# we have to use the dictionary get() method to specify the actual key, in this case '_id'
if jsonFileData['ElderFox Documentaries']['_id'] == collection.find_one({}, {'_id': 1}).get('_id'):
    print('they are equal')
else:
    print('they are not equal')


# ---------------------------- OLD STUFF BELOW --------------------------------
# mongodb
# GET THE YOUTUBE ID & VIEW COUNT OF A SINGLE CHANNEL
# json
# mongodb
# GET THE YOUTUBE ID & VIEW COUNT OF A SINGLE CHANNEL
# json
# mongodb
# GET THE YOUTUBE ID & VIEW COUNT OF A SINGLE CHANNEL
# json
# mongodb
# get the youtube id of an element, in this case the first
data[0]['ytcId']

# get the activity status
data[0]['channelActive']

# get all the channel counts, this has a sub-document aka array
data[0]['channelCounts']

# get the video count from the channel counts sub-document
data[0]['channelCounts'][0]['dts']
data[0]['channelCounts'][0]['videoCount']
data[0]['channelCounts'][0]['playlistCount']
data[0]['channelCounts'][0]['subscriberCount']
data[0]['channelCounts'][0]['viewCount']

# get all of the tags
data[0]['tags']

# get any one tag (the zeroeth tag in this case)
data[0]['tags'][0]

# get the video id sub-document {note-it is not done yet}
data[0]['videoIds']

# get the playlist id sub-document {note-it is not done yet}
data[0]['playlistIds']

# get all the social links
data[0]['socialLinks']

# get any one social link
data[0]['socialLinks'][0]['email']
data[0]['socialLinks'][0]['twitter']
data[0]['socialLinks'][0]['facebook']
data[0]['socialLinks'][0]['instagram']
data[0]['socialLinks'][0]['twitch']
data[0]['socialLinks'][0]['wechat']
data[0]['socialLinks'][0]['discord']

# get any web urls
data[0]['webLinks'][0]['channelAffiliatedSite']

# get any alternate youtube channel id's
data[0]['altYtChannels']

# get the description
data[0]['ytDescription']

# get the date the site was added to the database
data[0]['dateAdded']

# get the date the site was paused from displaying in the video wall
data[0]['datePaused']

# get the date the site was removed from the video wall {note: need to make an audit log}
data[0]['dateRemoved']

# get the date of the last statistics and video update from Youtube
data[0]['lastUpdated']
