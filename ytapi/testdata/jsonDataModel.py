# here, create reference lookups to access various levels of the JSON channel document
# added equivalent mongodb reference db lookup as well
# https://docs.mongodb.com/manual/tutorial/query-documents/

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

print(type(collection.find_one({}, {'_id': 1})))

# to get ONLY the specific key id, this works because the return
# from mongodb is a dictionary
collection.find_one({}, {'_id': 1}).get('_id')

# ---------------------------------------------------------------------------------
# 4-GET THE ID OF ALL CHANNELS
# json
for record in jsonFileData:
    print(jsonFileData[record]['_id'])

# mongodb
for record in collection.find({}, {'_id': 1}):
    print(record)
    print('\n')

# or to get the id's only:
for record in collection.find({}, {'_id': 1}):
    print(record.get('_id'))
    print('\n')

# ---------------------------------------------------------------------------------
# 5-GET THE YOUTUBE ID OF ALL CHANNELS
# json
for record in jsonFileData:
    print(jsonFileData[record]['ytcId'])

# mongodb
for record in collection.find({}, {'_id': 1, 'ytcId': 1}):
    print(record.get('ytcId'))
    print('\n')

# ---------------------------------------------------------------------------------
# 6-GET THE YOUTUBE ID & CHANNEL NAME OF ALL CHANNELS
# json
for record in jsonFileData:
    print(jsonFileData[record]['ytcId'] + ' ' +
          jsonFileData[record]['displayName'])

# mongodb
for record in collection.find({}, {'_id': 1, 'ytcId': 1, 'displayName': 1}):
    print(record.get('ytcId') + ' ' + record.get('displayName'))
    print('\n')

# ---------------------------------------------------------------------------------
# 7-GET THE YOUTUBE ID & VIEW COUNT OF A SINGLE CHANNEL
# Traverse into a channel array
# json
jsonFileData['ElderFox Documentaries']['channelCounts'][0]['viewCount']

# mongodb
# hint - must use dot notation to get to sub-docs and a specific sub-key
collection.find_one({}, {'ytcId': 1, 'channelCounts.viewCount': 1})

# mongodb - set equal to a variable and parse each item in the dictionary
result_a = collection.find_one({}, {'ytcId': 1, 'channelCounts.viewCount': 1})
result_a.get('ytcId')
result_a.get('channelCounts')
result_a['channelCounts'][0]['viewCount']
result_a['channelCounts'][0].get('viewCount')


# ---------------------------------------------------------------------------------
# 8-GET THE YOUTUBE ID & VIEW COUNT OF MULTIPLE CHANNELS
# Traverse into a channel array
# json
for record in jsonFileData:
    print(str(jsonFileData[record]['ytcId'] + ' ' +
              str(jsonFileData[record]['channelCounts'][0]['viewCount'])))

# mongodb
# hint - must use dot notation to get to sub-docs
for record in collection.find({}, {'ytcId': 1, 'channelCounts.viewCount': 1}):
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

# ---------------------------------------------------------------------------------
# 10-MONGODB SPECIFIC QUERIES:
# find a specific channel id by mongodb id:
collection.find_one({'_id': 3})

# find a specific channel by youtube id:
collection.find_one({'ytcId': 'UCNqNkZ7kKfqimqHkgbWMNYA'})

# find a specific channel by channel display name:
collection.find_one({'displayName': 'Launch Pad Astronomy'})

# find a specific channel using a like term:
# see documentation for regex formulas
some_results = collection.find({'displayName': {'$regex': 'Bec'}})
for x in some_results:
    print(x)
