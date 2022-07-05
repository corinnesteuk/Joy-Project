
# combine all files for one month in a given year
# run separately for each month in each year and enter number of days

import pandas as pd
import json
from datetime import datetime


# combine month files for one year into one
def combine_month(year, month, num_days):

    first_file = 'L:\Joy/Data/tweets-' + str(year) + '-' + str(month) + '-01.json'
    start_date = str(year) + '-' + str(month) + '-02'
    end_date = str(year) + '-' + str(month) + '-' + str(num_days)

    dates = pd.date_range(start = start_date, end = end_date)

    for date in dates:

        date = datetime.strftime(date, '%Y-%m-%d')
        read_file = 'L:\Joy/Data/tweets-' + str(date) + '.json'

        print(date)

    
        f2data = "" 

        with open(read_file) as f2: 
            f2data = '\n' + f2.read()
    
        with open(first_file,'a+') as f1:
            f1.write(f2data)

    # print the contents of the new total month file
    #j2 = pd.read_json(first_file, lines = True)
    #print(j2)


# call combine months function for a specific month
print(combine_month(year = 2022, month = '01', num_days = 25))



# combine month files from one year into one
# give the desired year and the beginning and ending month for our data from that year

def combine_year(start_month, end_month, year):

    first_file = 'L:\Joy/Data/tweets-' + str(start_month) + '-' + str(year) + '.json'

    for month in range(int(start_month) + 1, int(end_month) + 1):

        if len(str(month)) == 1:
            month = '0' + str(month)
    
        read_file = 'L:\Joy/Data/tweets-' + str(month) + '-' + str(year) + '.json'

        print(read_file)
    
        f2data = "" 

        with open(read_file) as f2: 
            f2data = '\n' + f2.read()
    
        with open(first_file,'a+') as f1:
            f1.write(f2data)


# create combined file for 2021
#print(combine_year(start_month = '01', end_month = '09', year = 2021))

# file sizes
# 09/2019: 1.4 mil KB
# 01/2020: 1.454 mil KB
# 01/2021: 1.156 mil KB



'''
# combine year files into one
# files are too large so takes too much memory on current computer
years = ['2020', '2021']

for year in years:
    
    read_file = 'L:\Joy/Data/tweets-' + year + '.json'

    print(read_file)
    
    f2data = "" 

    with open(read_file) as f2: 
        f2data = '\n' + f2.read()
    
    with open('L:\Joy/Data/tweets-2019.json','a+') as f1:
        f1.write(f2data)
'''
