import pprint, json

myJson = [
    {
        'Dict1_prop1': 'Dict1_value1',
        'Name_prop2': 'Dict1_FileNameProp',
        'Dict1_prop3': 'Dict1_value1'
    },
{
        'Dict2_prop1': 'Dict2_value1',
        'Name_prop2': 'Dict2_FileNameProp',
        'Dict2_prop3': 'Dict2_value1'
    },
{
        'Dict3_prop1': 'Dict3_value1',
        'Name_prop2': 'Dict3_FileNameProp',
        'Dict3_prop3': 'Dict3_value1'
    },
{
        'Dict4_prop1': 'Dict4_value1',
        'Name_prop2': 'Dict4_FileNameProp',
        'Dict4_prop3': 'Dict4_value3'
    },
]

print("=============Normal Print==========================")
print(myJson)

print("=================PPprint Print=====================")
pprint.pprint(myJson)

print("===============ppPrint Pformat========================")
print("=================ppPrint Format=== writes python format of Dictionary")
print(pprint.pformat(myJson))


jSonFileName = 'myJson.json'
with open(jSonFileName, 'w') as file:
    file.write(json.dumps(myJson, indent=2))


jSonFileName = 'myJson_pprint.py'
with open(jSonFileName, 'w') as file:
    file.write(pprint.pformat(myJson))

print("Master Json file myJson.json is created")



