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
import pymc3 as pm
from pybayes.pdfs import CPdf,MLinGaussCPdf,GaussPdf,MyEmpPdf
k=pd.read_pickle('/home/sahil/projdir/dailydata.pkl')
k1=k[k.Symbol==k.Symbol.unique()[2]].iloc[1000:1100]
k1['ret']=((k1.Close-k1.Open)/(k1.Close))*100

def pdf(x,xmean,z,beta,q):
        ser=x
        pd =-(1/z)*(1+beta*(q-1)*(x-xmean)**2)**(-1/(q-1))
        return pd
with pm.Model() as model:
    vals = pm.MvNormal('vals',mu=[0,1.38,4.74,2.95],cov=np.identity(4),shape=4)
    xmean = vals[0]
    z = vals[1]
    beta=vals[2] 
    q=vals[3] 
    def pdf(x):
        ser=x
        pd= (1/z)*(1+beta*(q-1)*(x-xmean)**2)**(-1/(q-1))
        return np.log(pd)

    like = pm.DensityDist('like',pdf,observed={'x':k1.ret})

    start = dict{'vals':np.array([0,1.38,4.74,2.95])}
    step = pm.Metropolis()
    trace=pm.sample(1000,step=step,start=start)
