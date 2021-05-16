import datetime
import random
import nolds
from datetime import date, timedelta
from numpy.lib.stride_tricks import as_strided
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt1
from scipy.stats import norm
import pandas as pd
import numpy as np
from  pathlib import Path
from os import path
import shutil
import os
import pdb
from mle import *

pr = pd.DataFrame(columns=["open","high","low","close","signal",],data=np.ones((20,4)))
pr.loc[14,'open']=1.00
pr.loc[14,'low']=1.00
pr.loc[14,'close']=1.01
pr.loc[14,'high']=1.01
pr.loc[15,'open']=1.01
pr.loc[15,'close']=1.021
pr.loc[15,'low']=1.01
pr.loc[15,'high']=1.021
pr.loc[17,'low']=0.99
print(pr)
s=0
sl=-1
tp=2
long_short='long'
stopped_out=0
def simulate_trade(pr,long_short):
    pr['oh']=(pr.high-pr.open)/pr.open * 100
    pr['ol']=(pr.low-pr.open)/pr.open * 100
    pr['oc']=(pr.close-pr.open)/pr.open * 100
    print(pr)
    s=0
    for index,row in pr.iloc[0:len(pr)-1].iterrows():
        if(long_short=='long'): 
           if (s+row.oh>tp):
               s=tp
               stopped_out=1
           elif(s+row.ol<sl):
               s=sl
               stopped_out=1
           else:
               s=s+row.oc
        else:
           if (s-row.oh<sl):
               s=sl
           elif(s-row.ol>tp):
               s=tp
           else:
               s=s-row.oc

    return s
def extract_signal_trades(pr):
    k2=pr
    # Index of the signals
    rets=0
    signal_up=k2[k2.signal==1].index.values

    signal_down=k2[k2.signal==-1].index.values
    if((len(signal_up)!=0) & (len(signal_down)!=0)):#Condition for long trade with exit within the day
      signal_up=signal_up[0]

      signal_down=signal_down[0]

      if(signal_up<signal_down):

        rets=simulate_trade(k2.iloc[signal_up+1:signal_down+1],'long')

      else: # Condition for short trade with exit within the day

        rets=simulate_trade(k2.iloc[signal_down+1:signal_up+1],'short')

    elif((len(signal_up)>0) & (len(signal_down)==0)):#Condition for long trade with exit at the end of the day

      signal_up=signal_up[0]
      
      rets=simulate_trade(k2.iloc[signal_up+1:],'long')

    else:# Condition for short trade with exit at the end of the day
      signal_down=signal_down[0]

      rets=simulate_trade(k2.iloc[signal_down+1:],'short')

    return rets

print(extract_signal_trades(pr))
