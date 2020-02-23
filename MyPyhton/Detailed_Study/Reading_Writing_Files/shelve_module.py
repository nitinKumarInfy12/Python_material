# if you want to save data from your Python programs, use the shelve module
"""
You can save variables from Python programs to binary shelf files using the shelve module.
This way, your program can restore data to variables from the hard drive.
The shelve module will let you add, Save and Open features to your program and then have the program load them the next time it is run.
it allows to save variables as it is a dictionary
"""

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')

print(shelfFile['cats'])
shelfFile.close()

"""
Just like dictionaries, shelf values have keys() and values() methods that will return list like values of the keys and values in the shelf. 
Since these methods return list-like values instead of true lists, you should pass them to the list() function to get them in list form
"""

shelfFile = shelve.open('mydata')
print(f"keys : {shelfFile.keys()}")
print(f"keys -list() : {list(shelfFile.keys())}")

print(f"Values: {shelfFile.values()}")
print(f"Values -list() : {list(shelfFile.values())}")

print(f"Key Value : {shelfFile.items()}")
print(f"Key Value -list() : {list(shelfFile.items())}")
shelfFile.close()

