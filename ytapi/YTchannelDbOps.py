# class that updates mongodb with channel values

# needs to have access to the channel collection and db as arguments.


class ChannelDbOps:

    def __init__(self, db, collection):
        self.db = db
        self.collection = collection

    # method to print the collected db and collection arguments from main (a test)
    def __str__(self):
        # print('something here')
        print(self.db)
        print(self.collection)
        # print('the passed in db is: ' + str(self.db))
        # print('the passed in collection is: ' + str(self.collection))
        print('\n')

    def updateChannelStat(self):
        pass
