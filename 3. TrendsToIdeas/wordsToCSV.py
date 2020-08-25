from pydal import DAL, Field
from os import path
db = DAL('sqlite://storage.db', folder=path.join('../database'))

db.define_table('words', Field('word', 'string'), Field('freq', 'integer'), Field('trends', 'list:string'))

with open('words.csv', 'w') as f:
    for entry in db(db.words).select().as_list():
        for i in range(int(entry.get('freq'))):
            f.write(entry.get('word').lower() + ', ')
        f.write('\n')

db.close()