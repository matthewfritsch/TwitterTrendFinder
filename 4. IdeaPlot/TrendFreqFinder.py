from dbgetter import dbgetter
from string import punctuation
class TrendFreqFinder:
    def __init__(self):
        self.trendfreqs = {}
    
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

    def get_trend_freqs(self):
        mydb = dbgetter('trends')
        allTrends = [str(t) for t in mydb.getInfo('trend')]
        for i in range(len(allTrends)):
            trend = self.remove_punc(allTrends[i].lower())
            if trend in self.trendfreqs:
                self.trendfreqs[trend] += 1
            else:
                self.trendfreqs[trend] = 1
        mydb.close()
        return self.trendfreqs
