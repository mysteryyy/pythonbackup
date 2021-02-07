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
#Main.include("try3.jl")
#pos=int(input("enter stock pos: "))
#lb = int(input("enter no of returns: "))
#k=pd.read_pickle('/home/sahil/projdir/dailydata.pkl')
#k1=k[k.Symbol==k.Symbol.unique()[pos]].iloc[-lb:]
k1=investpy.search_quotes(text='AARTIIND',products=['stocks'],countries=['India'],n_results=2)[0].retrieve_historical_data(from_date='01/01/2015',to_date='07/12/2020')
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
k1['rets'] = k1.apply(lambda x:slret(x['Open'],x['High'],x['Low'],x['Close'],-2.0),axis=1)
k2['VIX_Close'] = k2.Close
k1 = pd.concat([k1,k2['VIX_Close']],join='inner',axis=1)
k1['Date'] = [i.date() for i in k1.index]
k1['VIX_Close'] = k1.VIX_Close.shift(1)
k1['VIX_Close_diff'] = ((k1.VIX_Close.shift(1)-k1.VIX_Close.shift(2))/k1.VIX_Close.shift(2))*100
k1 = k1.dropna()
k1 = feats.feattrans(k1)
k1['rsi20_diff'] = k1.rsi20.diff()
k1['rsi14_diff'] = k1.rsi14.diff()
k1['stoch20_diff'] = k1.stoch20.diff()
k1['rets1'] = k1.rets/abs(k1.rets)
k1['rets1'] = (k1.rets1+1)/2
k2 = k1[k1.Date>datetime.date(2018,1,1)]
k1 = k1[k1.Date<datetime.date(2018,1,1)]
k1 = k1.dropna()
feats = ['stoch20','stoch14','rsi14','rsi20','sine','bandpass','cci','decycle','quadlead','velacc','VIX_Close','VIX_Close_diff','h','rsi20_diff','rsi14_diff','stoch20_diff']
feats1= feats
xtrain = np.array(k1[feats1])
ytrain=np.array(k1.rets1)
tr = RandomForestClassifier(n_estimators=3550,max_depth=6,min_samples_split=10)
clf=tr
clf = AdaBoostClassifier(base_estimator=tr,n_estimators=80,random_state=50,learning_rate=1.0)
clf.fit(xtrain,ytrain)
k2['predictions'] =clf.predict(np.array(k2[feats1]))
k2['rand_preds'] = [random.choice([0,1]) for _ in range(len(k2))]
