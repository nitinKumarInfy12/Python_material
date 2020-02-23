# pdf file are binary files
# PyPDF2 is the module to work with PDF documents
# PyPDF2 does not have a way to extract images, charts, or other media from PDF documents,
# but it can extract text and return it as a Python string.
# use PyPDF2.PdfFileReader() to read teh pdf file obj
# numPages attribute of pdfreader Object to get the number of pages
# getPage() on pdfreader object to crate a page object of specific page
# extractText() function on page object to extrat page contents in string format

#===============================Password Protected PDF=======================================
# use isEncrypted attribute of pdfreader object to check if PDF is password protected
# use readerObject.dycrypt('password') to unlock teh PDF . it returns 1 if successfull else returns 0

#===============================Write PDF=======================================
# PdfFileWriter to be used to create/write pdf pages
# write() of pdffilewriter is used to write pages
# pdfWriter.addPage(pageObj) is used to add pages to pdfwriter
# PDF-writing capabilities are limited to copying pages from other PDFs, rotating pages, overlaying pages, and encrypting files.
# doesn’t allow you to directly edit a PDF. Instead, you have to create a new PDF and then copy content over from an existing document
"""general approach:
1. Open one or more existing PDFs (the source PDFs) into PdfFileReader objects.
2. Create a new PdfFileWriter object.
3. Copy pages from the PdfFileReader objects into the PdfFileWriter object.
4. Finally, use the PdfFileWriter object to write the output PDF.

# pdfWriter`s write() method creates/writes pdf pages. it takes a regular File object that has been opened in write-binary mode.

#####=============================Rotate PDF Pages================================
# rotateClockwise() and rotateCounterClockwise() methods on pageObject. Pass one of the integers 90, 180, or 270 to these methods

## ==============================Overlaying Pages==================================
# PyPDF2 can also overlay the contents of one page over another. it is useful for adding a logo, timestamp, or watermark to a page.
# pageObj1.mergePage(pageObj2)  : it updates teh pageObj1 as updated(merged) page object to use further

## ============================== Encrypt/Password Protect the PDF===================
# use pdfWriter.encrypt('password')  to protect teh file before calling the pdfWriter.write() on output pdf file

"""

import PyPDF2
fileName = 'meetingminutes.pdf'

pdfFileObj = open(fileName, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print(pdfReader.numPages)

pageObj1 = pdfReader.getPage(0)  # it uses zero-based index system for pages.

print(pageObj1.extractText())
#pdfFileObj.close()
######################################## encrypted pdf============================

pdfReaderObj = PyPDF2.PdfFileReader(open('encrypted.pdf','rb'))
print(pdfReaderObj.isEncrypted)
# true

pdfReaderObj.decrypt('rosebud')
# 1
print(pdfReaderObj.numPages)
pageObj2 = pdfReaderObj.getPage(0)
pageObj2.extractText()

#open('encrypted.pdf','rb').close()

############################ write PDF =================================================
# merging page 1 from meetingminutes.pdf and encrypted.ef and creating a new pdf with these pages

# pageObj1 is teh page object from first pdf
# pageObj2 is teh page object from Second pdf

# create object for PdfFileWriter()
pdfWriter = PyPDF2.PdfFileWriter()

# add pages to teh writer object
pdfWriter.addPage(pageObj1)
pdfWriter.addPage(pageObj2)

# open the output file in write-binary mode t pass to write function
pdfOutputFile = open('mergedFile.pdf', 'wb')

# pass the outputfile ref to write method
pdfWriter.write(pdfOutputFile)

# close teh pdf files
pdfOutputFile.close()
pdfFileObj.close()
open('encrypted.pdf','rb').close()


#####===================================== Rotate PDF Page ======================
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultPdfFile)
resultPdfFile.close()
minutesFile.close()

###=======================================Overlaying Pages=====================
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()



### ===================================== Encrypt/password protect PDF ========================

pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))
pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
