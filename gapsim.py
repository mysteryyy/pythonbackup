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
#import julia
import scipy.optimize as opt
from julia.api import Julia
#j=julia.Julia(compiled_modules=False)
#from julia import  Man
from scipy.integrate import quad,dblquad
#from pybayes.pdfs import CPdf
from scipy.special import  gamma
from arch import arch_model
import pyflux as pf
import sys
import investpy
from sklearn.ensemble import AdaBoostClassifier,RandomForestClassifier
import feats
from scipy.stats import norminvgauss
#Main.include("try3.jl")
#pos=int(input("enter stock pos: "))
#lb = int(input("enter no of returns: "))
#k=pd.read_pickle('/home/sahil/projdir/dailydata.pkl')
#k1=k[k.Symbol==k.Symbol.unique()[pos]].iloc[-lb:]
k1=investpy.search_quotes(text='AARTIIND',products=['stocks'],countries=['India'],n_results=2)[0].retrieve_historical_data(from_date='01/01/2015',to_date='10/02/2021')
#k1=investpy.search_quotes(text='AARTIIND',products=['stocks'],countries=['India'],n_results=2)[0].retrieve_historical_data(from_date='01/01/2019',to_date='07/12/2020')

k2=investpy.search_quotes(text='VIX',products=['indices'],countries=['India'],n_results=2)[0].retrieve_historical_data(from_date='01/01/2015',to_date='07/12/2020')
def slret(o,h,l,c,sl):
    hp = ((h-o)/o)*100
    if -hp<sl:
      return sl
    else:
      return(((o-c)/o)*100)
print(k2.columns)
#k1 = pd.concat([k1,k2['Close']],join='inner')
k1['rets'] = k1.apply(lambda x:slret(x['Open'],x['High'],x['Low'],x['Close'],-1.0),axis=1)
k2['VIX_Close'] = k2.Close
k1 = pd.concat([k1,k2['VIX_Close']],join='inner',axis=1)
k1['Date'] = [i.date() for i in k1.index]
k1['VIX_Close'] = k1.VIX_Close.shift(1)
k1['VIX_Close_diff'] = ((k1.VIX_Close.shift(1)-k1.VIX_Close.shift(2))/k1.VIX_Close.shift(2))*100
k1 = k1.dropna()
k1 = feats.feattrans(k1)
k1['close_diff'] = (k1.Close.shift(1).diff())/k1.Close.shift(2)*100
#k1['close_diff5'] = ((k1.Close-k1.Close.shift(5))/k1.Close.shift(5))*100
k1['rsi20_diff'] = k1.rsi20.diff()
k1['rsi14_diff'] = k1.rsi14.diff()
k1['stoch20_diff'] = k1.stoch20.diff()
k1['dayret'] = ((k1.Close-k1.Open)/k1.Open)*100
k1['gap'] = (k1.Open-k1.Close.shift(1))/k1.Close.shift(1)
k1 = k1[k1.gap>0]
nig = norminvgauss.fit(k1.dayret)
l = norminvgauss.rvs(nig[0],nig[1],nig[2],nig[3],size=100)
l=k1.dayret
a1=[]
a2=[]
s=2000
for i in l:
    if(i<-2):
      r=2
    elif(i>1):
      r=-1
    else:
      r=-i
    s=s*(1+r/100)
    a2.append(r)
    a1.append(s)
plt.plot(a1)
plt.show()
