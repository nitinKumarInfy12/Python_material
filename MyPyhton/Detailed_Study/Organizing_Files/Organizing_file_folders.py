# shutil (shell utilities), module has functions to let you copy, move, rename, and delete files in your Python programs

import shutil, os, zipfile
# import    send2trash

shutil.copy('source_file path_name', 'destination_file or_path_name_file') # copies a single file. target folder must exists
shutil.copytree('source_path', 'destination_path') # copies the entire folder structure anf files in it
shutil.move('source_file path_name', 'destination_file path_or_name') # moves/renames the file from source to target


# You can delete a single file or a single empty folder with functions in the os module,
# whereas to delete a folder and all of its contents, you use the shutil module.

os.unlink('path') # deletes the file at the path
os.rmdir('path') # will delete the folder at path. This folder must be empty of any files or folders
shutil.rmtree('path') # permanently deletes the folder at path, and all files and folders it contains will also be deleted

# send2trash module is used to soft/safe delete
"""
>>> import send2trash
>>> baconFile = open('bacon.txt', 'a') # creates the file
>>> baconFile.write('Bacon is not a vegetable.')
25
>>> baconFile.close()
>>> send2trash.send2trash('bacon.txt')

"""

# walking a directory tree : Say you want to rename every file in some folder and also every file in every subfolder of that folder
os.walk('path') # returns 3 values. string of current folder name, list of strings of the foders in teh current folder, list of strings of file in teh current folder

"""
for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
    print('')
    
The current folder is C:\delicious
SUBFOLDER OF C:\delicious: cats
SUBFOLDER OF C:\delicious: walnut
FILE INSIDE C:\delicious: spam.txt
The current folder is C:\delicious\cats
FILE INSIDE C:\delicious\cats: catnames.txt
FILE INSIDE C:\delicious\cats: zophie.jpg
The current folder is C:\delicious\walnut
SUBFOLDER OF C:\delicious\walnut: waffles
The current folder is C:\delicious\walnut\waffles
FILE INSIDE C:\delicious\walnut\waffles: butter.txt
"""


# zip files : python can create or read/extract zip files using zipfile module
# import zipfile

# read zip files with ZipFil(), namelist(), getinfo() , file_size, compress_size, close() methods
# ZiepFil() is like open() method for file.
"""
os.chdir('C:\\') # move to the folder with example.zip
>>> exampleZip = zipfile.ZipFile('example.zip')
>>> exampleZip.namelist()
['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
>>> spamInfo = exampleZip.getinfo('spam.txt')
>>> spamInfo.file_size
13908
>>> spamInfo.compress_size
3828
>>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
.compress_size, 2))
'Compressed file is 3.63x smaller!'
>>> exampleZip.close()
"""

# extract from zip file using extract() or extractall() methods
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extract('file.txt')
exampleZip.extractall()
exampleZip.close()


# adding to zip file. using write() method and write method
# zipfile('filename','w') : w mode overrites the existing ziped file or creates a new if not exists already
# zipfile('filename','a') : a mode appends teh file into teh existing zip file or creates new if not exists alreay
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()



