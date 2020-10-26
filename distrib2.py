import datetime
import random
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
from scipy.integrate import  quad
from scipy.special import betainc
from scipy.special import gamma
pos=int(input("enter stock pos:"))
k=pd.read_pickle('/home/sahil/projdir/dailydata.pkl')
k1=k[k.Symbol==k.Symbol.unique()[pos]].iloc[-1000:-500]
#k1['dayret']=1*((k1.Close-k1.Open)/(k1.Open))*100
k1['dayret']=k1.Close-k1.Open
def pdf5(params,*args):
        z,beta,q=params
        x,xmean=args
        #zf = lambda x,beta,q:(1-(1-q)*beta*x**2)**(1/(1-q))
        #z=quad(zf,-np.inf,np.inf,args=(beta,q))[0]
        pd =(1/z)*(1-beta*(1-q)*(x-xmean)**2)**(1/(1-q))
        return -np.sum(np.log(pd))
def pdf2(params,*args):
        beta,q=params
        x,xmean=args
        zf = lambda x,beta,q:(1-(1-q)*beta*x**2)**(1/(1-q))
        z=-quad(zf,-np.inf,np.inf,args=(beta,q))[0]
        pd =(1/z)*(1-beta*(1-q)*(x-xmean)**2)**(1/(1-q))
        return -np.sum(np.log(pd))


def mle(params, *args):
    eps_1, eps_2 = params
    ret_abs = args[0]
    # uniform noise
    ro = (eps_2-1)/eps_1*2
    arg = ret_abs/(ret_abs+ro)
    func = 1/ro*eps_2/(eps_1-1)*(1-betainc(eps_1-1, eps_2+1, arg))
    return -np.sum(np.log(func))
def pdf1(params, *args):

    eps_1, eps_2 = params
    ret_abs = args[0]
    # uniform noise
    ro = (eps_2-1)/eps_1*2
    arg = ret_abs/(ret_abs+ro)
    func = 1/ro*eps_2/(eps_1-1)*(1-betainc(eps_1-1, eps_2+1, arg))
    return -np.sum(np.log(func))  



  
  
res=opt.minimize(pdf1, np.array([1.3, 1.3]), method='SLSQP', args=(k1.dayret/k1.dayret.mean()), bounds = ((1.01,100), (1.01,100)))
