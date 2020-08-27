from dbgetter import dbgetter
from DotwFreq import DotwFreq
from string import punctuation
class DotwFreqTracker:
    def __init__(self):
        self.dotwFreqs = []
        self.allDates = 0
    
    def remove_punc(self, s):
        i = 0
        maxIndex = len(s)
        while i < maxIndex:
            let = s[i]
            if let in punctuation:
                let.replace(let, '')
                maxIndex = len(s)
            i+=1
        return s

    def addWDF(self, trend, date):
        for wdf in self.dotwFreqs:
            if wdf.trend == trend:
                wdf.addDate(date)
                return
        self.dotwFreqs.append(DotwFreq(trend, date))
        

    def get_dotw_freqs(self):
        mydb = dbgetter('trends')
        daysOfWeek = ['mon', 'tues', 'wednes', 'thurs', 'fri', 'satur', 'sun']

        allTrends = [str(t) for t in mydb.getInfo('trend')]
        allDates = [str(d) for d in mydb.getInfo('date')]
        self.allDates = [] + allDates
        
        for i in range(len(allTrends)):
            trend = self.remove_punc(allTrends[i].lower())
            date = allDates[i]
            if any(day+'day' in trend for day in daysOfWeek):
                for day in daysOfWeek:
                    if day+'day' in trend:
                        self.addWDF(trend, date)
        mydb.close()
        return self.dotwFreqs


    def getAllDates(self):
        return self.allDates