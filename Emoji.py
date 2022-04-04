import pandas as pd
df = pd.read_csv('/Users/corinnesteuk/PycharmProjects/pythonProject/EmojiSentiment.csv')

#removing unnecessary columns & first row that was a descriptive row
df = df.drop(0 , axis = 'index')
df = df.drop(['Unnamed: 1','Unicode name', 'Unicode block','Sentiment bar', 'Occurrences', 'Position'] , axis = 1)

#The emotional intensity of an emoji (which will affect valence & dominance) is equal to the absolute value of sentiment.
#This is due to the fact that emojis can have multiple, somtimes very constrasting positive/negative meanings
#and we can not assume this since it is based on the context of the tweet.
df['Sentiment score'] = df['Sentiment score']. astype(float)
df['Emot_Intensity']= abs(df['Sentiment score'])

#convert from 0 to 1 scale --> 0.5 to 1
df['Emot_Intensity'] = (df['Emot_Intensity']/2) + 0.5

df.to_csv('/Users/corinnesteuk/PycharmProjects/pythonProject/EmojiIntensity.csv')