
import datetime
import csv
import subprocess

# set up scraping and error logs

with open('TweetErrors.csv', 'w', newline='') as csvfile:
    errorwriter = csv.writer(csvfile)
    errorwriter.writerow(['Date'])

with open('ScrapingLog.csv', 'w', newline='') as csvfile:
    scraperwriter = csv.writer(csvfile)
    scraperwriter.writerow(['Days Scraped'])



# scrape twitter for all tweets from chicago in a given month
# input year, month, and number of days in the month
# ex: scrape_month(2020, 1, 31)


def scrape_month(year, month, num_days):


    # scrape one day at a time and output to separate json file
    for i in range(1, num_days + 1):

        date = datetime.date(year, month, i)
        print(date)

        next_day = date + datetime.timedelta(days=1)

        command = 'snscrape --jsonl --progress --since ' + str(date) + " twitter-search 'until:" + str(next_day) + ' near:"Chicago"' + "' > tweets-" + str(date) + ".json"
        print(command)



        # try scraping a specific day and log whether that date was fully scraped or raised an error
        try:
            subprocess.check_call(command, shell = True)
            
            
            with open('ScrapingLog.csv', 'a', newline='') as csvfile:
                errorwriter = csv.writer(csvfile)
                errorwriter.writerow([str(date)])
          
       
        except: 


            with open('TweetErrors.csv', 'a', newline='') as csvfile:
                errorwriter = csv.writer(csvfile)
                errorwriter.writerow([str(date)])
        


     
# list out the days in each month for years we are interested in
month_days_2019 = {9:30, 10: 31, 11: 30, 12: 31}
month_days_2020 = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}            
month_days_2021 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30}



# scrape tweets from all days in last three months of 2019
for month in month_days_2019.keys():
    scrape_month(2019, month, month_days_2019[month])


# scrape tweets from all days in 2020
for month in month_days_2020.keys():
    scrape_month(2020, month, month_days_2020[month])


# scrape tweets from all days in 2021
for month in month_days_2021.keys():
    scrape_month(2021, month, month_days_2021[month])



#snscrape --jsonl --progress --since 2021-10-04 twitter-search 'until:2021-10-05 near:"Chicago"' > tweets-2021-10-04.json
