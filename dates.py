from os import path
from datetime import date
from random import randint
class dates:
    
    def __init__(self):
        self.lines = 0
        if not path.exists('datesToFind.txt'):
            f = open('datesToFind.txt', 'a')
            for i in range(5):
                year = 2016 + i
                currYear = year == int(str(date.today())[:4])
                for j in range(1, 13 if not currYear else 1+int(str(date.today())[5:7])):
                    if year == 2016 and j == 1:
                        continue
                    month = j
                    dayCap = 31
                    for k in range(31 if not currYear else 1+int(str(date.today())[8:])):
                        day = k
                        d = 0
                        try:
                            d = date(year, month, day)
                        except ValueError:
                            continue
                        f.write(str(d) + '\n')
                        self.lines += 1
            f.close()
        else:
            self.lines = len(open('datesToFind.txt', 'r').readlines( ))
            print(self.lines)

    def getRandomDate(self):
        if self.lines == 0:
            return None
        date = ''
        allelse = ''
        with open('datesToFind.txt', 'r') as f:
            allelse = f.readlines()
        with open('datesToFind.txt', 'w') as f:
            num = randint(1, self.lines)
            self.lines -= 1
            for line in allelse:
                num-=1
                if not (num == 0):
                   f.write(line)
                else:
                    date = line.strip('\n')
        return date
