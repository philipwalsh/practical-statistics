###
### Practical Statistics for Data Sceintists
###


import pandas as pd
from scipy import stats
import numpy as np
import wquantiles


state = pd.read_csv('D:/my-coding/practical-statistics-4-ds-book/data/state.csv')
state_mean = state['Population'].mean()
print ( state_mean )
state_mean_trimmed_01 = stats.trim_mean(state['Population'], 0.1)
print ( state_mean_trimmed_01 )
state_median = state['Population'].median()
print ( state_median )

state_weighted_mean = np.average(state['Murder.Rate'], weights=state['Population'])
print(state_weighted_mean)

state_weighted_median = wquantiles.median(state['Murder.Rate'], weights=state['Population'])
print(state_weighted_median)

## key ideas
## basic metric for location is the mean, but it can be sensaitive to extreme values aka outliers
## other metrics such as median and trimmed mean are less sensitive to outliers and unusal distributions and hence are more robust