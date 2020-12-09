import scipy
import matplotlib.pyplot as plt
import vegas
from scipy.integrate import nquad
from scipy.stats import t,norm
from scipy.special import gamma
from scipy.integrate import dblquad,tplquad,quad
import numpy as np
from numpy.random import normal,uniform
def probs(x,t1,alpha,nu,u,s):
    #x,t1,alpha,nu,u,s=x1[0],x1[1],x1[2],x1[3],x1[4],x1[5]
    return 1*(t1**alpha)*t.pdf((x-u)*(t1**alpha),nu,0,s)*norm.pdf(nu,2.6,1)*norm.pdf(u,-0.1,0.2)*norm.pdf(s,2,.4)
#integ = vegas.Integrator([[-10,-.5],[1,7000],[1.2,1.8],[1,9],[-1,1],[1,4]])
#print(integ(probs,nitn=150,neval=10000))
def pdf1(x,t1,alpha,nu,u,s):
    return (t1**alpha)*t.pdf(x*(t1**alpha),nu,u,s)/(norm.pdf(nu,2.4,1)*norm.pdf(u,-0.1,0.2)*norm.pdf(s,2,.5)*(1/4999)*(1/.6)*(1/10.5))
s=0
l=0
#for i in range(100000):
#    pdf=probs(x:=uniform(-10,-.5),t1:=uniform(1,500),alpha:=uniform(1.2,1.8),nu:=normal(2.4,2),u:=normal(-.1,.5),s:=normal(2,1))/(norm.pdf(nu,2.4,2)*norm.pdf(u,-.1,.5)*norm.pdf(s,2,1))
#    if(~np.isnan(pdf)):
#        l = l+1
#        s = s+pdf
#    else:
#        continue
#    print(s)
#    print(str(i)+" c")
al=.77
nu=2.52
s=1.72
u=0.02
lim=20
def t_dist(x,nu,s):

   return ((s**-1)*gamma((nu+1)/2)/((nu**.5)*np.pi**.5*gamma(nu/2)))*(1+(x/s)**2/nu)**(-(nu+1)/2)

def slprobcalc(sl,al):
    
    slprob= dblquad(lambda x,t1:t_dist((x-u/t1**(1/al)),nu,s/(t1**(1/al))),sl,-lim,lambda t:1,lambda t:500)[0]
    return slprob
def utility(sl):
   slprob= dblquad(lambda x,t1:(t1**(1/al))*t_dist((x-u)*(t1**(1/al)),nu,s),sl,-lim,lambda t:1,lambda t:500)[0]
   #slprob=0
   #for i in range(1000):
   #  al = np.random.uniform(1.2,1.8)
   #  slprob=slprob+slprobcalc(sl,al)
   print(str(sl)+" alpha done")
   #slprob = slprob*.6/1000
   return sl*slprob+(1-slprob)*quad(lambda x:x*t_dist((x-u),nu,s),sl,lim)[0]
slrange = np.arange(-5,-0.1,0.1)
uts = [utility(i) for i in slrange]
plt.plot(slrange,uts)
plt.show()
