from pageReader import pageReader
from dates import dates
from time import sleep, time
from random import choice
from trenddb import trenddb

dateRetriever = dates()
sleep(5)

trendtracker = trenddb()

pr = pageReader()

with open('website.txt', 'r') as f:
    site = f.readline()

date = dateRetriever.getRandomDate()
print("Retrieving...")
while date is not None:
    print(date)
    a = time()
    URL = site + 'trend/' + date + '.html'
    trendtracker.add(pr.crawl(URL), date)
    b = time()
    sleep(12 - (b-a))
    date = dateRetriever.getRandomDate()

print("All done!")