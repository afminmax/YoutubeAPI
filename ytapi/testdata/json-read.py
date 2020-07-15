import json

with open('data.json') as json_file:
    data = json.load(json_file)
    # for p in data['people']:
    #     print('Name: ' + p['name'])
    #     print('Website: ' + p['website'])
    #     print('From: ' + p['from'])
    #     print('')


print(type(data))


# jsonFile = open('data.json')
# jsonString = jsonFile.read()
# jsonData= json.loads(jsonString)
# type(jsonData)
# print(jsonData)
