from datetime import date
class dates:
    allDates = []
    def __init__(self):
        currYear = False
        for i in range(5):
            year = 2016 + i
            currYear = year == 2020
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
                    self.allDates.append(str(d))
    def getDates(self):
        return self.allDates
