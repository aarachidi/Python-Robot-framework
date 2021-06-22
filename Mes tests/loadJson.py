import json


# Opening JSON file
f = open('data.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['composant']:
    print(i['name'])
  
# Closing file
f.close()