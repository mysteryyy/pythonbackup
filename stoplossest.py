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

def gen_sample_ret():
    alpha = wald.rvs(loc=alpha_mean,scale=alpha_conc)
    beta = norm.rvs(loc=beta_mean,scale=beta_var)
    scale = np.random.exponential(scale=scale_rate)
    mean = halfnorm.rvs(loc=.1,scale=.08)
    ret = norminvgauss.rvs(alpha,beta,mean,scale) 
    return ret
