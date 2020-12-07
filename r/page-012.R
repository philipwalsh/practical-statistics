###
### Practical Statistics for Data Sceintists
###


state <- read.csv("D:/my-coding/practical-statistics-4-ds-book/data/state.csv")
state
state.mean<-mean(state[['Population']])
state.mean
state.mean.trimmed_1<-mean(state[['Population']], trim=0.1)
state.mean.trimmed_1
state.median=median(state[['Population']])
state.median



