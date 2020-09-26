import datetime
from datetime import date, timedelta
from numpy.lib.stride_tricks import as_strided
import pandas as pd
import numpy as np
from  pathlib import Path
from os import path
import shutil
import os
import pdb
from digfilters import filters
filt = filters()
k = pd.read_pickle('projdir/dailydata.pkl')
k1 = k[k.Symbol==k.Symbol.unique()[5]]
k1['hp'] = filt.highpass2(k1.Close,48)
k1['sig'] =  filt.butterworth2(k1.hp,10)
for i in range(48,len(k1)):
    k2 =k1.iloc[i-48:i]
    sqsum = np.zeros(49)
    cl = k2.sig.values
    sig=cl
    corr = np.zeros(48)
    cos = np.zeros(49)
    sin = np.zeros(49)
    for period in range(10,49):
        comp = period
        for n in range(48):
            cos[period]+=sig[n]*np.cos(2*np.pi/period)/comp
            sin[period]+=sig[n]*np.sin(2*np.pi/period)/comp
        sqsum[period]=cos[period]**2+sin[period]**2
    pwr=sqsum
    #pwr = filt.normalize(pwr,0.995)
    spx=0
    sp=0
    for per in range(10,49):
        spx+=per*pwr[per]
        sp+=pwr[per]
    print(spx/sp)
    

