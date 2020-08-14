from pageReader import pageReader
from dates import dates
from time import sleep, time

allDates = dates().getDates()

pr = pageReader()
f = open('website.txt', 'r')
site = f.readline()
f.close()
for date in allDates:
    print(date)
    a = time()
    URL = site + 'trend/' + date + '.html'
    print(pr.crawl(URL))
    b = time()
    sleep(12 - (b-a))
    