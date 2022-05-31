
import re
import pandas as pd
import json


# reformat json file to contain an array of all tweets 
# so it can be easily read in by json.loads function

def reformat_json(file):

    json_string = ""

    with open(file) as f: 

        json_string = f.read() + '\n'

        output_dict = dict()
        output_dict['tweets'] = list()

    for line in json_string.split('\n'):
        if line != '':
            json_line = json.loads(line)
            output_dict['tweets'].append(json_line)


    with open(file, 'w') as f2:
        json.dump(output_dict, f2)


# this reformats the json files for each MONTH
# create a list of months to loop through 
dates = pd.date_range(start = '10/01/2021', end = '01/31/2022', freq = 'M')


months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    months.append([month, year])


# reformat JSON file for each month
for month in months:

    file_name = 'L:\Joy/Data/tweets-' + str(month[0]) + '-' + str(month[1]) + '.json'
    reformat_json(file_name)
