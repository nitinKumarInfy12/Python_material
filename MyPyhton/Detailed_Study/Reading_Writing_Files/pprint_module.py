# Saving Variables with the pprint.pformat() Function
"""
Pretty Printing that the pprint.pprint() function will “pretty print” the
contents of a list or dictionary to the screen, while the pprint.pformat() function will
return this same text as a string instead of printing it. Not only is this string formatted to be
easy to read, but it is also syntactically correct Python code. Say you have a dictionary
stored in a variable and you want to save this variable and its contents for future use.
Using pprint.pformat() will give you a string that you can write to .py file. This file will
be your very own module that you can import whenever you want to use the variable
stored in it. These 2 lines are equivalent to each other
pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))
"""

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pprint(cats)
print(pprint.pformat(cats))

fh = open('myCats.py', 'w')
fh.write('cats = ' + pprint.pformat(cats) + '\n')
fh.close()

"""
When
the string from pprint.pformat() is saved to a .py file, the file is a module that can be imported just like any other.
>>> import myCats
>>> myCats.cats
[{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
>>> myCats.cats[0]
{'name': 'Zophie', 'desc': 'chubby'}
>>> myCats.cats[0]['name']
'Zophie'

The benefit of creating a .py file (as opposed to saving variables with the shelve module)
is that because it is a text file, the contents of the file can be read and modified by anyone
with a simple text editor. For most applications, however, saving data using the shelve
module is the preferred way to save variables to a file. Only basic data types such as
integers, floats, strings, lists, and dictionaries can be written to a file as simple text. File
objects, for example cannot be encoded as text so shelve module will be required for such objects

"""