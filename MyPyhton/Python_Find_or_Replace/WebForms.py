import os, openpyxl, glob

excelFile = 'NA_NetShip_Metrics.xls'
rulesPath = '.\\Webforms\\'

webForms = [f for f in glob.glob(rulesPath + "**/*.xlsx", recursive=True)]

wb = openpyxl.load_workbook(excelFile)
sheets = wb.sheetnames
sheet = wb[sheets[0]]

#print(webForms)
# max row in excel
maxRow = sheet.max_row
print(f"Source Max Row:{maxRow}")

# loop though column A and B for the metrics name and metrics code search
for column in range(1,2):
    for row in range(2, maxRow+1):
        cellText = sheet.cell(row=row, column=column).value
        #searchText = f"'{cellText}'"
        print(cellText)

        findFlag = None
        matchFIles = []

        for forms in webForms:
            print(forms)

            wbForm = openpyxl.load_workbook(forms)
            wbFormSheets = wbForm.sheetnames

            for i in range(len(wbFormSheets)):
                wsForm = wbForm[wbFormSheets[i]]

                formMax_Row = wsForm.max_row
                formMax_Column = wsForm.max_column

                for r in range(1, formMax_Row+1):
                    breakBoolean = False
                    for c in range(1, formMax_Column+1):
                        val = wsForm.cell(row=r, column=c).value
                        if val:
                            if cellText.upper == str(val).upper():
                                breakBoolean = True
                                findFlag='W'
                                #fileName = os.path.basename(forms).split('.')[0]+'>'+wsForm.title
                                fileName = os.path.basename(forms) + '>' + wsForm.title
                                print(fileName)
                                matchFIles.append(fileName)
                                break
                        if breakBoolean:
                            print("Breaking the loop and Checking another Sheet in the same Web form")
                            break

            wbForm1 = openpyxl.load_workbook(forms, data_only=True)
            wbFormSheets1 = wbForm1.sheetnames

            for i in range(len(wbFormSheets1)):
                wsForm1 = wbForm[wbFormSheets1[i]]

                formMax_Row1 = wsForm1.max_row
                formMax_Column1 = wsForm1.max_column

                for r1 in range(1, formMax_Row1 + 1):
                    breakBoolean1 = False
                    for c1 in range(1, formMax_Column1 + 1):
                        val1 = wsForm1.cell(row=r1, column=c1).value
                        if val1:
                            if cellText.upper() == str(val1).upper():
                                breakBoolean1 = True
                                findFlag = 'W'
                                #fileName1 = os.path.basename(forms).split('.')[0]+'>'+wsForm1.title
                                fileName1 = os.path.basename(forms) + '>' + wsForm1.title
                                print(fileName1)
                                matchFIles.append(fileName1)
                                break
                        if breakBoolean1:
                            print("Breaking the loop and Checking another Sheet in the same Web form")
                            break

            print("Moving to another web form")

        #update the column D in the sheet
        sheet.cell(row=row, column=5).value = findFlag
        #sheet.cell(row=row, column=3).value = str(matchFIles)

# save file
wb.save(excelFile)
print("Done")

