# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 09:39:09 2022

@author: fusiek
"""

#Shows daily VaR in terms of % loss for a single security for pre-defined confidence level and period of time
#Two simulations are availble - historical and MC

import pandas as pd
import numpy as np
import matplotlib as plt

ticker = "mls"
range = 400
confidence = 99


df = pd.read_csv(ticker+'.txt', index_col="<DATE>", parse_dates=True)

df["Return"] = df['<CLOSE>'].pct_change()


VaR_HS = df['Return'].tail(range).quantile(1-confidence/100)
es = []
for i in df['Return']:
    if i < VaR_HS:
        es.append(i)
ES_HS = round(np.mean(es)*100,2)

print("The loss will not exceed "+str(round(VaR_HS*100,2))+"% with a "+str(confidence)+"% confidence as per historical simulation.")
print("Expected Shortfall is "+str(ES_HS)+"%")
#plt.pyplot.hist(df['Return'],bins=20,density=True,alpha=0.7)


a= df['Return'][-range:].to_numpy()
daily_vol = np.std(a)
mean = np.average(a)
vol = np.sqrt(252)*daily_vol

reps = 1000
simulations = np.random.normal(mean,daily_vol,reps)
VaR_MC = np.quantile(simulations,1-confidence/100)
es = []
for i in simulations:
    if i < VaR_MC:
        es.append(i)
ES_MC = round(np.mean(es)*100,2)


print("The loss will not exceed "+str(round(VaR_MC*100,2))+"% with a "+str(confidence)+"% confidence as per MC simulation.")
print("Expected Shortfall is "+str(ES_MC)+"%")
plt.pyplot.hist([simulations,df['Return']],bins=20, density=True,alpha=1,label=['MC',"HS"],align="mid")


