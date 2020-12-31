import matplotlib.pyplot as plt
import pandas as pd
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

def gen_sample_ret(period,size):
    alpha = wald.rvs(loc=alpha_mean,scale=alpha_conc)
    beta = norm.rvs(loc=beta_mean,scale=beta_var)
    scale = np.random.exponential(scale=scale_rate)
    scale=scale/period
    mean = halfnorm.rvs(loc=.1,scale=.08)
    mean = mean/period
    ret = norminvgauss.rvs(alpha,beta,mean,scale,size=size) 
    return ret

def hlc(period):
    rets = gen_sample_ret(period)
    return np.cumsum(rets).max(),np.cumsum(rets).min(),rets.sum()
sum=0
def slutil(sl,tp,days):
    assert sl<0
    assert tp>0

    hit=False
    finaldayret=[]
    for _ in range(days):
        dayret=0
        dayrets=pd.Series(gen_sample_ret(720,720))
        print(dayrets.sum())
        cumsum=np.cumsum(dayrets)
        h = cumsum.max()
        l = cumsum.min()
        if(cumsum[cumsum==h].index<cumsum[cumsum==l].index):
            if(h>tp):
                dayret=tp
                finaldayret.append(dayret)
                hit=True
            elif(l<sl):
                dayret=sl
                finaldayret.append(dayret)
                hit=True
        else:
            if(l<sl):
                dayret=sl
                finaldayret.append(dayret)
                hit=True
            elif(h>tp):
                dayret=tp
                finaldayret.append(dayret)
                hit=True
        if(hit==False):
            dayret=dayrets.sum()
            finaldayret.append(dayret)
        print(hit)
                


    return finaldayret

slutil(-2,4,100)








        

