#! python3

"""Carries out a brute-force password attack on an encrypted PDF."""

import PyPDF2, os

#print('Enter the absolute directory of the PDF you wish to break:')
#file = input()



path = 'C:\\Users\\kumar\\PycharmProjects\\PDF_Word_Documents\\Encrypted'

pdfFiles = os.listdir(path)
print(pdfFiles)

for file in pdfFiles:
    #fileName = os.path.basename(file)
    pdf_reader = PyPDF2.PdfFileReader(open(os.path.join(path,file), 'rb'))
    with open('dictionary.txt') as f:
        words = f.readlines()


    for word in words:
        word = word.strip()
        lower = word.lower()
        upper = word.upper()
        if pdf_reader.decrypt(lower) == 1:
            print(f"Password for {file} is: {lower}")
            break
        elif pdf_reader.decrypt(upper) == 1:
            print(f"Password for {file} is: {upper}")
            break
        elif pdf_reader.decrypt(word) == 1:
            print(f"Password for {file} is: {word}")
            break

