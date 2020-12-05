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
#Main.include("try3.jl")
pos=int(input("enter stock pos: "))
lb = int(input("enter no of returns: "))
k=pd.read_pickle('/home/sahil/projdir/dailydata.pkl')
k1=k[k.Symbol==k.Symbol.unique()[pos]].iloc[-lb:]
k1['dayret'] = np.log(k1.Close/k1.Open)
#k1['dayret']=-1*((k1.Close-k1.Open)/(k1.Open))*100
k1['lowrange']=((k1.Open-k1.Low)/(k1.Open))*100
def optimizer(x):
    def pdf(x,*args):
        xmean,beta,q=args
        ser=x
        cq=(2*(np.pi**.5)*gamma(1/(q-1)))/((3-q)*((1-q)**.5)*gamma((3-q)/(2-2*q)))
        pd =(beta**0.5/cq)*(1-beta*(1-q)*(x-xmean)**2)**(1/(1-q))
        return pd
     
    def lnpdf(xmean,beta,q,x):
        ser=x
        pd = ser.apply(lambda x:pdf(x,xmean,beta,q))
        logpdf = np.sum(np.log(pd))
        return logpdf
    def crit(params,*args):
        xmean,beta,q=params
        x=args[0]
        logpdf=lnpdf(xmean,beta,q,x)
        return -logpdf
    res=opt.minimize(crit,[0,5,1.65],args=(x,))
    return res
def pdf(x,xmean,*args):
        z,beta,q=args
        ser=x
        pd = -(1/z)*(1+beta*(q-1)*(x-xmean)**2)**(-1/(q-1))
        return pd
def pdf1(params,*args):
        z,beta,q=params
        x,xmean=args
        #zf = lambda x,beta,q:(1-(1-q)*beta*x**2)**(1/(1-q))
        #z=quad(zf,-np.inf,np.inf,args=(beta,q))[0]
        pd =(1/z)*(1-beta*(1-q)*(x-xmean)**2)**(1/(1-q))
        return -np.sum(np.log(pd))
res=optimizer(k1.dayret)
#res=opt.minimize(pdf1,[1.1,5, 2.95],args=(k1.dayret,k1.dayret.mean()))
k2=k1[k1.dayret>0]
z,beta,q=res.x[0],res.x[1],res.x[2]
lim=int(input("enter limits: "))
def pdfret(x,xm,t,sl,z,beta,q):

    val2=np.float(1/nolds.dfa(k1.Close))
    global lim
    return -(1/z)*(t**val2)*(1+beta*(q-1)*((x-xm)*(t**val2))**2)**(-1/(q-1))
l=quad(lambda x:pdfret(x,k1.dayret.mean(),1,-0.3,z,beta,q),-lim,lim)[0]
def scaledpdfret(x,t,xm,sl,z,beta,q):
    global k1
    val1=1/(nolds.dfa(k1.Close))
    return -(1/z)*(1+beta*(q-1)*(x/(t**val1)-xm/(t**val1))**2)**(-1/(q-1))
def stoploss(x,xm,sl,z,beta,q,k1):
   #sl1 = quad(lambda x:pdfret(x,xm,t,sl,z,beta,q),-lim,sl)[0] 
   sl2=dblquad(lambda x,t:pdfret(x,xm,t,sl,z,beta,q)/l,-lim
           ,sl,lambda t:1,lambda t:np.inf)[0]

   return quad(lambda x:x*pdfret(x,xm,sl,*res.x),sl,lim)[0]/l+sl*sl2
vals = [stoploss(k1.dayret.values,k1.dayret.mean(),i,z,beta,q,k1) for i in np.arange(-10.5,0,0.1)]
print(vals)
res = optimizer(k1.dayret)     
pd1 = pdf(k1.dayret,k1.dayret.mean(),*res.x)
#pd2 = pdf(k1.lowrange,k1.lowrange.mean(),*res1.x)
df=pd.DataFrame()
df2=pd.DataFrame()
df['returns']=k1.dayret
df2['lowrange']=k2.lowrange
#df['prob2']=pd2
#df2['prob2']=pd2
df['prob']=pd1
df['prob1']=norm().pdf(df.returns)
df = df.sort_values(by='returns')
fig=plt1.figure()
ax1=fig.add_subplot(211)
ax1.plot(np.arange(-10.5,0,0.1),vals)
ax2=fig.add_subplot(212)
ax2.plot(df.returns,df.prob)
plt1.show()

