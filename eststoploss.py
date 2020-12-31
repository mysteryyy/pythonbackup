import matplotlib.pyplot as plt
import vegas
from scipy.integrate import nquad
from scipy.stats import t,norm,wald,expon,norminvgauss,halfnorm
from scipy.special import gamma
from scipy.integrate import dblquad,tplquad,quad
import numpy as np
from numpy.random import normal,uniform
samp = np.load('nig.trace/0/samples.npz')
alpha_mean,alpha_conc = wald.fit(samp['alpha'])
beta_mean=samp['beta'].mean()
beta_var=samp['beta'].var()
scale_rate = samp['scale'].mean()

def gen_sample_ret(size):
    alpha = wald.rvs(loc=alpha_mean,scale=alpha_conc)
    beta = norm.rvs(loc=beta_mean,scale=beta_var)
    scale = np.random.exponential(scale=scale_rate)
    scale=scale/720
    mean = halfnorm.rvs(loc=.1,scale=.08)
    mean = mean/720
    ret = norminvgauss.rvs(alpha,beta,mean,scale,size=size) 
    return ret

def ohlc(period):
    sret=0
    max=0
    min=1000
    for _ in range(720):
        ret = gen_sample_ret()
        sret = sret+ret
        sret<

