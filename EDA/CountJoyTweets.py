
import re
import pandas as pd
import json
import nltk
import matplotlib.pylab as plt
from prettytable import PrettyTable


# count number of joy tweets for each month and store the indices in a dictionary
def count_joy_tweets(list_months):

    monthly_joy_indicies = {}
    joy_counts = {}

    for month in list_months:

        file = 'L:\Joy/Data/tweets-' + str(month[0]) + '-' + str(month[1]) + '.json'
        with open(file, 'r') as f:
            data = json.load(f)

        df = pd.DataFrame(data['tweets'])

        counter = 0
        joy_indices = []
        new_tweets = []

        for tweet in df['content']:
    
            tokenizer = nltk.RegexpTokenizer(r"\w+")
            words = tokenizer.tokenize(tweet)


            if 'joy' in words:
                # create an indicator variable ijoy (if joy is in the tweet)
                df['ijoy'] = 1
                counter += 1
                unique_index = pd.Index(df['content'])
                joy_indices.append(unique_index.get_loc(tweet))

            else:
                df['ijoy'] = 0

            tweet = tweet.lower()
            tweet = ' '.join(words)
            new_tweets.append(tweet)

        month_str = str(month[0]) + '/' + str(month[1])
        joy_counts[month_str] = counter
        monthly_joy_indicies[month_str] = joy_indices
        df['content'] = new_tweets
        
    return joy_counts, monthly_joy_indicies

# create a list of months to loop through for counting joy tweets 
dates = pd.date_range(start = '09/01/2019', end = '09/30/2021', freq = 'M')


months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    months.append([month, year])



joy_counts, monthly_joy_indicies = count_joy_tweets(months)

# plot frequency of joy tweets for each month
plt.plot(joy_counts.keys(), joy_counts.values())

# add title and axis names
plt.title('Figure 1: Monthly Joy Tweets')
plt.xlabel('Month')
plt.ylabel('# Joy Tweets')
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.15)

# create points for max and min
joy_max = max(joy_counts, key = joy_counts.get)
joy_min = min(joy_counts, key = joy_counts.get)

plt.plot(joy_max, joy_counts[joy_max], marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
plt.plot(joy_min, joy_counts[joy_min], marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
plt.annotate(f"Maximum = {joy_counts[joy_max]}", (joy_max, joy_counts[joy_max]))
plt.annotate(f"Minimum = {joy_counts[joy_min]}", (joy_min, joy_counts[joy_min]))

plt.savefig('Figure1.png')


# create table with joy counts for each month
table = PrettyTable()

table.title = 'Figure 2'
table.field_names = ['Month', '# Joy Tweets']
for key in joy_counts.keys():
    table.add_row([key, joy_counts[key]])

print(table)


table_str = table.get_string()

with open('Figure2-Table.txt', 'w') as f2:
    f2.write(table_str)
