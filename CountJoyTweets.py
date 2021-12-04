
import re
import pandas as pd
import json
import nltk
import matplotlib.pylab as plt


# count number of joy tweets for each month and store the indices in a dictionary
def count_joy_tweets(list_months):

    monthly_joy_tweets = {}
    joy_counts = {}

    for month in list_months:

        file = 'tweets-' + str(month[0]) + '-' + str(month[1]) + '.json'
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
        monthly_joy_tweets[month_str] = joy_indices
        df['content'] = new_tweets
        
    return joy_counts, monthly_joy_tweets

# create a list of months to loop through for counting joy tweets 
dates = pd.date_range(start = '09/01/2019', end = '09/30/2021', freq = 'M')

months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    months.append([month, year])


joy_counts, monthly_joy_tweets = count_joy_tweets(months)

# plot frequency of joy tweets for each month
plt.plot(joy_counts.keys(), joy_counts.values())

# add title and axis names
plt.title('Monthly Joy Tweets')
plt.xlabel('Month')
plt.ylabel('# Joy Tweets')
plt.show()
