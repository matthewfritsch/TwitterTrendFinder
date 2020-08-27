class DotwFreq:
    def __init__(self, trend, date):
        self.trend = trend
        self.qtrs = self.setupQtrs()
        self.freq = 0                                   #freq is the overall frequency
        self.addDate(date)

    def setupQtrs(self):
        tempQtrs = {}
        tempRange = [str(q) for q in sorted(list(range(2016,2021))*4)]       #tempRange is just a list of numbers 16-20, with four copies of each number
        for i in range(len(tempRange)):                 #looking through each spot in the list
            m = i%4                                     #m is the remainder of the index/4 (0, 1, 2, 3, 0, 1, 2, 3, etc.)
            tempQtrs[tempRange[i]+ 'q' + str(m+1)] = 0 #the key is the current number in temprange + 'q' + remainder + 1 (16q1, 16q2, etc.) and the value is zero since there are no frequencies yet.
        return tempQtrs

    def addDate(self, newdate):
        nd = str(newdate)
        qtr = nd[:4]
        q1 = ['01', '02', '03']
        q2 = ['04', '05', '06']
        q3 = ['07', '08', '09']
        q4 = ['10', '11', '12']
        if nd[5:7] in q1:
            qtr += 'q1'
        elif nd[5:7] in q2:
            qtr += 'q2'
        elif nd[5:7] in q3:
            qtr += 'q3'
        else:
            qtr += 'q4'

        self.qtrs[qtr] += 1
        self.freq+=1