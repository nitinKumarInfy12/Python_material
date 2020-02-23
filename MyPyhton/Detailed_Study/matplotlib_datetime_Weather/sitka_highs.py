import csv
import matplotlib.pyplot as plt
from datetime import datetime
# Imports datetime class from teh datetime module

#filename = 'data/sitka_weather_07-2018_simple.csv'
#filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f) #csv.reader returns row by row in form of list for each row'''
    header_row = next(reader)

#    # Get hight tempartures from the file
#    highs = []
#    for rows in reader:
#       high = int(rows[5])
#        highs.append(high)
#
#    print(highs)

    # Getdates and high temperatures from teh file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        #high = int(row[5])
        #low = int(row[6])

        # updating the index for death_valley_2018_simple.csv file, to do error checking
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    #print(dates)

    # plot the high temperatures
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    #ax.plot(dates, highs, c='red')
    # plots the list items in red color
    #ax.plot(dates, lows, c='blue') # can plot multiple series

    # lets fill teh area between teh 2 series, need to use teh fill_between() method following updating the ax.plot method parameters
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # Alpha value controls teh color transparency, alpha value of 0 is completely transparent, and 1 (the default) is completely opaque

    # format plot
    #plt.title("Daily high temperatures, July 2018", fontsize = 24)
    #plt.title("Daily high temperatures - 2018", fontsize=24)
    title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()  # it plots teh date labels diagonally to prevent from overlapping
    plt.ylabel("Temprature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show() #displays the chart


#for index, column_header in enumerate(header_row): # enumerate function returns both index and value from teh list
#    print(index, column_header)
# out put of teh loop
'''
0 STATION
1 NAME
2 DATE
3 PRCP
4 TAVG
5 TMAX
6 TMIN
'''




