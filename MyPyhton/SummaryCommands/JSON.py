import json

"""
Note that JSON strings always use double quotes. It will return that data as a Python
dictionary. Python dictionaries are not ordered, so the key-value pairs may appear in a
different order when you print jsonDataAsPythonValue.
"""


a = {
    'name' : 'Max',
    'agee':22,
    'marks' : [90,50,40,30],
    'pass' : True,
    'object': {
        'color' : ('red','blue')
    }
}
# other than sets, any format or type can be provided as argument to json.dumps method
# The value can only be one of the following basic Python data types: dictionary, list,
# integer, float, string, Boolean, or None.

#json.dumps(a) # this functions creates the JSON file for the informatin is in python dictionary a

# to print the json output
print(json.dumps(a))
print(json.dumps(a, indent=4)) # provis indentation
print(json.dumps(a, indent=2, sort_keys=True)) # sorts based on keys
print(json.dumps(a, indent=4, separators=('.','='))) # replaces comma with dot, colom with equal

# create or write in JSON file
with open('myDemo_JSON.json','w') as fh:
    fh.write(json.dumps(a, indent=2))


# read from JSON file
with open('myDemo_JSON.json','r') as fh1:
#    print(fh1.read()) # it returns a string format print(type(fh.read()))
# to parse the string values into JSOn, need to use the json.loads method, it takes string an dconverts into JSON format
# json.loads converts json file into python dictionary
    json_str = fh1.read()
    json_value = json.loads(json_str)
    print(type(json_value))
    print(json_value['name'])

# now it can be parsed
  #  print(json_val['Name']) # will prnt the namee value from teh Json file


# ==================== API call ==============================================
# TODO: Download the JSON data from OpenWeatherMap.org's API.
import requests, json
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)

response = requests.get(url)
response.raise_for_status() # error check
json_str = response.text  # response.text  has teh json string that can be conveted into python dictionary using the json.loads()

# TODO: Load JSON data into a Python variable.
weatherData = json.loads(json_str)


######################################################################################
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)   #{'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}



pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)     # '{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'
