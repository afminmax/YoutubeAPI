# Class for creating channel object

# this module is used to send and receive RESTful data
import requests

# import json module to handle returned JSON
import json

# progress bar
from tqdm import tqdm


class YTstats:
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None  # stores channel data as json
        self.video_data = None  # stores video data as json

    def get_channel_statistics(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        # print(url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        # print(data)
        try:
            data = data["items"][0]["statistics"]
        except:
            data = None

        self.channel_statistics = data
        return data

    def get_channel_video_data(self):
        # part 1 - get the video id's first
        channel_videos = self._get_channel_videos(limit=50)
        print('number of channel videos that are not playlists: ' +
              str(len(channel_videos)))
        # print(channel_videos)

        # part 2 - get the video statistics
        # youtube provides details about each video in three places, each of which must be collected via URL
        # the places are 1-snippet, 2-statistics, 3-content details
        parts = ['snippet', 'statistics', 'contentDetails']
        for video_id in tqdm(channel_videos):
            for part in parts:
                data = self._get_single_video_data(video_id, part)
                channel_videos[video_id].update(data)

        self.video_data = channel_videos
        return channel_videos

    # helper function to get video data
    def _get_single_video_data(self, video_id, part):
        url = f'https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}'
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0][part]
        except:
            print('error will robinson!')
            data = dict()
        return data

        self.video_data = channel_videos
        return channel_videos

    # helper function that builds the initial video search URL

    def _get_channel_videos(self, limit=None):
        url = f'https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=id&order=date'
        if limit is not None and isinstance(limit, int):
            url += '&maxResults=' + str(limit)
            # print('search url: ' + url)

        vid, npt = self._get_channel_videos_per_page(url)
        index = 0
        while(npt is not None and index < 10):
            nexturl = url + "&pageToken=" + npt
            next_vid, npt = self._get_channel_videos_per_page(nexturl)
            vid.update(next_vid)
            index += 1

        return vid

    # helper function that gets all the pages of videos and stores the video id's

    def _get_channel_videos_per_page(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_videos = dict()
        if 'items' not in data:
            return channel_videos, None

        item_data = data['items']
        nextPageToken = data.get('nextPageToken', None)
        for item in item_data:
            try:
                kind = item['id']['kind']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_videos[video_id] = dict()
            except KeyError:
                print('problem with the keys and/or data')
        return channel_videos, nextPageToken

# this function dumps the content of the channel into a json file

    def dump(self):
        if self.channel_statistics is None or self.video_data is None:
            print('data is none')
            return

        fused_data = {self.channel_id: {
            'channel_statistics': self.channel_statistics,
            "video_data": self.video_data}}

        channel_title = self.video_data.popitem()[1].get(
            'channelTitle', self.channel_id)
        channel_title = channel_title.replace(" ", "_",).lower()
        file_name = channel_title + '.json'
        with open(file_name, 'w') as f:
            json.dump(fused_data, f, indent=4)
        print('file dumped')
