#! pyhton3
import os, shutil

targetfolder = 'C:\\Users\\kumar\\OneDrive\\Desktop\\Study Material\\Pyhton\\Python_Study\\Python_youtube\\Test'
filesTobeDel = []

for folder, subfolders, files in os.walk(targetfolder):
    for file in files:
        filesize = os.path.getsize(os.path.join(folder,file))
        print(f"Size of the file {file}: {filesize}")
        if int(filesize) > 1000:
            #filesTobeDel.append(os.path.join(folder,file))
            with open(os.path.join(os.path.dirname(targetfolder),'otpt.txt'), 'a') as f:
                f.write(f"File {os.path.join(folder,file)} has been deleted.\n")
                os.unlink(os.path.join(folder, file))










