import pandas as pd
import json
import nltk
import csv

'''Adding January 2022 to our Count Joy Tweets and Count Total Tweets in each Month for visualization purposes'''

total_jan_tweets = ['01-2022']
jan_joy_tweets = ['01-2022']

file_name = '/joy/joyData/tweets-01-2022.json'
with open(file_name, 'r') as f:
    j = json.load(f)

# appending the total number of tweets to list
df = pd.DataFrame(j['tweets'])
total_jan_tweets.append(len(df['content']))

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

# appending the number of joy tweets to list
jan_joy_tweets.append(counter)
# monthly_joy_indicies['01-2022'] = joy_indices
df['content'] = new_tweets


def append_list_as_row(file, row_contents):
    with open(file, 'a+', newline='') as f:
        csv_writer = csv.writer(f)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row_contents)
        f.close()


append_list_as_row('Total-Tweets-Per-Month.csv', total_jan_tweets)
append_list_as_row('Joy-Tweets-Per-Month.csv', jan_joy_tweets)
