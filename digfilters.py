import datetime
from datetime import date, timedelta
from numpy.lib.stride_tricks import as_strided
import pandas as pd
import numpy as np
from  pathlib import Path
from os import path
import shutil
import os
import pdb
class filters:
   
    def __init__(self):
        pass 
    

    def bandpass(self,cl,n):
            #pwr = np.zeros(n)
            bp=np.zeros(len(cl))
            comp=n
            for i in range(2,len(cl)):
              beta1=np.cos(2*np.pi/(0.9*n))
              gamma1=1/(np.cos(2*np.pi*.3/(0.9*n)))
              alpha1=gamma1-(gamma1**2-1)**.5
              bp[i] = .5*(1-alpha1)*(cl[i]-cl[i-2])
              +beta1*(1+alpha1)*bp[i-1]-alpha1*bp[i-2]
            return bp
    def velacc5(self,p):
             k =p.dropna()
             k['hp'] = k.roof
             k = k.dropna()
             k['vel'] = (49/20)*k.hp-(6)*k.hp.shift(1)
             +(15/2)*k.hp.shift(2)-(20/3)*k.hp.shift(3)
             +(15/4)*k.hp.shift(4)-(6/5)*k.hp.shift(5)
             +(1/6)*k.hp.shift(6)
             k['acc']=(4.5112)*k.hp-(17.4)*k.hp.shift(1)
             +(29.25)*k.hp.shift(2)-(28.222)*k.hp.shift(3)
             +(16.5)*k.hp.shift(4)-(5.4)*k.hp.shift(5)
             +(.7612)*k.hp.shift(6)
             k=k.dropna()
             return k
    def ema(self,cl,l):
        em = np.zeros(len(cl))
        alpha = 2/(l+1)
        for i in range(1,len(cl)):
            em[i]=alpha*cl[i]+(1-alpha)*em[i-1]
        return em

    def butterworth2(self,cl,period):
        cl1=cl
        cl = np.zeros(len(cl))
        a = np.exp(-1.414*3.14159/period)
        b = 2*a*np.cos(1.414*(3.14159/2)/period)
        c2 =b
        c3=-a*a
        c1=1-c2-c3
        for i in range(3,len(cl)):
             cl[i] = c1*(cl1[i]+cl1[i-1])/2+c2*cl[i-1]+c3*cl[i-2]
        return cl
    
    def butterworth3(self,cl,period):
        bw = np.zeros(len(cl))
        a = np.exp(-np.pi/period)
        b=2*a*np.cos(1.738*(np.pi/2)/period)
        c=a*a
        d2=b+c
        d3=-(c+b*c)
        d4=c*c
        d1=1-d3-d2-d4
        for i in range(4,len(cl)):
            bw[i] = d1*cl[i]-d2*bw[i-1]-d3*bw[i-2]-d4*bw[i-3]
        return bw 
    def highpass2(self,cl,period):
        hp = np.zeros(len(cl))
        cos_element=np.cos(0.707*2*np.pi/period)
        sin_element=np.sin(0.707*2*np.pi/period)
        alpha = (cos_element+sin_element-1)/cos_element
        print(alpha)
        peak = np.zeros(len(cl))
        for i in range(3,len(cl)):
            hp[i] = (1-alpha/2)**2*(cl[i]-2*cl[i-1]+cl[i-2])+2*(1-alpha)*hp[i-1]-(1-alpha)**2*hp[i-2]
        return hp
    def highpass1(self,cl,period):
        hp = np.zeros(len(cl))
        cos_element=np.cos(2*np.pi/period)
        sin_element=np.sin(2*np.pi/period)
        alpha = (1-sin_element)/cos_element
        for i in range(1,len(cl)):
            hp[i] = .5*(1+alpha)*(cl[i]-cl[i-1])+alpha*(hp[i-1])
        print(alpha)
        return hp
  
    def normalize(self,filt,fac):
        peak = np.zeros(len(filt))
        for i in range(len(filt)):
            peak[i] = peak[i-1]*fac
            if(abs(filt[i])>peak[i]):
                peak[i]=abs(filt[i])
            if(peak[i]>0):
                filt[i]=filt[i]/peak[i]
        return filt

    
