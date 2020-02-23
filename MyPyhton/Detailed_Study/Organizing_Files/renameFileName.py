# Renaming Files with American-Style Dates to European-Style Dates
# you have thousands of files with American-style dates (MM-DD-YYYY) in their names and needs them renamed to European-style dates (DD-MM-YYYY)
"""
Here’s what the program does:
    It searches all the filenames in the current working directory for American-style dates.
    When one is found, it renames the file with the month and day swapped to make it European-style.

This means the code will need to do the following:
    Create a regex that can identify the text pattern of American-style dates.
    Call os.listdir() to find all the files in the working directory.
    Loop over each filename, using the regex to check whether it has a date.
    If it has a date, rename the file with shutil.move().
"""

import shutil, os, re

# create a regex that matches American date format
datePattern = re.compile(r'''
^(.*?)                                  # all text before the date
((0|1)?\d)-                             # one or two digits for the month
((0|1|2|3)?\d)-                          # one or two digits for the day
((19|20)\d\d)                              # four digits for the year
(.*?)$                                      # all text after the date
''', re.VERBOSE)


#  Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

#  Skip files without a date.
    if mo == None:
        continue
#  Get the different parts of the filename.

# datePattern = re.compile(r"""^(1) # all text before the date
# (2 (3) )- # one or two digits for the month
# (4 (5) )- # one or two digits for the day
# (6 (7) ) # four digits for the year
# (8)$ # all text after the date
# """, re.VERBOSE)

    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

#  Form the European-style filename.
euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

absWorkingDir = os.path.abspath('.')
amerFilename = os.path.join(absWorkingDir, amerFilename)
euroFilename = os.path.join(absWorkingDir, euroFilename)
# Rename the files.
#print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
shutil.move(amerFilename, euroFilename) # uncomment after testing


