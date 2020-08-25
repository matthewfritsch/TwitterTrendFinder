import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from HashtagFinder import HashtagFinder


htf = HashtagFinder()
hashtagcount = htf.get_date_counts()

x_labels = []
x_vals = []
y_vals = []
i = 0
for key, value in hashtagcount.items():
    x_labels.append(key)
    y_vals.append(value)
    i+=1
    x_vals.append(i)

plt.plot(x_vals, y_vals)
plt.title('Hashtag Frequency over Time')
plt.xlabel('Days since 2016-02-01')
plt.xticks([0, x_vals[-1]], [x_labels[0], x_labels[-1]]) 
plt.ylabel('Frequency')
plt.show()