# PyPI, or the Python Package Index, is a sort of free app store for Python modules
# on windows use pip install module_name to install  the library


# use import module_name to import the modules.
# to read the inbuilt modules. Click ctrl and on the module name
import builtins

#help(builtins.slice)   # thi swill give the list of all buitltin functions as well as teh builtin exceptions. Musdt import he buitlins module for this command
help(builtins.slice)

# import
import myFunctions

print(myFunctions.add(5,7))
print(myFunctions.multiply(5,7))

# or another way to import a module from different dir import dir.myFunctions
#print(dir.myFunctions.add(5,7))
#print(dir.myFunctions.multiply(5,7))


#You can type ? before the name of a method in IPython shell to take a quick look at the documentation.
#e.g.:
import os
? os.makedirs

# or another syntax from dir import myfunctions

print(myFunctions.add(5,7))
print(myFunctions.multiply(5,7))


# or the name can be alliased :
#import <dir>.myfunctions as mf
#print(mf.add(5,7))
#print(mf.multiply(5,7))


# import a class from other file syntax: "from filename import className"


"""# The pyperclip module has copy() and paste() functions that can send text to and
receive text from your computer’s clipboard.After installing the pyperclip module, import it in the code"""

import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()
# 'Hello world!'
"""Of course, if something outside of your program changes the clipboard contents, the
paste() function will return it. For example, if I copied this sentence to the clipboard and
then called paste(), it would look like this:"""
pyperclip.paste()
"""For example, if I copied this sentence to the clipboard and then called
paste(), it would look like this:"""