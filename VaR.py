# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 09:39:09 2022

@author: fusiek
"""

#Shows daily VaR in terms of % loss for a single security for pre-defined confidence level and period of time
#Two simulations are availble - historical and MC

import pandas as pd
import numpy as np

ticker = "mls"
range = 100
confidence = 99


df = pd.read_csv(ticker+'.txt', index_col="<DATE>", parse_dates=True)

df["Return"] = df['<CLOSE>'].pct_change()


VaR_HS = df['Return'].tail(range).quantile(1-confidence/100)

print("The loss will not exceed "+str(round(VaR_HS*100,2))+"% with a "+str(confidence)+"% confidence as per historical simulation.")


a= df['Return'][-range:].to_numpy()
daily_vol = np.std(a)
mean = np.average(a)
vol = np.sqrt(252)*daily_vol

reps = 1000
simulations = np.random.normal(mean,daily_vol,reps)
VaR_MC = np.quantile(simulations,1-confidence/100)


print("The loss will not exceed "+str(round(VaR_MC*100,2))+"% with a "+str(confidence)+"% confidence as per MC simulation.")


