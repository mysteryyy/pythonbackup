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
from scipy.integrate import quad,dblquad
from pybayes.pdfs import CPdf
#Main.include("try3.jl")
pos=int(input("enter stock pos:"))
k=pd.read_pickle('/home/sahil/projdir/dailydata.pkl')
k1=k[k.Symbol==k.Symbol.unique()[pos]].iloc[1000:1100]
k1['dayret']=1*((k1.Close-k1.Open)/(k1.Open))*100
k1['lowrange']=((k1.Open-k1.Low)/(k1.Open))*100
def optimizer(x):
    def pdf(x,xmean,*args):
        z,beta,q=args
        ser=x
        pd =(1/z)*(1+beta*(q-1)*(x-xmean)**2)**(-1/(q-1))
        return pd
     
    def lnpdf(z,beta,q,x,xmean):
        ser=x
        pd = ser.apply(lambda x:(1/z)*(1+beta*(q-1)*(x-xmean)**2)**(-1/(q-1)))
        logpdf = np.sum(np.log(pd))
        return logpdf
    def crit(params,*args):
        z,beta,q=params
        x,xmean=args
        logpdf=lnpdf(z,beta,q,x,xmean)
        return -logpdf
    res=opt.minimize(crit,[1.11,4.95,1.65],args=(x,x.mean()))
    return res
def pdf(x,xmean,*args):
        z,beta,q=args
        ser=x
        pd = -(1/z)*(1+beta*(q-1)*(x-xmean)**2)**(-1/(q-1))
        return pd
res=optimizer(k1.dayret)
k2=k1[k1.dayret>0]
res1=optimizer(k2.lowrange)
z,beta,q=res.x
z1,beta1,q1=res1.x
val1=str(nolds.dfa(k1.Close)**-1)
lim=int(input("enter limits: "))
def pdfret(x,xm,sl,z,beta,q):
    global lim
    return -(1/z)*(1+beta*(q-1)*(x-xm)**2)**(-1/(q-1))
l=quad(lambda x:pdfret(x,k1.dayret.mean(),-0.3,z,beta,q),-lim,lim)[0]
def scaledpdfret(x,t,xm,sl,z,beta,q):
    global k1
    val1=1/(nolds.dfa(k1.Close))
    return -(1/z)*(1+beta*(q-1)*(x/(t**val1)-xm/(t**val1))**2)**(-1/(q-1))
def stoploss(x,xm,sl,z,beta,q,k1):
   global val1
   val2=np.float(val1)
   sl1 = quad(lambda x:pdfret(x,xm,sl,z,beta,q),-lim,sl)[0] 
   sl2=dblquad(lambda x,t:pdfret(x*t**val2,xm*t**val2,sl,z,beta,q)/l,-lim
           ,sl,lambda t:1,lambda t:np.inf)[0]

   return quad(lambda x:x*pdfret(x,xm,sl,*res.x),sl,lim)[0]/l+sl*sl2
vals = [stoploss(k1.dayret.values,k1.dayret.mean(),i,z,beta,q,k1) for i in np.arange(-10.5,0,0.1)]
print(vals)
res = optimizer(k1.dayret)     
pd1 = pdf(k1.dayret,k1.dayret.mean(),*res.x)
pd2 = pdf(k1.lowrange,k1.lowrange.mean(),*res1.x)
df=pd.DataFrame()
df2=pd.DataFrame()
df['returns']=k1.dayret
df2['lowrange']=k2.lowrange
df['prob2']=pd2
df2['prob2']=pd2
df['prob']=pd1
df['prob1']=norm().pdf(df.returns)
df = df.sort_values(by='returns')
fig=plt1.figure()
ax1=fig.add_subplot(211)
ax1.plot(np.arange(-10.5,0,0.1),vals)
ax2=fig.add_subplot(212)
ax2.plot(df.returns,df.prob)
plt1.show()

