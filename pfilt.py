import random
from  matplotlib import pyplot as plt1
from scipy.stats import norm
import investpy
import pandas as pd
import numpy as np
from  pathlib import Path
from os import path
import shutil
import os
import pdb
from mle import *
from scipy.stats import norm
#import julia
import scipy.optimize as opt
def get_data(name,prod,start_date,end_date):
     k1=investpy.search_quotes(text=name,products=[prod],countries=['India']
     ,n_results=2)[0].retrieve_historical_data(from_date=start_date,to_date=end_date)
     stockfile = name+'_'+prod+'.pkl'
     k1.to_pickle(stockfile)
     return k1
     print('stock data downloaded')
    # stockfile= stock_name + 'stockdata.pkl'
# k1 = pd.read_pickle(stockfile)
k1=get_data('GAIL','stocks','10/01/2021','20/01/2021')
k1['dayret'] = ((k1.Close/k1.Open)-1)*100
step_size=0.05
vol_mean = 0.6
vol_sd=0.24
mean_mu = -.2
mean_sd=.1
ret = np.array(k1.dayret)
def likelihood(x,vol):
    sd = np.exp(vol)
    prob=0
    for i in norm.rvs(loc=mean_mu,
    scale=mean_sd,size=1000):
         prob=prob+norm.pdf(x,i,sd)/1000
    return prob
def get_resample_indices(weights):
        n = weights.shape[0]
        cum_weights = np.cumsum(weights)

        u = np.zeros(n)
        fuzz = random.uniform(0,1)
        for i in range(n):
            u[i] = (i + fuzz) / n

        # calculate number of babies for each particle
        baby_indices = np.zeros(n)  # index array: a[i] contains index of
        # original particle that should be at i-th place in new particle array
        j = 0
        for i in range(n):
            while u[i] > cum_weights[j]:
                j += 1
            baby_indices[i] = j
        return baby_indices
##Likelihood Calculation
#w=np.zeros(1000)
#samps=np.zeros(1000)
#for (i,j) in enumerate(norm.rvs(vol_mean,
#vol_sd,size=1000)):
#         w[i]=likelihood(ret[0],j)
#         samps[i]=j
#w = w/np.sum(w)
##
w = np.array([.01,.01,.2,.3])
get_resample_indices(w)
     

