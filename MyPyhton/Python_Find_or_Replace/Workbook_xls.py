import os, xlrd, glob, openpyxl

excelFile = 'NA_NetShip_Metrics.xlsx'
#rulesPath = '.\\Webforms\\'
#rulesPath = '.\\Webforms\\SRI'
rulesPath = '.\\Webforms\\'
webForms = [f for f in glob.glob(rulesPath + "**/*.xls", recursive=True)]

wb = openpyxl.load_workbook(excelFile)
sheets = wb.sheetnames
sheet = wb[sheets[0]]


#print(webForms)
# max row in excel
maxRow = sheet.max_row
#print(f"Source Max Row:{maxRow}")

# loop though column A and B for the metrics name and metrics code search
for column in range(1,2):
    for row in range(2, maxRow+1):
        cellText = sheet.cell(row=row, column=column).value
        #searchText = f"'{cellText}'"
        #print(cellText)

        findFlag = None
        matchFIles = []

        for forms in webForms:
            print(forms)

            wbForm = xlrd.open_workbook(forms)
            wbFormSheets = wbForm.sheet_names()
            print(wbFormSheets)

            for i in range(len(wbFormSheets)):
                wsForm = wbForm.sheet_by_index(i)

                formMax_Row = wsForm.nrows
                formMax_Column = wsForm.ncols

                for r in range(0, formMax_Row):
                    breakBoolean = False
                    for c in range(0, formMax_Column):
                        val = wsForm.cell(r, c).value
                        if val:
                            if cellText.strip().upper() == str(val).strip().upper():
                                breakBoolean = True
                                findFlag='W'
                                #fileName = os.path.basename(forms).split('.')[0]+'>'+wsForm.title
                                fileName = os.path.basename(forms) + '>' + wsForm.name
                                print(str(val))
                                print("File Name : "+fileName)
                                matchFIles.append(fileName)
                                break
                        if breakBoolean:
                            print("Breaking the loop and Checking another Sheet in the same Web form")
                            break
                    #if breakBoolean:
                    #    print("Breaking the loop and Checking another Sheet in the same Web form")
                    #    break

            print("Moving to another web form")

        #update the column D in the sheet
        sheet.cell(row=row, column=5).value = findFlag
        sheet.cell(row=row, column=6).value = str(matchFIles)


# save file
wb.save(excelFile)
print("Done")

