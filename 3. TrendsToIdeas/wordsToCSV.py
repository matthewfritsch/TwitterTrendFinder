from pydal import DAL, Field
from os import path
db = DAL('sqlite://storage.db', folder=path.join('../database'))

db.define_table('words', Field('word', 'string'), Field('freq', 'integer'), Field('z', 'list:string'))

with open('words.csv', 'w') as f:
    for entry in db(db.words).select().as_list():
        for i in range(int(entry.get('freq'))):
            f.write(entry.get('word').lower() + ', ')
        f.write('\n')

lines = []
with open('words.csv', 'r') as f:
    for line in f:
        lines.append(line[:-3])

with open('words.csv', 'w') as f:
    for line in lines:
        f.write(line + '\n')
db.close()