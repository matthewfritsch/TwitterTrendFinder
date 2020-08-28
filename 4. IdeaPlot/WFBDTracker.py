from dbgetter import dbgetter
from WFBD import WFBD

class WFBDTracker:

    def __init__(self, quantity):
        self.wflist = []
        self.quantity = quantity

        self.setupWFList()

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

    def setupWFList(self):
        dbg = dbgetter('words')
        wordTable = dbg.getTable()
        dbg.close()
        for entry in wordTable:
            self.wflist.append(WFBD(entry.get('word'), entry.get('freq')))

    def getFreqs(self):
        dbg = dbgetter('trends')
        trendTable = dbg.getTable()
        dbg.close()

        for wf in self.wflist:                                          #Cycle through every word and frequency in the list of words and frequencies
            for entry in trendTable:                                    #Cycle through every trend and date in the map of trends and dates
                trend = self.remove_punc(entry.get('trend').tolower())  #With the current trend,
                dates = entry.get('dates')                              #and it's associated dates,
                if wf.trend in trend:                                   #if the word we're looking at occurs in this trend,
                    for date in dates:                                  #add all dates to the word's list of dates
                        wf.addDate(date)

        return self.wflist