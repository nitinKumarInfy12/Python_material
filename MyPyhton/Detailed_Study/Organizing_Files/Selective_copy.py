#! python3

# This program walks through a folder tree and searches for files with a certain file
# extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a
# new folder.

import shutil, os, zipfile
# shutil module given the abilty to move around the files
# os modules gives you teh ability to deal with folders


searchfolder = 'C:\\Users\\kumar\\OneDrive\\Desktop\\Study Material\\Pyhton\\Python_Study\\Python_youtube\\MyProject'
targetfolder = 'C:\\Users\\kumar\\OneDrive\\Desktop\\Study Material\\Pyhton\\Python_Study\\Python_youtube\\Test'

if not os.path.exists(targetfolder):
    os.mkdir(targetfolder)
    if os.path.exists(targetfolder):
        print("folder created")
else:
    print("folder already exists")



if os.path.exists(searchfolder):
    print("Source folder Exists")
else:
    print("Source Folder doesnot exists")

for folder, subfoldder, filenames in os.walk(searchfolder):
    for filename in filenames:
        if filename.endswith('{}'.format('json')):
            shutil.copy(f"{folder}\\{filename}", f"{targetfolder}\\{filename}")

if os.listdir(targetfolder):
    myzip = zipfile.ZipFile(os.path.join(os.path.dirname(targetfolder),'myZip.zip'),'w')
    myzip.write(targetfolder, compress_type=zipfile.ZIP_DEFLATED)
    myzip.close()








