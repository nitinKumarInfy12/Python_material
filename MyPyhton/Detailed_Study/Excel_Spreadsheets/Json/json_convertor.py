import json

# update the jsonFile variable to point to intended Json File
jsonFile = 'myJson.json'

# load json into program
with open(jsonFile, 'r') as file:
    json_str = file.read()
    print(json_str)

    json_val = json.loads(json_str)

# create new json files
for item in json_val:
    # create file name based on 'Name_Prop2' key
    newJsonName = item['Name_prop2']+'.json'

    # convert dict into list before spiting out the new json files
    listItem = []
    listItem.append(item)

    # create the new Json files with name as given in the attribute
    with open(newJsonName, 'w') as newFile:
        newFile.write(json.dumps(listItem, indent=2))



