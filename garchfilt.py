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
import scipy
k1=investpy.search_quotes(text='GAYAPROJ',products=['stocks'],countries=['India'],n_results=2)[0].retrieve_historical_data(from_date='01/01/2018',to_date='16/12/2018')
if path.exists("/home/sahil/pythonbackup/todays_stock.pkl"):
 os.remove("/home/sahil/pythonbackup/todays_stock.pkl")
else:
 k1.to_pickle("todays_stock.pkl")
 
k1['dayret'] = ((k1.Close/k1.Open)-1)*100
k1['logdayret'] = np.log((k1.Close/k1.Open))*100
#k1['dayret'] = k1.Close.pct_change()*100
k1 = k1.dropna()
print("long term hold ret")
print(((k1.Close[-1]/k1.Open[0])-1)*100)
print("intraday hold ret")
print((((k1.Close/k1.Open)-1)*100).sum())
print("normal ret skew")
print(scipy.stats.skew(k1.dayret))
print("log ret skew")
print(scipy.stats.skew(k1.logdayret))

