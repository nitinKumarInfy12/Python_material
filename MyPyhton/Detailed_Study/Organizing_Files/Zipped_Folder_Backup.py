#! python3
"""
create ZIP file “snapshots” of the entire folder with different versions name each tim ecode is executed, so you want the ZIP
file’s filename to increment each time it is made; for example, AlsPythonBook_1.zip,AlsPythonBook_2.zip, AlsPythonBook_3.zip, and so on
"""

import zipfile, os

def backupToZip(folder):
    # backup teh entire content of folder into a zip file
    folder = os.path.abspath(folder)
    sourceFolderPath = os.path.dirname(folder) # the folder back up needs to be placed
    sourceFolderName = os.path.basename(folder) # folder to be backed up

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFileName = f"{sourceFolderName}_{str(number)}.zip"
        if not os.path.exists(zipFileName):
            break
        print(f"Creating the {zipFileName}")
        number +=1



    backUpZip = zipfile.ZipFile(zipFileName, 'w') # open teh zipfile in edit mode

    # TODO: Walk the entire folder tree and compress the files in each folder.print('Done.')
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding {foldername} file in {zipFileName}.zip")
        # add teh curent folder to teh zip
        backUpZip.write(foldername, compress_type=zipfile.ZIP_DEFLATED)

        # add the files in this foldere to teh zip file
        for filename in filenames:
            if filename.startswith(f"{sourceFolderName}_") and filename.endswith('.zip'):
                continue    # don back up the backup zip files

            backUpZip.write(os.path.join(foldername, filename), compress_type=zipfile.ZIP_DEFLATED)


    backUpZip.close()


# call teh function by passing the folder details
backupToZip('C:\\Users\\kumar\\PycharmProjects\\Organizing_Files')
