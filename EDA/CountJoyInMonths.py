import pandas as pd
import csv
import json
import nltk

'''This code counts the number of instances of joy in the monthly tweet files and writes to a CSV'''

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

        month_str = str(month[0]) + '-' + str(month[1])
        joy_counts[month_str] = counter
        monthly_joy_indicies[month_str] = joy_indices
        df['content'] = new_tweets
        print(month_str)

    return joy_counts, monthly_joy_indicies


# create a list of months to loop through for counting joy tweets
dates = pd.date_range(start='09/01/2019', end='12/31/2021', freq='M')

months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    months.append([month, year])
joy_counts, monthly_indices = count_joy_tweets(months)


df_indx = pd.DataFrame.from_dict(joy_counts, orient = 'index', columns = ['Joy Tweets'])
df_indx.to_csv("Joy-Tweets-Per-Month.csv", mode = 'w' )

