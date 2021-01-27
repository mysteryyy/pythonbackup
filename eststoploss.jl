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



function gen_sample_ret(sl::StopLoss,period)
	fac = 360/period
	mean_dist=Normal(mean_mu/fac,mean_sd/(fac^.5))
	w,var=gen_sample(sl.weights,sl.var)
        ret=zeros(size)
	for (i,j) in enumerate(var)
	    mean = rand(mean_dist,fac)[1]
            sample_ret=Normal(mean,j)
	    ret[i]=rand(sample_ret,1)[1]
	end
	return ret
end

function sltpval(rets::Array{Float64},sl::Float64,tp::Float64)
	   hit=false 
	   dayret=0
           cumrets=cumsum(rets)
	   o,h,l,c = rets[1],maximum(cumrets),
	   minimum(cumrets),sum(rets)
	   hindex=findall(x->x==h,cumrets)[1]
	   lindex=findall(x->x==l,cumrets)[1]
	   if(hindex<lindex)
	     if(h>tp)
	       dayret=tp
	       hit=true
	     elseif(l<sl)
	       dayret=sl
	       hit=true
	     end
	   else
	     if(l<sl)
	       dayret=sl
	       hit=true
	     elseif(h>tp)
	       dayret=tp
	       hit=true
	     end
	   end
	   if(hit==false)
	      dayret=sum(dayret)
	      	   end
	 return dayret 
end

    
function slutil(sloss::StopLoss,sl,tp,days)
	dayret=Float64[]
	hit=false
	for i in days

	   rets = gen_sample(sloss,.5)
	   	end
        return finaldayret
end








		
           
















