# here, create reference lookups to access various levels of the JSON channel document

import json

# dataFolder = Path("X:/Coding/YoutubeAPI/")
# fileToOpen = dataFolder / "channelsDb.json"
with open('channelsDb.json') as json_file:
    data = json.load(json_file)

print(type(data))

# elements have integeger key id's

# get the id of an element, in this case the first
data[0]['_id']

# get the youtube id of an element, in this case the first
data[0]['ytcId']

# get the activity status
data[0]['channelActive']

# get the channel counts, this has a sub-document aka array
data[0]['channelCounts']

# get the video count from the channel counts sub-document
data[0]['channelCounts']

