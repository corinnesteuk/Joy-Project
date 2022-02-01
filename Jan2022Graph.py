
import pandas as pd
import json
import matplotlib.pylab as plt


# count total number of tweets for each day in january and store totals in a dictionary
def count_jan_tweets():

    counts = {}

    for day in range(1, 26):

        file = 'L:\Joy/Data/tweets-2022-01-' + str(day) + '.json'
        with open(file, 'r') as f:
            data = json.load(f)

        #df = pd.DataFrame(data['tweets'])
        date_str = '01/' + str(day)
        counts[date_str] = len(data['tweets'][0])


    return counts


daily_counts = count_jan_tweets()



# plot frequency of tweets for each day in january
plt.plot(daily_counts.keys(), daily_counts.values())

# add title and axis names
plt.title('Figure 1: Daily Tweets January 2022')
plt.xlabel('Day')
plt.ylabel('# Tweets')
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.15)

# create points for max and min
jan_max = max(daily_counts, key = daily_counts.get)
jan_min = min(daily_counts, key = daily_counts.get)

plt.plot(jan_max, daily_counts[jan_max], marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
plt.plot(jan_min, daily_counts[jan_min], marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
plt.annotate(f"Maximum = {daily_counts[jan_max]}", (jan_max, daily_counts[jan_max]))
plt.annotate(f"Minimum = {daily_counts[jan_min]}", (jan_min, daily_counts[jan_min]))

plt.savefig('JanuaryTweets.png')