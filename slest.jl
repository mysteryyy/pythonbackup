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

function nigpdf1(alpha,beta,mean,scale,x)
          extra = (alpha^2-beta^2)^.5
          num = alpha*scale*besselk(1,alpha*(scale^2 + (x-mean)^2)^.5)*exp(extra*scale+beta*(x-mean))
          den = pi*(scale^2 + (x-mean)^2)^.5
          pdf = num/den
	  return pdf
end

function likelihood(x,vol)
	mean_mu=pf.mean_mu
	mean_sd=pf.mean_sd
	sd=exp(vol)
	prob=0
	for i in rand(Normal(mean_mu,mean_sd),1000)
	    prob = prob + pdf(Normal(i,sd),x)/1000
	end
	return prob
end

function limutilcheck(sl,tp,lim)
   global nig
   slval = -sl*quadgk(x->pdf(nig,x),sl,lim)[1]
   tpval = tp*quadgk(x->pdf(nig,x),-lim,tp)[1]
   nolim = quadgk(x->-x*pdf(nig,x),tp,sl)[1]
   return slval+tpval+nolim
end

function limutil(sl,tp,lim)
   global nig
   slval = sl*quadgk(x->pdf(nig,-x),-lim,sl)[1]
   tpval = tp*quadgk(x->pdf(nig,-x),tp,lim)[1]
   nolim = quadgk(x->-x*pdf(nig,-x),sl,tp)[1]
   return slval+tpval+nolim
end

function slutil(sl,lim,nig)
   slval = sl*quadgk(x->pdf(nig,x),-sl,lim)[1]
   nolim = quadgk(x->-x*pdf(nig,x),-lim,-sl)[1]
   return slval+nolim
end

function optsl(nig2)
	diffs=Float64[]
	lim=10
	sl = [i for i in -1:.1:-.1]
	vals=Float64[]

	for i in sl
	    p = slutil(i,lim,nig2)
	    append!(vals,p)
	    diff = abs(p-abs(i))
	    append!(diffs,diff)
	end
	ind = findall(x->x==minimum(diffs),diffs)
	return sl[ind]
end
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
for i in keys(f)
        sym=i
	vars = read(f,join([sym,"/samples"]))
	w = read(f,join([sym,"/weights"]))
	mean_mu = read(f,join([sym,"/mean_mu"]))
	mean_sd = read(f,join([sym,"/mean_sd"]))
	w = w/sum(w)
	w,vars=gen_sample(w,vars)
	mean1 = rand(Normal(mean_mu,mean_sd),length(vars))
	try
	global nig1=calc_dist(vars,w,mean_mu,mean1)
	print(nig1)
        catch e
	println(join([i," ",e]))
	continue
        end
	sl = optsl(nig1)
	println(join([i," ",sl[1]]))
end
close(f)
