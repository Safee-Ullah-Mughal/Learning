import requests
import json

data = requests.get("https://jsonplaceholder.typicode.com/users")
cleandata=data.json()

keydata=cleandata[0]
a=keydata.keys()
print(a)
newlist=[]



for i in range(5):
    keydata=cleandata[i]
    print(keydata['name'])
    print(keydata['email'])
    print(keydata['address'])

 
with open("extracted_data.json","w") as file:
    json.dump(keydata, file, indent=4)

