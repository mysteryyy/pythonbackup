import datetime
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
#Main.include("try3.jl")
#pos=int(input("enter stock pos: "))
#lb = int(input("enter no of returns: "))
#k=pd.read_pickle('/home/sahil/projdir/dailydata.pkl')
#k1=k[k.Symbol==k.Symbol.unique()[pos]].iloc[-lb:]
k1=investpy.search_quotes(text='GAYAPROJ',products=['stocks'],countries=['India'],n_results=2)[0].retrieve_historical_data(from_date='01/01/2019',to_date='07/12/2020')
#k1=investpy.search_quotes(text='AARTIIND',products=['stocks'],countries=['India'],n_results=2)[0].retrieve_historical_data(from_date='01/01/2019',to_date='07/12/2020')
k1.to_pickle("todays_stock1.pkl")
#k1 = pd.read_pickle("todays_stock.pkl")
k1['dayret'] = ((k1.Close/k1.Open)-1)*100
#k1['dayret'] = k1.Close.pct_change()*100
k1 = k1.dropna()
k1 = k1.iloc[-300*3:]
#mod =arch_model(k1.dayret,vol='GARCH',p=2,o=2,q=7,dist='StudentsT')
#model = pf.EGARCH(np.array(k1.dayret.dropna()),p=1,q=1)
model = pf.GAS(ar=2, sc=2,data=np.array(k1.dayret.dropna()), family=pf.Skewt())
#model.add_leverage()
result=model.fit(method='BBVI', iterations=500, optimizer='ADAM')
#result=model.fit()
print(result.summary())
