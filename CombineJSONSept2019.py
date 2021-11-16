
import pandas as pd
import json
from datetime import datetime


def combine_month_2019(month, num_days):

    start_date = '2019-' + str(month) + '-02'
    end_date = '2019-' + str(month) + '-' + str(num_days)

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
    
        with open('Data/tweets-2019-09-01.json','a+') as f1:
            f1.write(f2data)


    j2 = pd.read_json('Data/tweets-2019-09-01.json', lines = True)
    print(j2)


print(combine_month_2019(month = '09', num_days = 30))
