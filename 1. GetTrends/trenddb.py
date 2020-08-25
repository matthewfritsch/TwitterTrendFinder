from pydal import DAL, Field
from os import path
from datetime import date

class trenddb:
    

    def __init__(self):
        self.db = DAL('sqlite://storage.db', folder=path.join("../database"))
        try:
            self.db.define_table('trenddates',
                Field('trend', 'text'),
                Field('date', 'date')
            )
        except:
            print("Trenddates exists...")    
            if len(self.db(self.db.trenddates).select().as_list()) > 0:
                print("It has entries, somehow.")

    def add(self, trends, trenddate):
        if trends is None:
            return
        f = open('runningTrends.txt', 'a')
        d = date(int(trenddate[:4]), int(trenddate[5:7]), int(trenddate[8:]))
        for t in trends:
            self.db.trenddates.insert(trend=t, date=d)
            f.write(str(d) + ": " + t)
            f.write("\n")
        f.close()


    def addParsed(self, trends, trenddate):
        d = date(int(trenddate[:4]), int(trenddate[5:7]), int(trenddate[8:]))
        for t in trends:
            self.db.trenddates.insert(trend=t, date=d)

    def end(self):
        self.db.close()