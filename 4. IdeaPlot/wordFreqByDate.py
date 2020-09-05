from WFBDTracker import WFBDTracker
from WFBD import WFBD
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

def getAllDates():
    allDates = []
    curDate = str(date.today())
    for i in range(5):
        year = 2016 + i
        currYear = year == int(curDate[:4])
        for j in range(1, 13 if not currYear else 1+int(curDate[5:7])):
            if year == 2016 and j == 1:
                continue
            month = j
            currMonth = currYear and month == int(curDate[5:7])
            for k in range(31 if not currMonth else 1+int(curDate[8:])):
                day = k
                d = 0
                try:
                    if year == 2020 and month >= 8 and day > 13:
                        break
                    allDates.append(str(date(year, month, day)))
                except ValueError:
                    continue
    return allDates


wfbdt = WFBDTracker(10)

wordfreqdates = wfbdt.getFreqs()

x_vals = getAllDates()

x_vals = np.array(sorted(x_vals))
fig_1 = plt.figure(figsize=(16,9), dpi=100)
axes_1 = fig_1.add_axes([0.1, 0.1, 0.9, 0.9])
#set labels here if desired

for w in wordfreqdates:
    x = 0
    y_vals = []
    for date in x_vals:
        x+= w.getFreqOnDate(date)
        y_vals.append(x)
    y_vals = np.array(y_vals)
    axes_1.plot(x_vals, y_vals, label=w.getWord())

x_ticks = [x_vals[0]]
for i in range(len(x_vals)):
    if x_vals[i][-2:] == '01' and int(x_vals[i][5:7])%6 == 0:
        x_ticks.append(x_vals[i])
x_ticks.append(x_vals[-1])
x_labels = [xt[:7] for xt in x_ticks]
plt.style.use('fivethirtyeight')
plt.xticks(x_ticks, labels=x_labels)
axes_1.legend(loc=0)
plt.show()