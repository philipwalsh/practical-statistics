###
### Practical Statistics for Data Sceintists
###


import pandas as pd
from scipy import stats

state = pd.read_csv('D:/my-coding/practical-statistics-4-ds-book/data/state.csv')
state_mean = state['Population'].mean()
print ( state_mean )
state_mean_trimmed_01 = stats.trim_mean(state['Population'], 0.1)
print ( state_mean_trimmed_01 )
state_median = state['Population'].median()
print ( state_median )

