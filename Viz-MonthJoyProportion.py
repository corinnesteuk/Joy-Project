import re
import pandas as pd
import json
import matplotlib.pylab as plt
from prettytable import PrettyTable
import csv


total_tweets = pd.read_csv('Total-Tweets-Per-Month.csv', names= ['Date', 'Total Tweets'])
total_tweets = total_tweets.set_index('Date')
joy_tweets = pd.read_csv('Joy-Tweets-Per-Month.csv', names= ['Date', '# Joy Tweets'])
#joy_tweets = joy_tweets.set_index('Date')
print(joy_tweets)

# #ceates a dictionary with the month as the key and the proportion of joy tweets as the value
# idx = list(range(0, len(joy_counts)))
# for i in idx:
#     freq_joy[list(joy_counts)[i]] = list(joy_counts.values())[i]/list(total_tweets.values())[i]
#
#
#
# # plot frequency of joy tweets for each month
# plt.plot(joy_counts.keys(), freq_joy.values())
#
# # add title and axis names
# plt.title('Figure 1: Proportion of Joy Tweets by Month')
# plt.xlabel('Month')
# plt.ylabel('Proportion of Joy Tweets')
# plt.xticks(rotation=90)
# plt.subplots_adjust(bottom=0.15)
#
# # create points for max and min
# joy_max = max(joy_counts, key=joy_counts.get)
# joy_min = min(joy_counts, key=joy_counts.get)
#
# plt.plot(joy_max, joy_counts[joy_max], marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
# plt.plot(joy_min, joy_counts[joy_min], marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
# plt.annotate(f"Maximum = {joy_counts[joy_max]}", (joy_max, joy_counts[joy_max]))
# plt.annotate(f"Minimum = {joy_counts[joy_min]}", (joy_min, joy_counts[joy_min]))
#
# plt.savefig('Figure1.png')
#
# '''Create Table with Proportion of Joy Tweets Per Month'''
# table = PrettyTable()
#
# table.title = 'Figure 2'
# table.field_names = ['Month', '# Joy Tweets', 'Total # of Tweets', 'Proportion of Joy Tweets']
# for i in idx:
#     table.add_row(list(joy_counts.keys())[i], list(total_tweets.values())[i]), list(freq_joy.values())[i]
# print(table)
#
# table_str = table.get_string()
#
# with open('Figure2-Table.txt', 'w') as f2:
#     f2.write(table_str)