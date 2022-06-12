# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 09:39:09 2022

@author: dmslf
"""

#Shows daily VaR in terms of % loss for a single security for pre-defined confidence level and period of time

import pandas as pd

ticker = input("Ticker: ")
range = int(input("Range: "))
confidence = int(input("Confidence: "))


df = pd.read_csv(ticker+'.txt', index_col="<DATE>", parse_dates=True)

df["Return"] = df['<CLOSE>'].pct_change()


VaR = df['Return'].tail(range).quantile(1-confidence/100)

print("The loss will not exceed "+str(VaR*100)+"% with a "+str(confidence)+"% confidence.")

