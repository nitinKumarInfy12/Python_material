import requests
import json


# make an API call an dstore teh response
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)

print(f"staus_code: {r.status_code}")

# explore the structure of teh data
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

#print(response_dict.keys())
