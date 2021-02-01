import pandas as pd
import numpy as np
import os
import h5py 

def qcalc(tr,marg,open,w,r1=4000):
      global tq  
      q = round((2*w*r1)/(abs(tr)*open))
      print(q)
      tq+= (q*open)*marg
      if(tq>r1):
            q = 0
      return q


f = h5py.File("stocksdata.hdf5",'r')
c=0
stocks=[]
for i in f.keys():
    g=f[i]
    mean_mu=g['mean_mu'][()]
    beta_rhat=g['beta_step_rhat'][()]
    alpha_rhat=g['alpha_step_rhat'][()]
    if(mean_mu<0 and beta_rhat<1.20 and alpha_rhat<1.2):
        stocks.append(i)
        c=c+1
print(c)

def cov_ab(beta_b,beta_a,var_b):
    return (beta_b*var_b)/beta_a

nstocks = len(stocks)
cov = np.zeros((nstocks,nstocks))
