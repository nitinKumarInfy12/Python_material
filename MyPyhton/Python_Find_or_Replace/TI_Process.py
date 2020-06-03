import os, openpyxl, glob

excelFile = 'NA_NetShip_Metrics.xlsx'
rulesPath = '.\\TI_Process'

tiFiles = [f for f in glob.glob(rulesPath + "**/*.pro", recursive=True)]

wb = openpyxl.load_workbook(excelFile)
sheets = wb.sheetnames
sheet = wb[sheets[0]]

#print(tiFiles)

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

        for tiPro in tiFiles:
            with open(tiPro, 'r') as searchfile:
                if searchText in searchfile.read():
                    findFlag='T'
                    fileName = os.path.basename(tiPro)
                    #matchFIles.append(fileName)
                    #print(fileName)

                    #update the column D in the sheet
                    sheet.cell(row=row, column=4).value = findFlag

# save file
wb.save(excelFile)

