import pandas as pd
import csv

'''This code counts the number of instances of joy in the monthly tweet files and writes to a CSV'''

# count number of joy tweets for each month and store the indices in a dictionary
def count_joy_tweets(list_months):
    monthly_joy_indicies = {}
    joy_counts = {}

    for month in list_months:

        file = 'L:\Joy/Data/tweets-' + str(month[0]) + '-' + str(month[1]) + '.json'
        with open(file, 'r') as f:
            data = json.load(f)

        df = pd.DataFrame(data['tweets'])

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
        print(month_str)
        month_str = str(month[0]) + '/' + str(month[1])
        joy_counts[month_str] = counter
        monthly_joy_indicies[month_str] = joy_indices
        df['content'] = new_tweets

    return joy_counts, monthly_joy_indicies


# create a list of months to loop through for counting joy tweets
dates = pd.date_range(start='09/01/2019', end='09/30/2021', freq='M')

months = []
for date in dates:
    date = str(date).split('-')
    year = date[0]
    month = date[1]
    months.append([month, year])

# joy_counts, monthly_joy_indicies = count_joy_tweets(months)
# fields = ['Date', 'Number of Joy Tweets']
# new_path = open("Joy-Tweets-Per-Month.csv", "w")
# z = csv.writer(new_path)
# z.writerow(fields)
# for new_k, new_v in joy_counts.items():
#     z.writerow([new_k, new_v])
# new_path.close()

monthly_indices = {'09/2019': [2], '10/2019': [3],'11/2019': [4]}
df_indx = pd.DataFrame(monthly_indices)
df_indx = df_indx._set_axis_name(['Date'])
df_indx = df_indx.T

print(df_indx)
df_indx.to_csv("Joy-Tweets-Per-Month.csv", mode = 'w' )





