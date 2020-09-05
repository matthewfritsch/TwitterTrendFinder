from pydal import DAL, Field
from os import path
class dbgetter:
    def __init__(self, dbchoice = None):
        self.db = DAL('sqlite://storage.db', folder=path.join('../database'))
        self.hasdb = (not dbchoice == None)
        self.mydb = 0
        if self.hasdb:
            if dbchoice == 'trenddates' or dbchoice == 'trends':
                self.mydb = self.db.define_table('trenddates', Field('trend', 'text'), Field('date', 'date'))
            elif dbchoice == 'words':
                self.mydb = self.db.define_table('words', 
                    Field('word', 'string'), 
                    Field('freq', 'integer'), 
                    Field('dates', 'list:string'))
            else:
                raise NameError("Your options from dbgetter are 'trends' or 'words'.")
        else:
            raise NameError("You must provide a database choice from dbgetter ('trends' or 'words').")

    def getInfo(self, data):
        toRet = []
        dbdata = self.db(self.mydb).select().as_list()
        for d in dbdata:
            toRet.append(d.get(data))
        return toRet

    def getTable(self):
        return self.db(self.mydb).select()
    
    def close(self):
        self.db.close()