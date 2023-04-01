#world population 
#pip3 install pandas

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

col_count = 3
bar_width = .1

korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)

k1 = plt.bar(index, korea_scores, bar_width, 
             alpha =0.4,
             label = 'Korea')
c1 = plt.bar(index+0.1, canada_scores, bar_width,
             alpha =0.4,
             label = 'Canada')
ch1 = plt.bar(index +0.2, china_scores, bar_width,
              alpha =0.4,
             label = 'China')
f1 = plt.bar(index+0.3, france_scores, bar_width,
              alpha =0.4,
             label = 'France')
plt.ylabel("Mean scire in PISA 2012")
plt.xlabel("Subjects")
plt.title("Test Scores by Country")
plt.xticks(index + 0.3/2, ("Mathematics", "Reading", "Science"))
plt.legend()
plt.grid(True)
plt.show()

