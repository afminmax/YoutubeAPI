

countables = ["viewCount", "commentCount",
              "subscriberCount", "videoCount", "playlistCount"]

print('{')
print('"year": "2020",')
print('"ytcId": null,')

for item in countables:
    countNum = 1
    endNum = 365
    print('"'+item+'": {')

    while endNum > 0:
        if countNum != 365:
            print('"'+str(countNum)+'"' + ': 0,')
        else:
            print('"'+str(countNum)+'"' + ': 0},')
        endNum = endNum - 1
        countNum = countNum + 1

print('"lastUpdate": null')
print('}')
