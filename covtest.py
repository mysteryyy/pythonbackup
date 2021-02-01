import pandas as pd
import numpy as np
import os
import h5py 
f = h5py.File("stocksdata.hdf5",'r')
c=0
for i in f.keys():
    g=f[i]
    mean_mu=g['mean_mu'][()]
    beta_rhat=g['beta_step_rhat'][()]
    alpha_rhat=g['alpha_step_rhat'][()]
    if(mean_mu<0 and beta_rhat<1.2 and alpha_rhat<1.2):
        print(i)
        c=c+1
print(c)
