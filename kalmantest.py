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
from supervised.automl import AutoML
#Main.include("try3.jl")
#pos=int(input("enter stock pos: "))
#lb = int(input("enter no of returns: "))
#k=pd.read_pickle('/home/sahil/projdir/dailydata.pkl')
#k1=k[k.Symbol==k.Symbol.unique()[pos]].iloc[-lb:]
automl=AutoML(mode='Compete',total_time_limit=600)
def get_stock_data(name):
    k1=investpy.search_quotes(text=name,products=['stocks'],countries=['India'],n_results=2)[0]

    k1 = investpy.get_stock_historical_data(stock=k1.symbol,country='India',from_date='01/01/2015',to_date='20/03/2021')
    return k1

k1 = get_stock_data('AARTIIND')
k2 = get_stock_data('SBIN')
ret1 = (k1.Close-k1.Open)/(k1.Open)
ret2 = (k2.Close-k2.Open)/(k2.Open)

