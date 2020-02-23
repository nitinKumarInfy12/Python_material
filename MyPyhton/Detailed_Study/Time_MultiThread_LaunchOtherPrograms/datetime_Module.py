# if you want to display a date in a more convenient format, or do arithmetic with dates
# The datetime module has its own datetime data type. datetime values represent a # specific moment in time
# datetime.datetime.fromtimestamp() : converts the time.time()or Unix epoch timestamp into datetime object
#  timedelta data type, which represents a duration of time rather than a moment in time.
# it takes keyword arguments weeks, days, hours, minutes, seconds, milliseconds, and microseconds. There is no month or year keyword argument
# total_seconds() method of timedelta returns the duration in second
# str() method of timedelta converts it into human readable time format
# datetime.datetime.strftime() converts epoch timestamps or datetime objects into human friendly strings
# f in strftime(), uses similar directives as python`s string formating
# datetime.datetime.strptime() is the revrese function of strftime() : converts formated string into datetime object

import datetime
import time

datetime.datetime.now()   # returns a datetime object fro current date
datetime.datetime(2015, 2, 27, 11, 10, 49, 55, 53)
dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
dt.year, dt.month, dt.day #(2015, 10, 21)
dt.hour, dt.minute, dt.second #(16, 29, 0)


# converts the time.time()or Unix epoch timestamp into datetime object
datetime.datetime.fromtimestamp(1000000)
datetime.datetime(1970, 1, 12, 5, 46, 40)
datetime.datetime.fromtimestamp(time.time())
datetime.datetime(2015, 2, 27, 11, 13, 0, 604980)


# Comparision operators work with datetime objects
halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
halloween2015 == oct31_2015 # True
halloween2015 > newyears2016 # False


# =================================timedelta Data Type=============================================
# A timedelta object has the total duration represented in days, seconds, and microseconds.
# These numbers are stored in the days, seconds, and microseconds attributes, respectively.
# The total_seconds() method will return the duration in number of seconds alone.
# passing a timedelta object to str() will return a nicely formatted, human-readable string representation of the object.

# timedelta objects can be added or subtracted with datetime objects or other timedelta objects using the + and - operators.
# A timedelta object can be multiplied or divided by integer or float values with the * and / operators.


delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
# (11, 36548, 0)
delta.total_seconds()
# 986948.0
str(delta)
# '11 days, 10:09:08'


# arithmetic operations can be performed on datetime objects with timedelta objects
# calculate 100 days from now
dt = datetime.datetime.now()
# datetime.datetime(2015, 2, 27, 18, 38, 50, 636181)
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays
# datetime.datetime(2017, 11, 23, 18, 38, 50, 636181)


oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
# datetime.datetime(2015, 10, 21, 16, 29)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
oct21st - aboutThirtyYears
# datetime.datetime(1985, 10, 28, 16, 29)
oct21st - (2 * aboutThirtyYears)
# datetime.datetime(1955, 11, 5, 16, 29)



""" pausing the program untill a certainn date 
import datetime, time
halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
"""

# ====================strftime()=================================
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
# '2015/10/21 16:29:00'
oct21st.strftime('%I:%M %p')
# '04:29 PM'
oct21st.strftime("%B of '%y")
# "October of '15"


# ======================strptime()============================
datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
datetime.datetime(2015, 10, 21, 0, 0)
datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
datetime.datetime(2015, 10, 21, 16, 29)
datetime.datetime.strptime("October of '15", "%B of '%y")
datetime.datetime(2015, 10, 1, 0, 0)
datetime.datetime.strptime("November of '63", "%B of '%y")
datetime.datetime(2063, 11, 1, 0, 0)

