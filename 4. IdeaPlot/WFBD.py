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
    
    def getDatesSorted(self):
        return sorted(self.dates)
