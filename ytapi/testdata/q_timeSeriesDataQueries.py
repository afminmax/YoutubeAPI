from _typeshed import FileDescriptor
from fiscalyear import FiscalQuarter
import pymongo
from pymongo import MongoClient
import json
from pathlib import Path
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import calendar
import pandas as pd
import math


# MAKE MONGODB CONNECTION
dataFolder = Path("C:/Coding/YoutubeAPI/keys/")
fileToOpen = dataFolder / "dbc.txt"
with open(fileToOpen) as file:
    dbc_key = file.read()
myClient = MongoClient(dbc_key)
db = myClient['channelsDB']
collection = db['ChannelTimeStats']
print('the db key to be used is: ' + dbc_key)
print(db)
print(collection)

# IMPORTANT MONGO FIND NOTE
# FIND - will give you ALL matching documents to a query
#        if you have multiple items that may fit a query, use this.
#        example - similar to the WHERE clause in sql

# FINDONE - will only give you the FIRST matching document to a query.
#           be sure you really need only one unique item when using.

# ---------------------------------------------------------------------------------
# 1-LOOK AT ALL ITEMS (SELECT *)
# outputs all data in channel timeseries document

for record in collection.find():
    print(record)
    print('\n')

# ---------------------------------------------------------------------------------
# 2-GET THE VIEWCOUNTS OF A SPECIFIC CHANNEL
# get the viewCounts of a channel
# put in the sub-doc if needed for another query (ex: sub-counts)

# verbose with ytcid for check
collection.find_one({'ytcId': 'abc123'}, {'ytcId': 1, 'viewCount': 1})
# specific for pandas with object id removed
collection.find_one({'ytcId': 'abc123'}, {'_id': 0, 'viewCount': 1})

# ---------------------------------------------------------------------------------
# 3-PUT THE VIEWCOUNTS INTO A PYTHON DICTIONARY
# note that the python dictionary get() method extracts only the values
viewCount_dict = collection.find_one(
    {'ytcId': 'abc123'}, {'_id': 0, 'viewCount': 1}).get('viewCount')
print(viewCount_dict)

# get a specific count from the dictionary, say day 27
# note that a string is required
viewCount_dict.get('27')

# ---------------------------------------------------------------------------------
# 4-BUILT IN PYTHON METHODS FOR DATE

# 4A-GET THE CURRENT DAY OF THE YEAR
day_of_year = datetime.now().timetuple().tm_yday

# 4B-GET DAY OF THE MONTH
day_of_month = datetime.now().day

# 4C-GET MONTH OF THE YEAR
month_of_year = datetime.now().month

# 4D-DAYS UNTIL LAST DAY OF MONTH
# get last day of month - current day of month

# 4E-GET YEAR
year = datetime.now().year

# 4F-GET QUARTER
current_quarter = int(math.ceil(month_of_year/3))
print(current_quarter)

# 4G-GET FIRST DAY OF QUARTER
# source bookmarked in stack overflow
# first_day = datetime(year, 3 * current_quarter - 2, 1)
first_day = datetime(year, (month_of_year - 1) // 3 * 3 + 1, 1)
print('first day of quarter: ' + str(first_day))

# 4H-GET LAST DAY OF QUARTER
last_day = first_day + relativedelta(months=3, days=-1)
print('last day of quarter: ' + str(last_day))

# 4I-TIME (Local!)
currentSecond = datetime.now().second
currentMinute = datetime.now().minute
currentHour = datetime.now().hour

# ---------------------------------------------------------------------------------
# 5-BUILT IN PYTHON CALENDAR METHODS

# 5A-DETECT IF ITS A LEAP YEAR
calendar.isleap(datetime.now().year)

# 5B-GET MONTH CALENDAR
# returns a list with sub-lists per week. zeros are days not in current month
calendar.monthcalendar(year, month_of_year)

# ---------------------------------------------------------------------------------
# 6-DAY MATHS
# use the dictionary get() method to extract the value...
# the day_of_year must be converted to a string first!

# 6A-GET COUNT FOR THE CURRENT DAY
viewCount_dict.get(str(day_of_year))

# 6B-GET COUNT FOR THE PREVIOUS DAY
viewCount_dict.get(str(day_of_year - 1))

# 6C-GET COUNT FOR 3 DAYS PRIOR
viewCount_dict.get(str(day_of_year - 3))

# 6D-GET COUNT FOR 7 DAYS PRIOR (PREVIOUS WEEK)
viewCount_dict.get(str(day_of_year - 7))

# 6E-GET COUNT FOR 14 DAYS PRIOR (PREVIOUS 2 WEEKS)
viewCount_dict.get(str(day_of_year - 14))

# 6F-GET COUNT FOR 21 DAYS PRIOR (PREVIOUS 3 WEEKS)
viewCount_dict.get(str(day_of_year - 21))

# 6G-GET COUNT FOR 28 DAYS PRIOR (PREVIOUS 4 WEEKS, ~MONTH-ish)
viewCount_dict.get(str(day_of_year - 28))

# ---------------------------------------------------------------------------------
# DICTIONARY TO PANDAS DATAFRAME
df = pd.Series(viewCount_dict).to_frame('Counts')
df.head()
