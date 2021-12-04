
import re
import pandas as pd
import json
import nltk


with open('tweets-2019-09-01-02.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['tweets'])

# convert tweets to all lowercase, tokenize and remove punctuation
counter = 0
joy_indices = []
new_tweets = []

for tweet in df['content']:

    tweet = tweet.lower()
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    words = tokenizer.tokenize(tweet)
    tweet = ' '.join(words)
    new_tweets.append(tweet)

    if 'joy' in words:
        # create an indicator variable ijoy (if joy is in the tweet)
        # store with indexes instead
        df['ijoy'] = True
        print(tweet)
        counter += 1
    else:
        df['ijoy'] = False

df['content'] = new_tweets
print(counter)


dates = pd.date_range(start = '09/01/2019', end = '09/30/2021', freq = 'M')

months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    months.append([month, year])

print(months)

for month in months:

    file = 'tweets-' 