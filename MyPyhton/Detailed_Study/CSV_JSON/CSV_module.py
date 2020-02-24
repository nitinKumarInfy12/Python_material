# to read data from a csv file with teh csv module, need to cSreate a reader object
# the reader object iterates over each lines in csv and returns list for each line having cells from each column in the row as seperate item
# using list() on reader-Object returns list of lists
#       now cell values can be accessed such as exampleData[row][col]   ex: exampleData[0][2]   : '73'

# readerObject.line_num returns the line number for teh current row in the reader object

# Writer Objects lets yo write data in csv
# open the output file in write mode with newline argument , create wrtrObj = csv.writer(OutputfileName) , wrtrObj.writerow([]) writes data in the row
# if you forget to set the newline argument, the rows in output.csv will be double-spaced
# wrtrObj.writerow([]) returns teh number of characters written to teh file

# optional arguments delimiter and lineterminator can also be passe in the writer object . for ex
# Say you want to separate cells with a tab character instead of a comma and you want the rows to be double-spaced.
# csvFile = open('example.tsv', 'w', newline='')   : note the file extn is .tsv  : tab seperated values
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')

# loop through teh current folder directory to find teh csv files
# . represents teh current working directory
# for csvfile in os.listdir('.'):
#     if not csvfile.endswith('.csv'):

# os.makedirs('header_removed', exist_ok=True)  # true wont throw error if tehe folder already exists
# inputDir = '.\\removeCsvHeader'


import csv

Examplefile = open('example.csv')
exampleReader = csv.reader(Examplefile)
exampleData = list(exampleReader)  # using list() on reader-Object returns list of lists

"""
[['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'],
['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'],
['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'],
['4/10/2015 2:40', 'Strawberries', '98']]
"""
exampleData[0][1]  # 'Apples'
exampleData[0][2]  # '73'
exampleData[1][1]  # 'Cherries'
exampleData[6][1]  # 'Strawberries'



# ============================ another 
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # returns the next line in the file when passed the reader object.
    print(header_row)

# =======================Reading data from Readre objects in a for loop==================
for row in exampleData:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))


# ==================================writer Objects==============================
outPutFile = open('output.csv', 'w' , newline='')  # if you forget to set the newline argument, the rows in output.csv will be double-spaced
writerObj = csv.writer(outPutFile)

writerObj.writerow(['spam', 'eggs', 'bacon', 'ham'])
writerObj.writerow(['Hello, world!', 'eggs', 'bacon', 'ham']) # Writer object automatically escapes the comma in the value 'Hello,world!' with double quotes in the CSV file
writerObj.writerow([1, 2, 3.141592, 4])

outPutFile.close()

# ================================= The delimiter and lineterminator Keyword Arguments =================================

#Say you want to separate cells with a tab character instead of a comma and you want the rows to be double-spaced.

csvFile = open('Tab_seperated.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')

csvWriter.writerow(['Apples', 'Oranges', 'Grapes'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()
