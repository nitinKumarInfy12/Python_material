import json

a = {
    'name' : 'nitin',
    'age' : 32,
    'marks' : [90,55,67,32],
    'pass': 'true',
    'object' : {
        'color' : ['red', 'blue', 'Green']
    }
}

print(json.dumps(a)) # json.dumps converts python value to json format. dumps funtion acccepts all format other than sets
print(json.dumps(a, indent=2))  # it will print in the json format with 2 characters indentation
# print(json.dumps(a, indent=2, separators=('.','='))) # it will replace comma with dot an dcolom with equal
print(json.dumps(a, indent=2, sort_keys=True))  # it will sort the keys in alphabatical order


# lets write the values in a json file
with open('testJSON.json','w') as fh:
    fh.write(json.dumps(a, indent=2))

# lets read the values from teh file
with open('testJSON.json', 'r') as fh:
    #print(fh.read()) # this fh.read() returns json contents as string.
    # print(type(fh.read()))
    json_str = fh.read()
    json_value = json.loads(json_str) # this converts the string into JSON
    print(type(json_value))
    print(json_value['name'])

