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
include("/home/sahil/pythonbackup/pfilt.jl")
mutable struct StopLoss{T<:Number}
	var::Vector{T}
	weights::Vector{T}
	mean_mu::T
	mean_sd::T
end



function gen_sample_ret(sl::StopLoss,period,size)
	fac = 360/period
	mean_dist=Normal(mean_mu/fac,mean_sd/(fac**.5))
	mean = rand(mean_dist,size)
	w,var=gen_sample(sl.weights,sl.var)
        ret=zeros(size)
	for (i,j) in enumerate(var)
	    mean = rand(mean_dist,size)[1]
            sample_ret=Normal(mean,j)
	    ret[i]=rand(sample_ret,1)[1]
	end
	return ret
end

    















