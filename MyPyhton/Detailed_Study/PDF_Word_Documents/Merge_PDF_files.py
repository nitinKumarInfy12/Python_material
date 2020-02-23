import PyPDF2

# create writer instance
pdfWrite = PyPDF2.PdfFileWriter()

# create instances for FIle1
pdfFile1 = open('meetingminutes.pdf','rb')
pdfReader1 = PyPDF2.PdfFileReader(pdfFile1)

# add pages from Pdf1 to PDF writer Object
for page in range(pdfReader1.numPages):
    pageObj1 = pdfReader1.getPage(page)
    pdfWrite.addPage(pageObj1)


# create instances for FIle2
pdfFile2 = open('meetingminutes2.pdf','rb')
pdfReader2 = PyPDF2.PdfFileReader(pdfFile2)

# add pages from Pdf2 to PDF writer Object
for page in range(pdfReader2.numPages):
    pageObj2 = pdfReader2.getPage(page)
    pdfWrite.addPage(pageObj2)

# open output page in write-binary mode
pdfOutPutfile = open('merged_Meetings.pdf', 'wb')

# write the page objects from pdf1 and pdf2 into the output file using the pdfwriter.write()
pdfWrite.write(pdfOutPutfile)

#close the pdf files
pdfFile1.close()
pdfFile2.close()
pdfOutPutfile.close()
