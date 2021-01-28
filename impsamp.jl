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

