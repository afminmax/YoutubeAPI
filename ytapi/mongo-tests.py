# MONGODB FIRST TESTS

from pathlib import Path
import json
import dns.resolver  # this is in fact the dnspython package
import pymongo
from pymongo import MongoClient

# Bad ass SO reference with standard SQL
# https://stackoverflow.com/questions/25589113/how-to-select-a-single-field-for-all-documents-in-a-mongodb-collection


# S1-GETTING THE DB INFO AND SETTING UP THE CONNECTION
dataFolder = Path("X:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "dbc.txt"
with open(fileToOpen) as file:
    dbc_key = file.read()
myClient = MongoClient(dbc_key)
db = myClient['channelsDB']
collection = db['ytchannels']
# print('the db key to be used is: ' + dbc_key)

# print the list of db's in the mongo cluster
print(myClient.list_database_names())

# S2-SQL to MONGODB EQUIVOCATIONS

# S2.1-SELECT ALL RECORDS
# get all items in the collection =
# SELECT * FROM tablename
for x in collection.find({}):
    print(x)

x = collection.find({})
for item in x:
    print(item)

# S2.2-SELECT ALL VALUES FOR A SINGLE RECORD
# SELECT * FROM tablename WHERE a column = 'some value'
j = collection.find_one({'_id': 1})
print(j)

k = collection.find_one({'videoCount': 50})
print(k)

# S2.3-SELECT SPECIFIC VALUES FOR A SINGLE RECORD
# SELECT columnA, columnB, columnC FROM tablename WHERE a column = 'some value'
l = collection.find_one({'videoCount': 50}, {
                        "ytcId": 1, 'displayName': 1, 'tags': 1})
print(l)

# S2.4-SELECT SPECIFIC VALUES FOR MUTLTIPLE RECORDS
# SELECT columnA, columnB, columnC FROM tablename WHERE a column = 'some value'
for x in collection.find({}, {"ytcId": 1, 'displayName': 1, 'tags': 1}):
    print(x)

# S2.5-SELECT SPECIFIC VALUES AND PLACE INTO A LIST
# put found data into a list, returns a list with two dictionaries
# the id field is always in by default and must be forcibly excluded.
someList = []
for x in collection.find({}, {"_id": 0, "ytcId": 1, 'displayName': 1}):
    someList.append(x)
print(someList)
