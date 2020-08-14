from pydal import DAL, Field
from os import path
from datetime import date

class trenddb:
    def __init__(self):
        self.db = DAL('sqlite://storage.db', folder=path.join("./database"))
        self.db.define_table('trenddates',
            Field('trend', 'text'),
            Field('date', 'date')
        )
        self.db.commit()
    
    def add(self, trends, trenddate):
        
        if trends is None:
            return
        
        f = open('runningTrends.txt', 'a')

        d = date(int(trenddate[:4]), int(trenddate[5:7]), int(trenddate[8:]))
        for t in trends:
            self.db.trenddates.insert(trend=t, date=d)
            f.write(str(d) + ": " + t)
        f.close()