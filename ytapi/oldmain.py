# HERE LIES VERBOSE CODE FROM MAIN THAT HAS BEEN REFACTORED FOR READABILITY

# -------- mongodb verbose for each ---------------------------------------------------------------------------------------
# refactored July 22, 2020
for record in collection.find({}, {'_id': 1, 'ytcId': 1, 'displayName': 1, 'channelCounts.viewCount': 1}):
    print('Querying channel ' +
          record['displayName'] + ' with channel ID of: ' + record['ytcId'] + ' and system ID of: ' + str(record['_id']) +
          ', with a view count of: ' + str(record['channelCounts'][0].get('viewCount')))

    yt = ChannelStats(api_key, record['ytcId'])
    channelStatistics = yt.get_channel_statistics()
    # print(channelStatistics)
    ytViewCount = int(channelStatistics['viewCount'])
    print(ytViewCount)
    print('\n')

    if (int(channelStatistics["viewCount"]) == record['channelCounts'][0].get('viewCount')):
        print('viewcounts match')
    elif (int(channelStatistics['viewCount']) > record['channelCounts'][0].get('viewCount')):
        print('Viewcounts do not match and update to be done. The current db view count is: ' +
              str(record['channelCounts'][0].get('viewCount')) + '. The new view count is: ' + channelStatistics['viewCount'])

        collection.update_one({'_id': record['_id']}, {
                              '$set': {'channelCounts.0.viewCount': int(channelStatistics['viewCount'])}})
        print('the new updated view count is: ' +
              channelStatistics['viewCount'])
    print('\n')
