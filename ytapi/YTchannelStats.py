# This class gets a channels stats
# It may get video information later - or it may be made a separate class


import requests
import json
from tqdm import tqdm


class ChannelStats:

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None

    def update_channel_statistics(self):
        print('boo')

    def get_channel_statistics(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        print('the url to send is: ' + url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data["items"][0]["statistics"]
        except:
            data = None
        # print(data)
        self.channel_statistics = data
        return data


# yada on line 29 = print(data["items"][0]["statistics"])

# bb = ChannelStats('12345', 2)

# bb.update_channel_statistics()


# url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCaE309xZTS4XdecZSoaYzFg&key=AIzaSyDeY-I6kx427L6grhfdsONFbKd8NpKzLNQ'
# print('the url to send is: ' + url)
# json_url = requests.get(url)
# data = json.loads(json_url.text)
# try:
#     data = data["items"][0]["statistics"]
# except:
#     data = None

# print(data)

# print(data["items"][0]["statistics"])
# print(data)
# self.channel_statistics = data
# return data
