using SpecialFunctions
using QuadGK
using ForwardDiff
using Optim
using ReverseDiff
#using Ipopt
#using JuMP
#using GLPK
using Distributions
using Zygote
#using Flux
#using Flux.Tracker
#using Flux.Tracker: update!
using PyCall
using DataFrames
using Debugger
using Turing,StatsBase,StatsPlots,MCMCChains
using Parameters
using LinearAlgebra
using HDF5
include("pfilt.jl")
f = h5open("stocksdata.hdf5","r")
function calc_dist(vars,w,mean_mu,mean1)
	s=0
	for i in mean1
		
		for j in vars
		 x=rand(Normal(i,exp(j)),1)[1]
		 s=s+((x-mean_mu)/exp(dot(vars,w)))^3
		end
	end
	k=0
	for i in mean1
		for j in vars
		 x=rand(Normal(i,exp(j)),1)[1]
		 z=(x-mean_mu)/(exp(dot(vars,w)))
		 k = k+z^4
		end
	end

	s=s/(length(vars)^2)
	k=k/(length(vars)^2)
	m=mean_mu
	fac1 = (k-5/3*(s^2)-3)
	fac2 = 3*k-4*(s^2)-9
	v = exp(dot(vars,w)+0.2)
	mean=m-3*s*v^.5/(fac2)
	bet=s/(v^.5*fac1) 
	al = fac2^.5/(v^.5*fac1)
	del =(3^1.5*(v*fac1)^.5)/fac2
	nig1 = NormalInverseGaussian(m,al,bet,del)
	return nig1
end

function limutil(sl,tp,lim)
   global nig
   slval = sl*quadgk(x->pdf(nig,x),-sl,lim)[1]
   tpval = tp*quadgk(x->pdf(nig,x),-lim,-tp)[1]
   nolim = quadgk(x->-x*pdf(nig,x),-tp,-sl)[1]
   return slval+tpval+nolim
end
function limutil_var(sl,tp,lim)
   global nig
   m=mean_mu
   slval = ((sl-m)^2)*quadgk(x->pdf(nig,x),-sl,lim)[1]
   tpval = ((tp-m)^2)*quadgk(x->pdf(nig,x),-lim,-tp)[1]
   nolim = quadgk(x->((x-m)^2)*pdf(nig,x),-tp,-sl)[1]
   return slval+tpval+nolim
end

function slutil(sl,lim,nig)
   slval = sl*quadgk(x->pdf(nig,x),-sl,lim)[1]
   nolim = quadgk(x->-x*pdf(nig,x),-lim,-sl)[1]
   return slval+nolim
end


sym="ADANIPORTS"
vars = read(f,join([sym,"/samples"]))
w = read(f,join([sym,"/weights"]))
mean_mu = read(f,join([sym,"/mean_mu"]))
mean_sd = read(f,join([sym,"/mean_sd"]))
w = w/sum(w)
w,vars=gen_sample(w,vars)
mean1 = rand(Normal(mean_mu,mean_sd),length(vars))
nig = calc_dist(vars,w,mean_mu,mean1)

	
