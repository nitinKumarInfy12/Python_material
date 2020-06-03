import glob
import os

"""
Instructions: 
1. Copy the }Applications folder from the TM1 server and keep it in the same folder where Applications.py python script is
2. The Script will update the files in the same location. Take }Applications folder back up if needed.
3. Once the Script is executed and files are updated with new text, copy back the file to TM1 server.
"""

findtext = "tm1-plan-ibpfs-qa.edf.nikecloud.net\\nacop-qa\\TM1ApplicationForms\\NACOP-QA\\"
replacetext = "tm1-plan-ibpfs-prd.edf.nike.net\\nacop\\TM1ApplicationForms\\NACOP\\"

formfolder = '.\\}Applications\\'
inputFile = [file for file in glob.glob(formfolder + "**/*.extr", recursive=True)]

for each_file in inputFile:
    with open(each_file, 'r') as fr:
        content = fr.read()
        if findtext in content:
            update_contents = content.replace(findtext, replacetext)

            # write back to the file
            with open(each_file, 'w') as fw:
                fw.write(update_contents)
            print(f"Updated {os.path.basename(each_file)}")

print("=============== Process Complete ========================")


