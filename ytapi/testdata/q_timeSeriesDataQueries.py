import pymongo
from pymongo import MongoClient
import json
from pathlib import Path
import datetime
import pandas as pd


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

# IMPORTANT MONGO FIND NOTE
# FIND - will give you ALL matching documents to a query
#        if you have multiple items that may fit a query, use this.
#        example - similar to the WHERE clause in sql

# FINDONE - will only give you the FIRST matching document to a query.
#           be sure you really need only one unique item when using.

# ---------------------------------------------------------------------------------
# 1-LOOK AT ALL ITEMS (SELECT *)
# outputs all data in channel timeseries document

for record in collection.find():
    print(record)
    print('\n')

# ---------------------------------------------------------------------------------
# 2-GET THE VIEWCOUNTS OF A SPECIFIC CHANNEL
# get the viewCounts of a channel
# put in the sub-doc if needed for another query (ex: sub-counts)

# by sub-docs
# verbose with ytcid for check
collection.find_one({'ytcId': 'abc123'}, {'ytcId': 1, 'viewCount': 1})
# specific for pandas with object id removed
collection.find_one({'ytcId': 'abc123'}, {'_id': 0, 'viewCount': 1})


# by array
collection.find_one({'ytcId': 'def456'}, {'ytcId': 1, 'viewCount': 1})
collection.find_one({'ytcId': 'abc123'}, {'_id': 0, 'viewCount': 1})

# ---------------------------------------------------------------------------------
# 3-PUT THE VIEWCOUNTS INTO A PYTHON DICTIONARY
# note that the python dictionary get() method extracts only the values
viewCount_dict = collection.find_one(
    {'ytcId': 'abc123'}, {'_id': 0, 'viewCount': 1}).get('viewCount')
print(viewCount_dict)
