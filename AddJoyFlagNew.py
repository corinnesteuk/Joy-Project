import pandas as pd
import json
import nltk


# add a column to the dataframe to indicate if a tweet includes the word joy

months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    months.append([month, year])

for m in months:
    file = 'tweets-' + str(month[0]) + '-' + str(month[1]) + '.json'

    with open(file, 'r') as f:
        data = json.load(f)

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

    df['ijoy'] = ijoy
    df_joy = df.query('ijoy == 1')
    df_joy.to_csv(str(m[0]) + '-' + str(m[1]) + '.csv', mode = 'w' )
