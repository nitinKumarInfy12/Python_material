#! python3

# this program combines selected pages from multiple PDF files
import re, os, PyPDF2

currDir = os.getcwd()
AllFiles = os.listdir(currDir)
print(f"All Files : {AllFiles}")
pdfFiles = []
reg = re.compile(r'\.pdf',re.I)

for file in AllFiles:
    if reg.search(file):
        pdfFiles.append(file)
pdfFiles = sorted(pdfFiles)
print(f"PDF files : {pdfFiles}")

pdfwriter = PyPDF2.PdfFileWriter()
OutpUtFIle = open('AllfilesMerged.pdf','wb')

for file in pdfFiles:
    fileReader = PyPDF2.PdfFileReader(open(file, 'rb'))
    if not fileReader.isEncrypted:
        if pdfFiles.index(file)==1:
            for page in range(fileReader.numPages):
                pdfwriter.addPage(fileReader.getPage(page))
        else:
            for page in range(1,fileReader.numPages):
                pdfwriter.addPage(fileReader.getPage(page))

pdfwriter.write(OutpUtFIle)

for file in pdfFiles:
    open(file, 'rb').close()