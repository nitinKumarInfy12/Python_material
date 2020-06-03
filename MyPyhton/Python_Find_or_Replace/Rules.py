import os, openpyxl, glob

excelFile = 'NA_NetShip_Metrics.xlsx'
rulesPath = '.\\Rules'

ruleFiles = [f for f in glob.glob(rulesPath + "**/*.txt", recursive=True)]

wb = openpyxl.load_workbook('NA_NetShip_Metrics.xlsx')
sheets = wb.sheetnames
sheet = wb[sheets[0]]

#print(ruleFiles)

# max row in excel
maxRow = sheet.max_row
#print(maxRow)

# loop though column A and B for the metrics name and metrics code search
for column in range(1,2):
    for row in range(1, maxRow+1):
        cellText = sheet.cell(row=row, column=column).value
        searchText = f"'{cellText}'"

        #print(searchText)

        findFlag = None
        #matchFIles = []

        for ruleFile in ruleFiles:
            with open(ruleFile, 'r') as searchfile:
                if searchText in searchfile.read():
                    findFlag='R'
                    fileName = os.path.basename(ruleFile)
                    #matchFIles.append(fileName)
                    #print(fileName)

                    #update the column C in the sheet
                    sheet.cell(row=row, column=3).value = findFlag

# save file
wb.save(excelFile)


