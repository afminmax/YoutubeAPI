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


print(type(data))
# elements have integeger key id's

# get the id of an element, in this case the first which is the zeroth item...
data[0]['_id']

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
