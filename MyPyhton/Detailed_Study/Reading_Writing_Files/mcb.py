"""This
“multiclipboard” will be named mcb.pyw (since “mcb” is shorter to type than “multiclipboard”).
The .pyw extension means that Python won’t show a Terminal window when it runs this program.
when you run py mcb.pyw save spam, the current contents of the clipboard will be saved with the keyword spam.
This text can later be loaded to the clipboard again by running py mcb.pyw spam.
if the user forgets what keywords they have, they can run py mcb.pyw list to copy a list of all keywords to the clipboard 

create a windows batch file with the following code and run the batch file
@pyw.exe C:\Python34\mcb.pyw % *
"""
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import pyperclip, sys, shelve

mcbself = shelve.open('mcb')

if len(sys.argv)==3 and sys.argv[1].lower()=='save':

    # TODO: Save clipboard content.
    mcbself[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv)==2 and sys.argv[1].lower()=='list':
    # TODO: List keywords and load content.
    pyperclip.copy(str(list(mcbself.keys())))
else:
    pyperclip.copy(str(mcbself[sys.argv[1]]))
mcbself.close()