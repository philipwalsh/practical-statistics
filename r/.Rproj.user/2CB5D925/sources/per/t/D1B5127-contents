###
### Practical Statistics for Data Sceintists
###

library('matrixStats')

state <- read.csv("D:/my-coding/practical-statistics-4-ds-book/data/state.csv")
state
state.mean<-mean(state[['Population']])
state.mean
state.mean.trimmed_1<-mean(state[['Population']], trim=0.1)
state.mean.trimmed_1
state.median=median(state[['Population']])
state.median

state.weighted.mean <- weighted.mean(state[['Murder.Rate']], w=state[['Population']])
state.weighted.mean

state.weighted.median = weightedMedian(state[['Murder.Rate']], w=state[['Population']])
state.weighted.median

## key ideas
## basic metric for location is the mean, but it can be sensaitive to extreme values aka outliers
## other metrics such as median and trimmed mean are less sensitive to outliers and unusal distributions and hence are more robust





