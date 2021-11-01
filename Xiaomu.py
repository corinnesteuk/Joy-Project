
import datetime
import csv
import subprocess
import snscrape 

# set up scraping and error logs

with open('/Joy Project/Joy_Project_Data/TweetErrors2020-5-12.csv', 'w', newline='') as csvfile:
    errorwriter = csv.writer(csvfile)
    errorwriter.writerow(['Date'])

with open('/Joy Project/Joy_Project_Data/ScrapingLog2020-5-12.csv', 'w', newline='') as csvfile:
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

        command = 'snscrape --jsonl --progress --since ' + str(date) + " twitter-search 'until:" + str(next_day) + ' near:"Chicago"' + "' > /Joy Project/Joy_Project_Data/tweets-" + str(date) + ".json"
        print(command)



        # try scraping a specific day and log whether that date was fully scraped or raised an error
        try:
            subprocess.check_call(command, shell = True)
            
            
            with open('/Joy Project/Joy_Project_Data/ScrapingLog2020-5-12.csv', 'a', newline='') as csvfile:
                errorwriter = csv.writer(csvfile)
                errorwriter.writerow([str(date)])
          
       
        except: 


            with open('/Joy Project/Joy_Project_Data/TweetErrors2020-5-12.csv', 'a', newline='') as csvfile:
                errorwriter = csv.writer(csvfile)
                errorwriter.writerow([str(date)])
        


     
# list out the days in each month for years we are interested in
# delete months from the dictionary after they are fully scraped if the code is interrupted from running
month_days_2020 = {5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}            



# scrape tweets from all days in 2020
for month in month_days_2020.keys():
    scrape_month(2020, month, month_days_2020[month])

