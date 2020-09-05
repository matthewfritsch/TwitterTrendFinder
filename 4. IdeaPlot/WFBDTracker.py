from dbgetter import dbgetter
from WFBD import WFBD
from string import punctuation

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

        removed = ['the', 'day', 'for', 'and', 'you']
        found = []
        for i in range(self.quantity):
            temp = wordTable[0]
            for entry in wordTable:
                if entry.get('freq') > temp.get('freq') and entry not in found and entry.get('word') not in removed and len(entry.get('word')) > 2:
                    temp = entry
            self.wflist.append(WFBD(temp.get('word'), temp.get('freq')))
            self.wflist[-1].addDates(temp.get('dates'))
            found.append(temp)
                
    def getFreqs(self):
        return self.wflist