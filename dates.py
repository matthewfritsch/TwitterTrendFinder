from datetime import date
dates = []
class dates:
    def __init__(self):
        for i in range(5):
            year = 2016 + i
            for j in range(12):
                month = j
                for k in range(31):
                    day = k
                    d = 0
                    try:
                        d = date(year, month, day)
                    except ValueError:
                        continue
    
    def getDates(self):
        return self.dates
