# THIS FILE CREATES A TINYDB DB TO HOLD THE CHANNEL DATA

from tinydb import TinyDB, Query
db = TinyDB('ytchannels.json')


def insert():
    db.insert({
        'ytcId': 'UCYNbYGl89UUowy8oXkipC-Q',
        'displayName': 'Dr.Becky',
        'isActive': 'True',
        'tags': ['Astronomy', 'Astrophysics', 'Solar System', 'Backyard'],
        'theme': 'I am Dr Becky Smethurst, an astrophysicist at the University of Oxford. I love making videos about science with an unnatural level of enthusiasm. I like to focus on how we know things, not just what we know. And especially, the things we still do not know. If you have ever wondered about something in space and couldn not find an answer online - you can ask me!',
        'videoCount': 75,
        'newVideoCount': 0,
        'playlistCount': 0,
        'subscriberCount': 95000,
        'dateAdded': '2020-06-07',
        'dateRemoved': '',
        'lastUpdated': '', })


insert()

print(db.all())
len(db)

Channel = query()


def search():
    results = db.search()
