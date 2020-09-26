import datetime
import nolds
from datetime import date, timedelta
from numpy.lib.stride_tricks import as_strided
from  matplotlib import pyplot as plt
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
ins=0
gns=0
ins=np.zeros(149)
g=np.zeros(149)
idt=0
gdt=0
k1=.5
k2=.1
k3=.4
k4=0.2
k5=0.1
C=5
for i in range(148):
    if i>=3:
     idt=k1*(g[i-3]**4)/(1+g[i-3]**4)-k2*ins[i]
    if(i<=30):
     gdt = k3/(1+ins[i]**2)-k4*g[i]-g[i]*ins[i]+k5*g[i]
    else:
     gdt = k3/(1+ins[i]**2)-k4*g[i]-g[i]*ins[i]
    ins[i+1]=ins[i]+idt
    g[i+1]=g[i]+gdt
    g[i+1] = 0 if g[i+1]<0 else g[i+1]
fig=plt.figure()
ax1=fig.add_subplot(211)
ax1.plot(g)
ax1.plot(ins)
ax1.legend(['glucose','insulin'])
ax2=fig.add_subplot(212)
ax2.acorr(g[60:],maxlags=10)
plt.show()

