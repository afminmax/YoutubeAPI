# class that updates mongodb with channel values

# needs to have access to the channel collection and db as arguments.


class ChannelDbOps:

    def __init__(self, db, collection):
        self.db = db
        self.collection = collection
        self.dbChannelId = 0

    # method to print the collected db and collection arguments from main (a test)
    def __str__(self):
        # print('something here')
        print(self.db)
        print(self.collection)
        # print('the passed in db is: ' + str(self.db))
        # print('the passed in collection is: ' + str(self.collection))
        print('\n')

    # this is a test function, it does a query to check if the db and collection objects are being passed properly
    # and the mongodb is able to be queried. the result is a dictionary.

    def peek(self, dbChannelId):
        return self.collection.find_one({'_id': dbChannelId}, {'ytcId': 1, 'displayName': 1, 'channelCounts.viewCount': 1})

    # this is a test function to see if the db and collection objects can make a change to a value in the mongodb
    def update(self, x):
        collection.update_one({'_id': dbChannelId}, {
                              '$set': {"displayName": "ElderFox Documentaries"}})
