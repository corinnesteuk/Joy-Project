
import pandas as pd
import json
from datetime import datetime


def combine_month_2021(month, num_days):

    first_file = 'Data/tweets-2021-' + str(month) + '-01.json'
    start_date = '2021-' + str(month) + '-02'
    end_date = '2021-' + str(month) + '-' + str(num_days)

    dates = pd.date_range(start = start_date, end = end_date)

    for date in dates:

        date = datetime.strftime(date, '%Y-%m-%d')
        read_file = 'Data/tweets-' + str(date) + '.json'

        print(date)

        '''
        j = pd.read_json(read_file, lines = True)
        j = j.drop(columns = ['_type', 'url', 'cashtags'])
        #j = j.set_index(['id'])
        print(j)
        '''
    
        f2data = "" 

        with open(read_file) as f2: 
            f2data = '\n' + f2.read()
    
        with open(first_file,'a+') as f1:
            f1.write(f2data)


    #j2 = pd.read_json(first_file, lines = True)
    #print(j2)

    '''
    # tried writing to a new file with a new name but it was fatser/easier to just change the name of the file for the first day of the month
    new_file = 'tweets-' + str(month) + '-2019'
    
    with open(new_file,'w') as f3:
            f3.write(j2)
    '''


print(combine_month_2021(month = '01', num_days = 31))




def combine_year(start_month, end_month, year):

    first_file = 'Data/tweets-' + str(start_month) + '-' + str(year) + '.json'

    for month in range(int(start_month) + 1, int(end_month) + 1):

        if len(str(month)) == 1:
            month = '0' + str(month)
    
        read_file = 'Data/tweets-' + str(month) + '-' + str(year) + '.json'

        print(read_file)
    
        f2data = "" 

        with open(read_file) as f2: 
            f2data = '\n' + f2.read()
    
        with open(first_file,'a+') as f1:
            f1.write(f2data)


# 09/2019: 1.4 mil KB
# 01/2020: 1.454 mil KB
# 01/2021: 1.156 mil KB

#print(combine_year(start_month = '01', end_month = '09', year = 2021))
'''
years = ['2020', '2021']

for year in years:
    
    read_file = 'Data/tweets-' + year + '.json'

    print(read_file)
    
    f2data = "" 

    with open(read_file) as f2: 
        f2data = '\n' + f2.read()
    
    with open('Data/tweets-2019.json','a+') as f1:
        f1.write(f2data)
'''
