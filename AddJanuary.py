import pandas as pd

total_jan_tweets = ['01-2022']
jan_joy_tweets = ['01-2022']
j = pd.read_json('L:\Joy/Data/tweets-01-2022.json', lines = True)

#appending the total number of tweets to list
total_jan_tweets.append(len(j['tweets'][0]))
df = pd.DataFrame(j['tweets'])
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

#appending the number of joy tweets to list
jan_joy_tweets.append(counter)
monthly_joy_indicies['01-2022'] = joy_indices
df['content'] = new_tweets

def append_list_as_row(file, row_contents):
    with open(file, 'a+', newline='') as f:
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row_contents)
        f.close()


append_list_as_row('/Users/corinnesteuk/PycharmProjects/pythonProject/Total-Tweets-Per-Month.csv', total_jan_tweets)
append_list_as_row('/Users/corinnesteuk/PycharmProjects/pythonProject/Joy-Tweets-Per-Month.csv', jan_joy_tweets)