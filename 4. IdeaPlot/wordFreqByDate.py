from WFBDTracker import WFBDTracker
from WFBD import WFBD

wfbdt = WFBDTracker(5)

wordfreqdates = wfbdt.getFreqs()
allDates = []

orderedVals = []

for w in wordfreqdates:
    for date, freq in list(w.dates.items()):
        if not date in allDates:
            allDates.append(date)
        
x_vals = sorted(allDates)

fig_1 = plt.figure(figsize=(16,9), dpi=100)
axes_1 = fig_1.add_axes([0.1, 0.1, 0.9, 0.9])
axes_1.set_ylabel('Times Used')
axes_1.set_xlabel('Date')

for w in wordfreqdates:
    y_vals = w.