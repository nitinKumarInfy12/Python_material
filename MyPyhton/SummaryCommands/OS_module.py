import os
# windows uses \ for folder structures, whereas linux uses / for folder path.
# os.path.join() can be used to write the folder path, that will run on all operating systems.
# for example: os.path.join('usr', 'bin', 'spam') would return 'usr\\bin\\spam' in windows where as  'usr/binspam' on linux etc
"""
>>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in myFiles:
print(os.path.join('C:\\Users\\asweigart', filename))
C:\Users\asweigart\accounts.txt
C:\Users\asweigart\details.csv
C:\Users\asweigart\invite.docx
"""

# curent workign directory or CWD

os.path.join('C:\\Users\\asweigart', 'filename')
os.getcwd()
os.chdir('C:\\Windows\\System32') # move to the folder

"""
There are also the dot (.) and dot-dot (..) folders. A single period (“dot”) for a folder name is shorthand for
“this directory.” Two periods (“dot-dot”) means “the parent folder.”
"""

# creating new folders  makedirs()
os.makedirs('C:\\delicious\\walnut\\waffles')

os.makedirs('headerRemoved', exist_ok=True)

os.path.abspath('relative_path')   # returns absolute path of the relative path
os.path.isabs('path') # returns true if the given path is absolute path
os.path.relpath('path','start') # returns a string of relativ epath from start to path. in absence of start, cwd will be used as start

os.path.dirname('path') # will return everything that comes before the last slash
os.path.basename('path') # returns everything comes after the last slash
os.path.split('path') # returns tuple of both os.path.dirname and os.path.basename

# to split ech folder, use os.sep method with split method
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.split(calcFilePath)
#('C:\\Windows\\System32', 'calc.exe')

calcFilePath.split(os.path.sep)
#['C:', 'Windows', 'System32', 'calc.exe']


os.path.getsize('path') # returns the size in bytes of the file in the path argument.
os.listdir('path') #returns a list of filename strings for each file in the path argument.

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)
# 1117846456

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
# . denotes current working directory
    if not csvFilename.endswith('.csv'):
    
    
os.path.exists('path') # returns TRUE/FALSE if teh path or path/file exists
os.path.isfile('path') # returns TRUE/FALSE if the path arguments exists and is file
os.path.isdir('path') # returns TRUE/FALSE if the path arguments exists and is directory

#walking a directory tree : Say you want to rename every file in some folder and also every file in every subfolder of that folder
# You can use os.walk() in a for loop statement to walk a directory tree
os.walk('path')
os.unlink('path')
os.rmdir('path')
"""
the os.walk()
function will return three values on each iteration through the loop:
1. A string of the current folder’s name
2. A list of strings of the folders in the current folder
3. A list of strings of the files in the current folder
"""
# startswith and endswith methods of os module healp to search a particular type of file
if filename.startswith(f"{sourceFolderName}_") and filename.endswith('.zip'):
    continue    # don back up the backup zip files



