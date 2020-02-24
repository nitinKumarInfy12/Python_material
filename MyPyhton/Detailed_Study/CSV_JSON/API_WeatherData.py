#! python3

# This program Prints the weather for a location from the command line

import sys, json, requests


# compute location from comand line
testVal = ['quickWeather.py', 'San', 'Francisco,', 'CA']

if (len(sys.argv)) < 2:
#if (len(testVal)) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()
else:
    location = ' '.join(sys.argv[1:])


# TODO: Download the JSON data from OpenWeatherMap.org's API.
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)

response = requests.get(url)
response.raise_for_status() # error check
json_str = response.text  # response.text  has teh json string that can be conveted into python dictionary using the json.loads()

# TODO: Load JSON data into a Python variable.
weatherData = json.loads(json_str)

# shortcut : use weatherData = response.json() instead json_str = response.text, weatherData = json.loads(json_str) to convert into dict.

print(weatherData)

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
