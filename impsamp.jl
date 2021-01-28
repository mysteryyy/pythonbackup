using SpecialFunctions
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
using HDF5
include("pfilt.jl")
f = h5open("stocksdata.hdf5","r")
vars = read(f,"ZEEL/samples")
w = read(f,"ZEEL/weights")
mean_mu = read(f,"ZEEL/mean_mu")
mean_sd = read(f,"ZEEL/mean_sd")
w = w/sum(w)
w,vars=gen_sample(w,vars)
mean1 = rand(Normal(mean_mu,mean_sd),length(vars))
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
s=0
for i in mean1
	for j in vars
	 global s
	 x=rand(Normal(i,exp(j)),1)[1]
	 s=s+((x-i)/exp(j))^3
	end
end
print(s/(length(vars)^2))
