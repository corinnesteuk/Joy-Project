
import pandas as pd
import json
import datetime

# print the number of rows in the json file
# read_json is giving an error again so maybe we need to reformat the file again? 
# does this mean it didn't save?
# difficult because we cannot open the file to view the format because it is too large...
# I am making a copy of all our large month and year data files so that if we 
# accidentally reformat twice and screw them up we have a backup
#f = open('L:\Joy/Data - Copy/tweets-03-2020.json')
#data = json.load(f)
#print(data)
#f.close()

#j = pd.read_json('L:\Joy/Data - Copy/tweets-03-2020.json', lines = True)
#print(len(j['tweets'][0]))
count = dict()

dates = pd.date_range(start = '09/01/2019', end = '09/30/2021', freq = 'M')

list_months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    list_months.append([month, year])

for month in list_months:
        j = pd.read_json('L:\Joy/Data/tweets-' + str(month[0]) + '-' + str(month[1]) + '.json', lines = True)
        #both of the 'd' using pandas or the datetime packages produces same output, 
        # it will default to putting '01' as the day and 0 for the time
        #converting it to a datetime may help when calling it for analyses
        d = datetime.datetime.strptime(str(month[0]) + "-" + str(month[1]), '%m-%Y')
        #d = pd.to_datetime(str(month[0]) + "-" + str(month[1]), format= '%m-%Y') 
        print(d)
        count[d] = len(j['tweets'][0])
print(count)
# after this I was going to try reformating the data again to see if this code would 
# work after that
# the copy of the Data folder said it would be done in about 25 minutes

#we may want to copy this count into a file? so we can call it in when using it in other programs