# import the datetime module
import datetime
import pandas as pd


# datetime in string format for may 25 1999
input = '2021/05/25'

# format
format = '%Y/%m/%d'

# convert from string format to datetime format
datetime = datetime.datetime.strptime(input, format)
dates = pd.date_range(start = '09/01/2019', end = '12/31/2021', freq = 'M')

list_months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    list_months.append([month, year])
# get the date from the datetime using date()
# function
for month in list_months:
    d = str(month[0]) + '-' + str(month[1])
    print(d)

i = list(range(0, len(list_months)))
print(i)

