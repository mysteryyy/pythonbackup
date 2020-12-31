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
    dayrets=[]

    for _ in range(days):
        sumtot=0
        hit=False
        dayret=0
        for _ in range(720):
         ret = gen_sample_ret(720,1)[0]
         sumtot=sumtot+ret
         if(sumtot<sl):
             dayret=sl
             hit=True
         elif(sumtot>tp):
             dayret=tp
             hit=True
        if(~hit):
            dayret=sumtot
        dayrets.append(dayret)
    return dayrets










        
    print(sum)

