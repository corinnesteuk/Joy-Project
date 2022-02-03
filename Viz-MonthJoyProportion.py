import re
import pandas as pd
import json
import nltk
import matplotlib.pylab as plt
from prettytable import PrettyTable
import csv

total_tweets = {}
total_tweets['09-2019'] = '440896'    
with open('L:\Joy/Joy-Project/Total-Tweets-Per-Month.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        total_tweets[row['09-2019']] = row['440896']

'''Count number of joy tweets for each month and store the indices in a dictionary'''
def count_joy_tweets(list_months):
    monthly_joy_indicies = {}
    joy_counts = {}

    for month in list_months:
        #open each month file and creates a data frame with just the 'tweet' feature
        file = 'L:\Joy/Data/tweets-' + str(month[0]) + '-' + str(month[1]) + '.json'
        with open(file, 'r') as f:
            data = json.load(f)

        df = pd.DataFrame(data['tweets'])

        counter = 0
        joy_indices = []
        new_tweets = []

        #in each tweet, there is a feature called 'content' with the text of the tweet
        #we are looping through each word of the content to search for joy
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

        #a counter is kept to keep track of the number of joy tweets for in each month file
        #joy_counts = we save this counter as the value in a dictionary with the corresponding key being the month (mm-yyy)
        #monthly_joy_indicies = we also save a dicitonary of the indices where the joy tweets are found, with the month as the key again
        month_str = str(month[0]) + '/' + str(month[1])
        joy_counts[month_str] = counter
        monthly_joy_indicies[month_str] = joy_indices
        df['content'] = new_tweets

    return joy_counts, monthly_joy_indicies


# create a list of months to loop through for counting joy tweets
dates = pd.date_range(start='09/01/2019', end='09/30/2021', freq='M')

months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    months.append([month, year])

joy_counts, monthly_joy_indicies = count_joy_tweets(months)

#ceates a dictionary with the month as the key and the proportion of joy tweets as the value
freq_joy = {}
idx = list(range(0, len(joy_counts)))
for i in idx:
    freq_joy[list(joy_counts)[i]] = int(list(joy_counts.values())[i])/int(list(total_tweets.values())[i])



# plot frequency of joy tweets for each month
plt.plot(joy_counts.keys(), freq_joy.values())

# add title and axis names
plt.title('Figure 1: Proportion of Joy Tweets by Month')
plt.xlabel('Month')
plt.ylabel('Proportion of Joy Tweets')
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.15)

# create points for max and min
joy_max = max(joy_counts, key=joy_counts.get)
joy_min = min(joy_counts, key=joy_counts.get)

plt.plot(joy_max, joy_counts[joy_max], marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
plt.plot(joy_min, joy_counts[joy_min], marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
plt.annotate(f"Maximum = {joy_counts[joy_max]}", (joy_max, joy_counts[joy_max]))
plt.annotate(f"Minimum = {joy_counts[joy_min]}", (joy_min, joy_counts[joy_min]))

plt.savefig('Figure1.png')

'''Create Table with Proportion of Joy Tweets Per Month'''
table = PrettyTable()

table.title = 'Figure 2'
table.field_names = ['Month', '# Joy Tweets', 'Total # of Tweets', 'Proportion of Joy Tweets']
for i in idx:
    table.add_row(list(joy_counts.keys())[i], list(total_tweets.values())[i]), list(freq_joy.values()[i])
print(table)

table_str = table.get_string()

with open('Figure2-Table.txt', 'w') as f2:
    f2.write(table_str)