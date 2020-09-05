#import time
class WFBD:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.dates = {}

    def addDate(self, date):
        d = str(date)
        if d in self.dates:
            self.dates[d] += 1
        else:
            self.dates[d] = 1
    
    def addDates(self, dates):
        if dates is None:
            return
        for date in dates:
            self.addDate(date)

    def getDatesSorted(self):
        return sorted(self.dates)

    def getFreqOnDate(self, date):
        if date in self.dates:
            return self.dates[date]
        else:
            return 0

    def getWord(self):
        return self.word

    def __str__(self):
        toRet = self.word + ':'
        for date, freq in self.dates.items():
            toRet += "\n" + str(date) + ":" + str(freq)
        #time.sleep(0.2)
        return toRet