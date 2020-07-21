from pathlib import Path
import pymongo
from pymongo import MongoClient


dataFolder = Path("Z:/YoutubeAPI/keys/")


class Connections:

    def __init__(self):
        pass

    def getApiKey():
        pass

    def dbConnection(self):
        fileToOpen = dataFolder / "dbc.txt"
        with open(fileToOpen) as file:
            dbc_key = file.read()
        myClient = MongoClient(dbc_key)
        db = myClient['channelsDB']
        collection = db['ytchannels']
        return db, collection


newDbConn = Connections()

newDbConn.dbConnection()
