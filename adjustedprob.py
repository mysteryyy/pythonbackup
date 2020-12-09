import scipy
import matplotlib.pyplot as plt
import vegas
from scipy.integrate import nquad
from scipy.stats import t,norm
from scipy.special import gamma
from scipy.integrate import dblquad,tplquad,quad
import numpy as np
from numpy.random import normal,uniform
al=.62
nu=6.52
s=1.72
u=0.02
lim=20
def t_dist(x,nu,s):

   return ((s**-1)*gamma((nu+1)/2)/((nu**.5)*np.pi**.5*gamma(nu/2)))*(1+(x/s)**2/nu)**(-(nu+1)/2)

def slprobcalc(sl,al,t1):
    slprob= quad(lambda x:(t1**(al))*t_dist((x-u)*(t1**(al)),nu,s),-lim,sl)[0]
    print(slprob)
    print(str(t1) + " done")
    return slprob

scaledprobs = [slprobcalc(-4,.6,i) for i in range(1,300)]
print(dblquad(lambda x,t1:(t1**(al))*t_dist((x-u)*(t1**(al)),nu,s),-lim,-4,lambda t1:1,lambda t1:30)[1])

#plt.plot(scaledprobs)
#plt.show()
