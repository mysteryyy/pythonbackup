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
from bandperiod import bandpassfilt
from hurst import compute_Hc
#k=pd.read_pickle('projdir/dailydata.pkl')
#k1=k[k.Symbol==k.Symbol.unique()[0]]
filt = filters()
bp=bandpassfilt()
def rsi(k):
    k['delta'] = k.roof.diff()
    k['du'] = ((k.delta/abs(k.delta)+1)/2)*k.delta#keeping only the positive k.delta
    k['dd'] = ((abs((k.delta/abs(k.delta))-1)/2))*abs(k.delta)#keeping only the negative delta
    k['rsi14'] = k.du.rolling(window=14).mean()/(k.dd.rolling(window=14).mean()+k.du.rolling(window=14).mean())

    k['rsi20'] = k.du.rolling(window=20).mean()/(k.dd.rolling(window=20).mean()+k.du.rolling(window=20).mean())
    return k
def h(l):
    s = compute_Hc(l)
    return s[0]

def feattrans(k1):
    def dir(x,y):
        if(x>y):
            return -1
        elif(x<y):
            return 1
        else:
            return 0
    k1['ret'] = ((k1.Close-k1.Open)/k1.Open)*100
    k1['targret']=0
    for i in range(5):
        k1['targret']+= k1.ret.shift(-i)
    k1['h'] = k1.Close.rolling(150).apply(h)
    k1['roof'] = filt.butterworth2(filt.highpass2(k1.Close,48),10)
    k1['roof1'] = filt.normalize(k1.roof,0.991)

    k1['ema'] = filt.ema(k1.Close,3)
    k1 = filt.velacc5(k1)
    k1['vel'] = k1.vel/abs(k1.vel)
    k1['acc'] = k1.acc/abs(k1.acc)
    k1['velacc'] = k1[['vel','acc']].apply(lambda x:dir(x.vel,x.acc),axis=1)
    #k1['roof'] = filt.normalize(k1.roof,0.991)
    k1['quad']=k1.roof.diff()
    k1['quad'] = filt.normalize(k1.quad,.991)
    k1['quad'] = filt.butterworth2(k1.quad,10)
    k1['quadlead'] = k1.quad-k1.roof
    #k1['period'] = bp.calcperiod(k1)
    k1=k1.drop('quad',1)
    k1['stoch20'] = (k1.roof-k1.roof.rolling(window=20).min())/(k1.roof.rolling(window=20).max()-k1.roof.rolling(window=20).min())
    k1['stoch14'] = (k1.roof-k1.roof.rolling(window=14).min())/(k1.roof.rolling(window=14).max()-k1.roof.rolling(window=14).min())
    k1=k1.dropna()
    k1['stoch20'] = filt.butterworth2(k1.stoch20,10)
    k1['stoch14'] = filt.butterworth2(k1.stoch14,10)
    k1 = rsi(k1) 
    k1=k1.dropna()
    k1['rsi20'] = filt.butterworth2(k1.rsi20,10)
    k1['rsi14'] = filt.butterworth2(k1.rsi14,10)
    k1['decycle'] = filt.highpass2(k1.Close,60)-filt.highpass2(k1.Close,30)
    k1['sine'] = filt.butterworth2(filt.highpass1(k1.Close,40),10)
    k1['sinpow'] = ((k1.sine)**2).rolling(window=3).mean()
    k1['sine'] = k1.sine.rolling(window=3).mean()/(k1.sinpow)**.5
    k1['bandpass'] = filt.bandpass(k1.roof,18)
    k1['bandpass'] = filt.normalize(k1.bandpass,0.991)
    k1['rms'] =k1.roof.rolling(window=20).std()
    k1['cci'] = (k1.roof-k1.roof.rolling(window=20).mean())/(.015*k1.rms)
    k1=k1.dropna()
    k1['cci'] = filt.butterworth2(k1.cci,10)
    return k1

#########k=pd.concat([feattrans(k[k.Symbol==i]) for i in k.Symbol.unique()])

