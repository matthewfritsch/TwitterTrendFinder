from trenddb import trenddb
class TrendSet:
    def __init__(self):
        self.date = ''
        self.trends = []
    
    def getTrends(self):
        return self.trends

    def getDate(self):
        return self.date

    def add(self, date, trends):
        self.date = date
        self.trends = trends

    def lt(self, other):
        return self.date < other.getDate()

    def __str__(self):
        toRet = self.date
        for t in self.trends:
            toRet += '\n > ' + t
        return toRet

def parseFile():
    trends = []
    lines = []
    with open('runningTrends.txt', 'r') as f:
        lines = f.readlines()
    
    x = 0
    lastDate = 0
    t = 0
    for line in lines:
        x+=1
        currentDate = line[:10]
        if x > 50:
            if not lastDate == currentDate:
                x = 1
                ts = TrendSet()
                ts.add(lastDate, t)
                trends.append(ts)
        if x == 1:
            lastDate = currentDate
            t = []
        if x <= 50 and currentDate == lastDate:
            t.append(line[12:].strip('\n'))
        elif line == lines[-1]:
            ts = TrendSet()
            ts.add(lastDate, t)
            trends.append(ts)
    return trends

t = trenddb()
a = parseFile()
a = sorted(a, key=lambda TrendSet: TrendSet.date)
print(len(a))
with open('runningTrends.txt', 'w') as f:
    for i in a:
        if len(i.getTrends()) != 50:
            print(i.getDate() + " with " + str(len(i.getTrends())))
        for line in i.getTrends():
            f.write(i.getDate() + ': ' + line + '\n')
t.end()