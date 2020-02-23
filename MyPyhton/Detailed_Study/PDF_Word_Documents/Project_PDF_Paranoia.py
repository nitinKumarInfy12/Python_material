#! python3

import PyPDF2, os, re, shutil

currWd = os.getcwd()
newDir = os.path.join(currWd, 'Encrypted')
if os.path.exists(newDir):
    shutil.rmtree(newDir)
os.mkdir(newDir)


reg = re.compile(r'.*\.pdf',re.I)

print(currWd)

AllFiles= []
pdfFiles = []
password = 'Test123'

for folder, subfolder, files in os.walk(currWd):
    for file in files:
        AllFiles.append(f"{folder}\\{file}")


for file in AllFiles:
    if reg.findall(file):
        pdfFiles.append(file)

print(len(pdfFiles))
print(pdfFiles)


for file in pdfFiles:
    pdfObj = PyPDF2.PdfFileReader(open(file, 'rb'))

    if not pdfObj.isEncrypted:
        fileName = os.path.basename(file).split('.')[0]
        fileDir = os.path.dirname(file)

        outputFile = open(os.path.join(newDir, fileName+'_encrypted.pdf'),'wb')
        pwb = PyPDF2.PdfFileWriter()

        for i in range(pdfObj.numPages):
            pwb.addPage(pdfObj.getPage(i))

        pwb.encrypt(password)
        pwb.write(outputFile)
        outputFile.close()
        open(file, 'rb').close()


    else:
        fileName = os.path.basename(file).split('.')[0]
        fileDir = os.path.dirname(file)

        pdfWrtr = PyPDF2.PdfFileWriter()
        OutputFile = open(os.path.join(newDir,fileName+'_encrypted.pdf'),'wb')
        pdfObj = PyPDF2.PdfFileReader(open(file, 'rb'))
        pdfObj.decrypt('rosebud')

        for i in range(pdfObj.numPages):
            pdfWrtr.addPage(pdfObj.getPage(i))

        pdfWrtr.encrypt(password)
        pdfWrtr.write(OutputFile)
        OutputFile.close()
        open(file, 'rb').close()


