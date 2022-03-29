import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sent = SentimentIntensityAnalyzer()

df = pd.read_csv('Joy-11-2021.csv', index_col = 0)
full_emojis = pd.read_csv('full_emoji.csv', index_col = 0)

emojis = pd.DataFrame(data = [full_emojis['emoji'], full_emojis['name']])
emojis = emojis.T
#print(emojis.head())

polarity = [round(sent.polarity_scores(i)['compound'], 2) for i in df['content']]
df['sentiment_score'] = polarity
print(df.head())
df.to_csv('/Users/corinnesteuk/PycharmProjects/pythonProject/joy_sent.csv')

# polarity = [round(sent.polarity_scores(i)['compound'], 2) for i in emojis['name']]
# emojis['sentiment_score'] = polarity
# print(emojis.head())
# emojis.to_csv('/Users/corinnesteuk/PycharmProjects/pythonProject/all_emoji_sent.csv')