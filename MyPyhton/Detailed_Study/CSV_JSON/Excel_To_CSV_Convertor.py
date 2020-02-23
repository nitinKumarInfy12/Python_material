#! python3

# this program converts al excel files to csv files in the directory
# for each sheet fo the excel there has to be a csv file created
# The filenames of the CSV files should be <excel filename>_<sheet title>.csv

import csv, openpyxl, os, shutil

excelFilesFolder = '.\\excelSpreadsheets'
csvFilesFolder = '.\\CSV_Files'

excelFiles = []

# remove teh existign folders and all its files
if os.path.exists(csvFilesFolder):
    shutil.rmtree(csvFilesFolder)

# create folder
os.makedirs(csvFilesFolder, exist_ok=True)

# get the excel files list from te folder

for file in os.listdir(excelFilesFolder):
    if not file.endswith('.xlsx'):
        continue
    else:
        excelFiles.append(file)

#print(excelFiles)

# Traverse through teh excel files , get the name, sheet names, and create teh csv files
for excelFile in excelFiles:
    # get the file name
    fileName = excelFile.split('.')[0]
    #print(fileName)

    wb = openpyxl.load_workbook(os.path.join(excelFilesFolder, excelFile))
    listOfSheets = wb.sheetnames
    #print(listOfSheets)

    for sheet in range(0, len(listOfSheets)):
        sheetName = listOfSheets[sheet]
        outputCSVName = f"{fileName}_{sheetName}.csv"

        ws = wb[listOfSheets[sheet]]
        maxRow = ws.max_row
        maxColumn = ws.max_column

        #print(maxRow, maxColumn)

        # create output file csv writer object
        outputCSVFile = open(os.path.join(csvFilesFolder, outputCSVName), 'w', newline='')
        outputWriter = csv.writer(outputCSVFile)

        for row in range(1, maxRow+1):
            cellValues = []
            # traverse through the rows to get the cell values into a list to put into csv
            for cell in ws[row]:
                cellValues.append(cell.value)
                #print(cellValues)

            # write the row cell values into teh csv file
            outputWriter.writerow(cellValues)

        # close teh file for teh sheet
        outputCSVFile.close()


print("All Done")


