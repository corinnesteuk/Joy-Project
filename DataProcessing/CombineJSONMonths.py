
# Combine all files for one month in a given year
# run separately for each month in each year and enter number of days

import pandas as pd
import json
from datetime import datetime


# combine day files for one month into a single month file
## month files were too big to upload to GitHub
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
    j2 = pd.read_json(first_file, lines = True)
    print(j2)


# call combine months function for a specific month
## change parameters to match specific month
print(combine_month(year = 2022, month = '01', num_days = 31))