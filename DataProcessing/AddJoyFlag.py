## Add a column to the data to indicate if a tweet includes the word joy

import pandas as pd
import json
import nltk


# create a list of months to loop through month files
dates = pd.date_range(start = '09/01/2019', end = '01/31/2022', freq = 'M')

months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    months.append([month, year])



# loop through month files
## month files that were used are too large to add to GitHub
for m in months:
    file = 'tweets-' + str(month[0]) + '-' + str(month[1]) + '.json'

    with open(file, 'r') as f:
        data = json.load(f)


    # drop irrelevant columns
    for t in data['tweets']:
        myElementDel = ('_type','url', 'conversationId', 'lang', 'source', 'sourceUrl', 'sourceLabel',
         'outlinks', 'tcooutlinks', 'media', 'retweetedTweet', 'renderedContent', 'quotedTweet',
         'inReplyToTweetId', 'inReplyToUser', 'mentionedUsers', 'cashtags')
        for d in myElementDel:
            t.pop(d)
        t['user'] = t['user']['displayname']
        t['place'] = t['place']['fullName']
        t['coordinates'] = [t['coordinates']['longitude'], t['coordinates']['latitude']]
    df = pd.DataFrame(data['tweets'])

    new_tweets = []
    ijoy = []


    # find tweets with the word "joy" in them and create ijoy column
    for tweet in df['content']:
        tweet = tweet.lower()
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        words = tokenizer.tokenize(tweet)

        if 'joy' in words:
            # create an indicator variable ijoy (if joy is in the tweet)
            ijoy.append(1)

        else:
            ijoy.append(0)

        tweet = ' '.join(words)
        new_tweets.append(tweet)



    # create subsets of dataset based on ijoy value
    df['ijoy'] = ijoy
    df_joy = df.query('ijoy == 1')

    ## find code to create non joy sample
    #df_nojoy = df.query('ijoy == 0')
    df_joy.to_csv('Joy-' + str(m[0]) + '-' + str(m[1]) + '.csv', mode = 'w' )
    #df_nojoy.to_csv('NoJoy-' + str(m[0]) + '-' + str(m[1]) + '.csv', mode = 'w' )
