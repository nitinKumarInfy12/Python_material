#! python3
# readCensusExcel.py  - Tabulates population and number of consensus tracts for each country

import openpyxl, pprint

print("Opening the file...")

wb = openpyxl.load_workbook('censuspopdata.xlsx')
#sheet = wb.get_sheet_by_name('Population by Census Tract')
sheet = wb['Population by Census Tract']
#print(sheet)

countryData = {}

# TODO: Fill in countyData with each county's population and tracts.
print("Reading Rows....")

for row in range(2, sheet.max_row + 1):
    # each row has data for one consensus tract
    state = sheet['B'+str(row)].value
    country = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value

    # Make sure the key for this state exists
    countryData.setdefault(state,{})

    # make sure teh key for this country in this state exists
    countryData[state].setdefault(country,{'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one
    countryData[state][country]['tracts'] +=1

    # increase teh country populaton in this census tract
    countryData[state][country]['pop'] += int(pop)


#  TODO: Open a new text file and write the contents of countyData to it.
print("Writing to teh file")
with open('census2010.py','w') as resulFile:
    resulFile.write('allData = ' + pprint.pformat(countryData))

print("Done.")

