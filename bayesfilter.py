import datetime
import nolds
from datetime import date, timedelta
from numpy.lib.stride_tricks import as_strided
import matplotlib.pyplot as plt
from  matplotlib import pyplot as plt1
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
#from julia.api import Julia
#j=julia.Julia(compiled_modules=False)
#from julia import  Main
import pybayes
from scipy.integrate import quad,dblquad
from pybayes.pdfs import CPdf,MLinGaussCPdf,GaussPdf,MyEmpPdf
k=pd.read_pickle('/home/sahil/projdir/dailydata.pkl')
k1=k[k.Symbol==k.Symbol.unique()[2]].iloc[1000:1030]
k1['ret']=((k1.Close-k1.Open)/(k1.Close))*100
init_param=[0,1.38,4.74,2.95]
a=MLinGaussCPdf(np.identity(4),np.identity(4),np.zeros(4))
init=GaussPdf(np.array(init_param),np.identity(4))


def pdf(x,xmean,*args):
        z,beta,q=args
        ser=x
        pd =(1/z)*(1+beta*(q-1)*(x-xmean)**2)**(-1/(q-1))
        return pd
sample=[init.sample() for _ in range(20)]
w=[]
for i in range(30):
    
    if(i==0):
      
     sample=np.array([init.sample() for _ in range(20)])
     w=[pdf(k1.ret.iloc[i],*j) for j in sample]
     w = np.array(pd.Series(w).fillna(0))
     w=np.array(pd.Series(w).apply(lambda x:0 if x>1 else x))
     w=np.array(pd.Series(w).apply(lambda x:0 if x<0 else x))
     break

     
a1=MyEmpPdf(sample,w)
