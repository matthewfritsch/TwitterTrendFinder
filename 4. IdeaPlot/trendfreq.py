import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from TrendFreqFinder import TrendFreqFinder

tff = TrendFreqFinder()
tff = tff.get_trend_freqs()
tff = {k: v for k, v in sorted(tff.items(), key=lambda item: item[1], reverse=True)}

x_vals = []
y_vals = []
numberOfVals = 25

for key, value in tff.items():
    print(key, ':', value)
    if numberOfVals <= 0:
        break
    x_vals.append(key)
    y_vals.append(value)
    numberOfVals-=1

x_vals.reverse()
y_vals.reverse()

plt.barh(x_vals, y_vals, color='purple')
plt.title('Trends By Frequency Since 2016-02-01')
#plt.xticks(rotation=90)
# plt.gca().tick_params(axis = 'x', length=20)

plt.xlabel('Frequency Of The Trend')
plt.tight_layout()
plt.show()
    