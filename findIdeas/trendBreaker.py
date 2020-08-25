from pydal import DAL, Field
from os import path
from datetime import date
from string import punctuation

db = DAL('sqlite://storage.db', folder=path.join('../database'))
db.define_table('words',
    Field('word', 'string'),
    Field('freq', 'integer'),
    Field('trends', 'list:string'))
try:
    db.define_table('trenddates',
        Field('trend', 'text'),
        Field('date', 'date')
    )
except:
    print("trenddates already exists.")

def splitByWord(trend):
    if trend[0] == '#':
        trend = trend[1:]
    t = [trend.lower()]
    foundDay = []
    daysOfWeek = ['mon', 'tues', 'wednes', 'thurs', 'fri', 'satur', 'sun']
    for day in daysOfWeek:
        if day+'day' in trend:
            t = trend.split(day+'day')
            foundDay.append(day+'day')
    if len(foundDay) > 0:
        for i in range(len(t)):
            word = t[i]
            if len(word) == 0:
                t[i] = foundDay[0]
                foundDay.pop(0)
    canFind = True
    toRet = [] + t
    while canFind:
        canFind = False
        for word in t:
            #print(word)
            biggest = ''
            with open('words_alpha.txt', 'r') as f:
                skip = False
                for line in f:
                    if line.strip('\n') in word and len(line) > len(biggest):
                        biggest = line.strip('\n')
                        #print("Found biggest:", biggest)
                        canFind = True
                if len(biggest) > 2:
                    toRet.remove(word)
                    t.remove(word)
                    bg = word.index(biggest)
                    toRet.append(word[:bg])
                    t.append(word[:bg])
                    toRet.append(word[bg:bg+(len(biggest))])
                    toRet.append(word[bg+len(biggest):])
                    t.append(word[bg+len(biggest):])
                    if len(t[-1]) < 1:
                        t.pop(-1)
                else:
                    canFind = False
    i = 0
    maxIndex = len(toRet)
    while i < maxIndex:
        item = toRet[i]
        if len(item) == 0:
            toRet.remove(item)
            i-=1
        i+=1
        maxIndex = len(toRet)
    return toRet


def parse(trend):
    if ' ' in trend:
        return trend.split()
    if trend.isupper() or trend.islower():
        return splitByWord(trend)
    trends = []
    newtrend = ''
    for i in range(len(trend)):
        letter = trend[i]
        if len(newtrend) == 0 and (letter.isalpha() or letter.isdigit()): #word is empty
            newtrend += letter
        elif letter.isalpha() and newtrend[0].isalpha(): #letter is alpha and word is alpha
            newtrend += letter
        elif letter.isdigit() and newtrend[0].isdigit(): #letter is numeric and word is numeric
            newtrend+= letter
        elif letter.isdigit() or letter.isalpha(): #letter is numeric or alpha, but word is alpha or numeric respectively
            trends.append(newtrend)
            newtrend = letter
        if i == len(trend)-1:
            trends.append(newtrend)
    temptrends = [] + trends
    #print(trends)
    for word in temptrends:
        trends.remove(word)
        #print(word)
        finallen = len(word)
        if word[1:].islower() or word.isupper() or not word.isalpha():
            trends.append(word)
            continue
        lastCap = -1
        for i in range(len(word)):
            letter = word[i]
            #print(letter)
            if i == 0:
                lastCap = 0
                continue
            if letter.isupper():
                trends.append(word[lastCap:i])
                lastCap = i
            if i == finallen-1:
                trends.append(word[lastCap:])
    lastSingle = -1
    i = 0
    maxIndex = len(trends)
    while i < maxIndex:
        word = trends[i]
        if len(word) == 1:
            if lastSingle > -1:
                trends[lastSingle] += word
                trends.remove(word)
                maxIndex -=1
                i-=1
            else:
                lastSingle = i
        else:
            lastSingle = -1
        i+=1
    return trends


        # firstCap = -1
        # onlyCap = -1
        # if word[1:].islower() or word.islower() or word.isupper():
        #     trends.append(word)
        #     continue
        # for i in range(len(word)):
        #     letter = word[i]
        #     #print(letter)
        #     if letter.isupper() and firstCap == -1 and onlyCap == -1: #letter is upper and first in str 
        #         #print("This is the first letter, it's upper")
        #         firstCap = i
        #         onlyCap = i
        #     elif letter.isupper() and firstCap > -1: #letter is upper and not first in a row (shows partway through acronym)
        #         #print("This is upper, but not first in series")
        #         onlyCap = -1
        #     elif letter.isupper() and onlyCap > -1: #letter is upper and arrives after lowers (shows end of a snakecase word)
        #         #print("This is upper and the start of a new word.")
        #         trends.append(word[onlyCap:i])
        #         onlyCap = i
        #         firstCap = i
        #     elif letter.islower() and firstCap == -1 and onlyCap == -1: #letter is lower and first in str 
        #         #print("This is lower, and the first in str")
        #         onlyCap = i
        #     elif letter.islower() and firstCap > -1 and i-firstCap > 1 and word[i-1].isupper(): #letter is lower and previous were upper (shows acronyms)
        #         #print("This is lower, and the end of an acro")
        #         trends.append(word[firstCap:i-1])
        #         onlyCap = i-1
        #         firstCap = -1
                          

count = 0
failed = 0

myWords = []                                                                        
for entry in db(db.trenddates).select().as_list():                                 #get every trend in db
    #print(entry)
    trend = entry.get('trend')                                                          #select the trend as a string
    checkTrend = '' + trend
    for l in trend:
        if l in punctuation:
            checkTrend = checkTrend.replace(l, '')
    if not checkTrend.replace(" ", "").isalnum():                                       #if the trend is not alphanumeric
        db.words.insert(word=trend, freq=1, trends=[])                             #just add it to the db and move on
        failed += 1
        print(trend, "is not alpha or digit")
        continue
    splitTrend = parse(trend)
    
    for word in splitTrend:
        #print(word)
        tempTrends = [] + splitTrend                                                     #make a temporary list of words, but remove the current one
        tempTrends.remove(word)                                                 
        if word in myWords:                                                         #if this word already exists,
            wordEntry = db(db.words.word == word).select(db.words.ALL)[0]           #just update the freq and associated words
            wordEntry.update_record(freq = wordEntry.freq+1)
            wordEntry.update_record(trends = wordEntry.trends + tempTrends)
        else:                                                                       #if the word doesn't already exist
            db.words.insert(word=word, freq=1, trends=list(tempTrends))                   #add it to the new db
            myWords.append(word)
            count += 1


print("Added " + str(count) + " entries.")
print("Failed with " + str(failed) + " entries.")
db.close()
