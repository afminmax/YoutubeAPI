from random import *

# This one for sub-documents
countables = ["viewCount", "commentCount",
              "subscriberCount", "videoCount", "playlistCount"]

print('{')
print('"year": "2020",')
print('"ytcId": "def456",')
print('"lastUpdate": null,')
for item in countables:
    dayNumber = 1
    lastDayNumber = 366
    print('"'+item+'": {')

    startNumber = 0
    nextNumber = 0
    previousNumber = 0
    # randomInteger = randint(1, 1000)
    randomInteger = 0

    while lastDayNumber > 0:
        if dayNumber == 1:
            print('"'+str(dayNumber)+'"' + ': ' + str(startNumber) + ',')
            previousNumber = startNumber
        elif dayNumber != 366:
            nextNumber = previousNumber + randomInteger
            print('"'+str(dayNumber)+'"' + ': ' +
                  str(nextNumber) + ',')
            previousNumber = nextNumber
        else:
            nextNumber = previousNumber + randomInteger
            print('"'+str(dayNumber)+'"' + ': ' +
                  str(nextNumber + randomInteger) + '},')

        lastDayNumber = lastDayNumber - 1
        dayNumber = dayNumber + 1

print('}')


# # This one for arrays
# countables = ["viewCount", "commentCount",
#               "subscriberCount", "videoCount", "playlistCount"]

# print('{')
# print('"year": "2020",')
# print('"ytcId": "def456",')
# print('"lastUpdate": null,')
# for item in countables:
#     dayNumber = 1
#     lastDayNumber = 365
#     print('"'+item+'": [{')

#     startNumber = 5
#     nextNumber = 0
#     previousNumber = 0
#     randomInteger = randint(1, 1000)

#     while lastDayNumber > 0:
#         if dayNumber == 1:
#             print('"'+str(dayNumber)+'"' + ': ' + str(startNumber) + ',')
#             previousNumber = startNumber
#         elif dayNumber != 365:
#             nextNumber = previousNumber + randomInteger
#             print('"'+str(dayNumber)+'"' + ': ' +
#                   str(nextNumber) + ',')
#             previousNumber = nextNumber
#         else:
#             nextNumber = previousNumber + randomInteger
#             print('"'+str(dayNumber)+'"' + ': ' +
#                   str(nextNumber + randomInteger) + '}],')

#         lastDayNumber = lastDayNumber - 1
#         dayNumber = dayNumber + 1

# print('}')
