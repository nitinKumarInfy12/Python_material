#! python3

# this program takes Excel Colum data into seperate Excel files.
# names the text file as the name of teh header

import os, openpyxl

Excelfile = 'Excel_Notepad.xlsx'
CurrDir =os.getcwd()

wb = openpyxl.load_workbook(Excelfile)
ws =  wb.active

fileColumns = ws.max_column

for column in range(1, fileColumns+1):
    i = 1
    txtFileName = 'my'+ws.cell(row=1, column=column).value
    txtfilePath = os.path.join(CurrDir, txtFileName+'.txt')

    with open(txtfilePath, 'w') as txtFile:
        while ws.cell(row=i+1, column=column).value:
            txtFile.write(f"{ws.cell(row=i+1, column=column).value}")
            i +=1

print("Done Creting text files")


