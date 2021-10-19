import json
import requests


response = requests.get("https://www.swapi.co/api/starships/3")
data = json.loads(response.text)
print("Name: ", data.get('name'))

keyList = list(data.keys())
keyList.sort()
for k in keyList:
    print(k,"=", data[k])
 
