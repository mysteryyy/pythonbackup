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
class bandpassfilt:
    def __init__(self):
        pass
    
    def calcperiod(self,k1):
        k1['hp'] = filt.highpass2(k1.Close,48)
        k1['sig'] =  filt.butterworth2(k1.hp,10)
        pwr=np.zeros(49)
        def bandpass(cl,n,pwr):
            bp=np.zeros(len(cl))
            comp=n
            for i in range(2,len(cl)):
              beta1=np.cos(2*np.pi/n)
              gamma1=1/(np.cos(2*np.pi*.3/n))
              alpha1=gamma1-(gamma1**2-1)**.5
              bp[i] = .5*(1-alpha1)*(cl[i]-cl[i-2])
              +beta1*(1+alpha1)*bp[i-1]-alpha1*bp[i-2]
            for i in range(n):
                  pwr[n]=pwr[n]+(bp[i]/comp)**2
            return

        #for i in range(100,len(k1)):
            #k2 =k1.iloc[i-100:i]
        def percalc(k2):
            pwr=np.zeros(49)
            print(type(k2))
            for n in range(10,48):
             bandpass(k2,n,pwr)    
            maxpwr=pwr.max()
            spx=0
            sp=0
            for period in range(10,49):
                spx=spx+period*pwr[period]
                sp=sp+pwr[period]
            print(spx/sp)
            return spx/sp
        k1['period'] = k1.sig.rolling(window=150).apply(percalc)
        return k1


            #pwr = filt.normalize(pwr,0.995)
def testscript():
    k1 = pd.read_pickle('projdir/dailydata.pkl')
    k1 = k1[k1.Symbol==k1.Symbol.unique()[0]]
    bp=bandpassfilt()
    k1=bp.calcperiod(k1)
