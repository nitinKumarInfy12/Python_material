#! python3

# this program removes header from teh CSV files in teh current directory

import csv, os

os.makedirs('header_removed', exist_ok=True)  # true wont throw error if tehe folder already exists
inputDir = '.\\removeCsvHeader'
outPutDir = '.\\header_removed'

# loop through teh current folder directory to find teh csv files
# for csvfile in os.listdir('.'):

# loop through in the folder to find a certain file type
for csvfile in os.listdir(inputDir):
    if not csvfile.endswith('.csv'):
        continue
    else:
        print(f"Removing header from the {csvfile} file")

        # create input file object
        inputFile = open(os.path.join(inputDir, csvfile))
        fileReader = csv.reader(inputFile)
        fileReaderList = list(fileReader)

        # create output file object
        outputfile = open(os.path.join(outPutDir, csvfile), 'w', newline='')
        fileWriter = csv.writer(outputfile)

        for row in fileReaderList:
            if fileReader.line_num ==1:
                continue
            else:
                fileWriter.writerow(row)
        outputfile.close()






