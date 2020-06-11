# MONGODB FIRST TESTS

from pathlib import Path
import json
import dns.resolver  # this is in fact the dnspython package
import pymongo
from pymongo import MongoClient

# Bad ass SO reference with standard SQL
# https://stackoverflow.com/questions/25589113/how-to-select-a-single-field-for-all-documents-in-a-mongodb-collection


# S1-GETTING THE DB INFO AND SETTING UP THE CONNECTION
fileToOpen = dataFolder / "dbc.txt"
with open(fileToOpen) as file:
    dbc_key = file.read()
myClient = MongoClient(dbc_key)
db = myClient['channelsDB']
collection = db['ytchannels']
# print('the db key to be used is: ' + dbc_key)

# print the list of db's in the mongo cluster
print(myClient.list_database_names())

# get all items in the collection
c = collection.find_one()
print(c)

# get specific fields (no sub-docs)
# specify the fieldname and then put a "1" to return. "0" to not return.
for x in collection.find({}, {"ytcId": 1, 'displayName': 1, 'tags': 1}):
    print(x)


# put found data into a list, returns a list with two dictionaries
# the id field is always in by default and must be forcibly excluded.
someList = []

for x in collection.find({}, {"_id": 0, "ytcId": 1, 'displayName': 1}):
    someList.append(x)
print(someList)
