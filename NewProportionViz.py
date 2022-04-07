import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from tabulate import tabulate

total = pd.read_csv("Total-Tweets-Per-Month.csv", header = None)
total = total.dropna(axis = 0)
total = total.reset_index()
total = total.drop(columns = ['index'])
joy = pd.read_csv("Joy-Tweets-Per-Month.csv")
all = total.join(joy, how = 'right')
all = all.drop(columns = ['Unnamed: 0'])

all['freq'] = 10000*(all['Joy Tweets']/all[1])
all = all.set_index(0)
print(all)

plt.bar(all.index, all['freq'], color='black')
plt.xlabel('Month')
plt.ylabel('Proportion of Joy Tweets (x10^-4)')
plt.title('Figure 1: Proportion of Joy Tweets by Month (Bar)')
plt.xticks(rotation=90)
plt.yticks(np.arange(0, 10, step=.5))
plt.grid(axis = 'y',  color = 'grey')
plt.subplots_adjust(left=0.15, bottom=0.2)
plt.savefig('Figure1new.png')
plt.show()



# plot frequency of joy tweets for each month

# add title and axis names
plt.plot(all.index, all['freq'], color='blue', marker='o', markersize = 3)
plt.title('Figure 2: Proportion of Joy Tweets by Month (Line)')
plt.xlabel('Month')
plt.ylabel('Proportion of Joy Tweets (x10^-4)')
plt.grid()
plt.xticks(rotation=90)
plt.yticks(np.arange(3, 10, step=.5))
plt.subplots_adjust(bottom=0.5)
plt.savefig('Figure2new.png')
plt.show()

# write dataframe to file as table
all = all.rename(columns = {1: "Total Tweets", 'freq':"Joy Proportion (x10^-4)"})
table = tabulate(all, headers='keys', tablefmt='psql')

with open('newFigure2-Proportions.txt', 'w') as f:
    f.write(table)


