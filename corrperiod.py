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
k1 = k[k.Symbol==k.Symbol.unique()[0]]
k1['hp'] = filt.highpass2(k1.Close,48)
k1['sig'] =  filt.butterworth2(k1.hp,10)
pwr=np.zeros(49)
def bandpass(cl,n):
    global pwr
    bp=np.zeros(len(48))
    comp=n
    for i in range(2,48):
      beta1=np.cos(2*np.pi/n)
      gamma1=1/(np.cos(2*np.pi*.3/n))
      alpha1=gamma1-(gamma1**2-1)**.5
      bp[i] = .5*(1-alpha1)*(cl[i]-cl[i-2])
      +beta1*(1+alpha1)*bp[i-1]-alpha1*bp[i-2]
      pwr[n]=0
    for i in range(n):
          pwr[n]=pwr[n]+(bp[i]/comp)**2
    return

for i in range(48,len(k1)):
    k2 =k1.iloc[i-48:i]
    for n in range(10,48):
     bandpass(k2.Close.values,n)    
    maxpwr=pwr.max()
    pwr = pwr/maxpwr
    spx=0
    sp=0
    for period in range(10,49):
        spx=spx+period*pwr[period]
        sp=sp+pwr[period]
    print(spx/sp)

    #pwr = filt.normalize(pwr,0.995)
    spx=0
    sp=0
    for per in range(10,49):
        spx+=per*pwr[per]
        sp+=pwr[per]
    print(spx/sp)
    

