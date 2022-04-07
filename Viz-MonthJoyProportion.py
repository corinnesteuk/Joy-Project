
import pandas as pd
import matplotlib.pylab as plt
import numpy as np
from tabulate import tabulate



total_tweets = pd.read_csv('Total-Tweets-Per-Month.csv', names= ['Date', 'Total Tweets'])
total_tweets = total_tweets.set_index('Date')
joy_tweets = pd.read_csv('Joy-Tweets-Per-Month.csv')
joy_tweets = joy_tweets.set_index('Unnamed: 0')
joy_tweets = joy_tweets.rename_axis(["Date"])


df = total_tweets.join(joy_tweets)

df['Joy Proportion'] = df['Joy Tweets'] /df['Total Tweets']
print(df)
df = df.reset_index()
plt.bar(df['Date'], df['Joy Proportion'], color='black')
plt.xlabel('Month')
plt.ylabel('Proportion of Joy Tweets')
plt.title('Figure 1: Proportion of Joy Tweets by Month')
plt.xticks(rotation=90)
plt.yticks(np.arange(0, 0.0011, step=0.0001))
plt.subplots_adjust(left=0.15, bottom=0.2)


plt.savefig('Figure1-Proportions.png')



# write dataframe to file as table

table = tabulate(df, headers='keys', tablefmt='psql')

with open('Figure2-Proportions.txt', 'w') as f:
    f.write(table)