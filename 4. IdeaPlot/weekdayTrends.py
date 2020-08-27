import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from WeekdayFreqTracker import WeekdayFreqTracker
from WeekdayFreq import WeekdayFreq

wdf = WeekdayFreqTracker()
weekdayfreqs = wdf.get_weekday_freqs()
weekdayfreqs = sorted(weekdayfreqs, key=lambda WeekdayFreq: WeekdayFreq.freq, reverse=True)

allDates = wdf.getAllDates()

quantity = 5

trends = [w.trend for w in weekdayfreqs[:quantity]]
trendFreqs = [w.freq for w in weekdayfreqs[:quantity]]
dateLists = [w.qtrs for w in weekdayfreqs[:quantity]]


#x: dates in quarters 
#y: frequency

x = [str(num) for num in sorted(list(range(2016, 2021))*4)]
x_vals = []
for i in range(len(x)):
    m = i%4
    x_vals.append(x[i] + 'q' + str(m+1))
x_vals.remove('2020q4')
x_vals.remove('2016q1')
x_vals = np.array(x_vals)
fig_1 = plt.figure(figsize=(16,9), dpi=100)
axes_1 = fig_1.add_axes([0.1, 0.1, 0.9, 0.9])
axes_1.set_ylabel('Trend Popularity')

for i in range(len(trendFreqs)):
    tf = trendFreqs[i]
    ql = dateLists[i]
    t = trends[i]
    y_vals = np.array(list(ql.values())[1:-1])
    axes_1.plot(x_vals, y_vals, label=t, linestyle='--', marker='o')

axes_1.legend(loc=0)
axes_1.set_title('Weekday Trend Frequency By Quarter')
plt.show()



