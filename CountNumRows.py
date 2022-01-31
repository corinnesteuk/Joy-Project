
import pandas as pd
import csv

'''This code counts the total number of tweets in each month'''
#The results are saved as a dictionary with the key mm-yyy and the value as the number of tweets in this file
#The dictionary is saved to as a CSV file to be used in other programs for analysis

count = dict()
dates = pd.date_range(start = '09/01/2019', end = '12/31/2021', freq = 'M')

list_months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    list_months.append([month, year])

for month in list_months:
        j = pd.read_json('L:\Joy/Data/tweets-' + str(month[0]) + '-' + str(month[1]) + '.json', lines = True)
        d = str(month[0]) + '-' + str(month[1])
        print(d)
        count[d] = len(j['tweets'][0])
print(count)

new_path = open("Total-Tweets-Per-Month.csv", "w")
z = csv.writer(new_path)
for new_k, new_v in count.items():
    z.writerow([new_k, new_v])
new_path.close()
