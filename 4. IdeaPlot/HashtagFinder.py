from dbgetter import dbgetter
from datetime import date
class HashtagFinder:
    def __init__(self):
        self.datecount = {}
    
    def get_date_counts(self):
        mydb = dbgetter('trends')
        allTrends = [str(t) for t in mydb.getInfo('trend')]
        allDates = [str(d) for d in mydb.getInfo('date')]
        for i in range(len(allTrends)):
            trend = allTrends[i]
            date = allDates[i]
            if '#' in trend:
                if date in self.datecount:
                    self.datecount[date] += 1
                else:
                    self.datecount[date] = 1
        mydb.close()
        return self.datecount
