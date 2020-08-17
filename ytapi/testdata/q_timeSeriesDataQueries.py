import pymongo
from pymongo import MongoClient
import json
from pathlib import Path
import datetime


# MAKE MONGODB CONNECTION
dataFolder = Path("C:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "dbc.txt"
with open(fileToOpen) as file:
    dbc_key = file.read()
myClient = MongoClient(dbc_key)
db = myClient['channelsDB']
collection = db['ChannelTimeStats']
print('the db key to be used is: ' + dbc_key)
print(db)
print(collection)


# ---------------------------------------------------------------------------------
# 1-LOOK AT ALL ITEMS (SELECT *)
# outputs all data in json object

for record in collection.find():
    print(record)
    print('\n')

# ---------------------------------------------------------------------------------
# 2-LOOK AT THE FIRST ITEM (SELECT (*) TOP 1)
# outputs all data in json object

print(collection.find_one())

# ---------------------------------------------------------------------------------
# 3-GET THE VIEWCOUNTS OF A SPECIFIC CHANNEL
# get the id of one channel, in this case the first which is the zeroth item...

# by sub-docs
collection.find_one({}, {'ytcId': 'abc123', 'viewCount': 1})

# by array
collection.find_one({}, {'ytcId': 'def456', 'viewCount': 1})
