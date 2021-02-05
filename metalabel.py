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
k1=investpy.search_quotes(text='AARTIIND',products=['stocks'],countries=['India'],n_results=2)[0].retrieve_historical_data(from_date='01/01/2014',to_date='07/12/2020')
#k1=investpy.search_quotes(text='AARTIIND',products=['stocks'],countries=['India'],n_results=2)[0].retrieve_historical_data(from_date='01/01/2019',to_date='07/12/2020')

k2=investpy.search_quotes(text='VIX',products=['indices'],countries=['India'],n_results=2)[0].retrieve_historical_data(from_date='01/01/2014',to_date='07/12/2020')
def slret(o,h,l,c,sl):
    hp = ((h-o)/o)*100
    if -hp<sl:
      return sl
    else:
      return(((o-c)/o)*100)
print(k2.columns)
k1 = pd.concat([k1,k2['Close']],join='inner')
k1['rets'] = k1.apply(lambda x:slret(x['Open'],x['High'],x['Low'],x['Close'],-1.0),axis=1)


