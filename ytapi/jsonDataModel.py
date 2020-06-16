# here, create reference lookups to access various levels of the JSON channel document

import json

# dataFolder = Path("X:/Coding/YoutubeAPI/")
# fileToOpen = dataFolder / "channelsDb.json"
with open('channelsDb.json') as json_file:
    data = json.load(json_file)

data
