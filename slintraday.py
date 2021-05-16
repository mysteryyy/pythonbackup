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

pr = pd.DataFrame(columns=["open","high","low","close",],data=np.ones((20,4)))
pr.loc[14,'close']=.99
pr.loc[15,'low']=0.996
pr.loc[15,'close']=0.990
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
               stopped_out=1
           elif(s-row.ol>tp):
               s=tp
               stopped_out=1
           else:
               s=s-row.oc

    return s
 
print(simulate_trade(pr,'long'))
