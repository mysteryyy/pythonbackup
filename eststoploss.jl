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
include("/home/sahil/pythonbackup/pfilt.jl")
@with_kw mutable struct StopLoss{T<:Number}
	var::Vector{T}
	weights::Vector{T}
	mean_mu::T
	mean_sd::T
end



function gen_sample_ret(sl::StopLoss,period)
	fac = 360/period
	fac = Int64(fac)
	size=fac
	mean_dist=Normal(mean_mu/fac,mean_sd/(fac^.5))
	w,var=gen_sample(sl.weights,sl.var)
	ret=zeros(Int64(size))
	for i in 1:fac
	    mean = rand(mean_dist,fac)[1]
	    j = mean(var)
	    sample_ret=Normal(mean,exp(j))
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
	finaldayrets=Float64[]

	mean_mu = sloss.mean_mu
	mean_sd = sloss.mean_sd
	for i in 1:days
           rets = gen_sample_ret(sloss,360)
	   dayret=sltpval(rets,sl,tp)
	   append!(finaldayrets,dayret)
	end
        return finaldayrets
end
vars = rand(Normal(.8,.14),100) 
w = [pdf(Normal(.8,.14),i) for i in vars]
mean_mu=-.2
mean_sd=.07
sloss = StopLoss(var=vars,weights=w,mean_mu=mean_mu,
		mean_sd=mean_sd)
rets = -1*rets
limits=[]
shrp=Float64[]
all_limrets=Float64[]
rets=Float64[]
for i=-1:.1:-.1,j=.5:.1:2
	global limrets=slutil(sloss,i,j,5000)
	#down_sd = std([k for k in limrets if k<0])+.01
	sharpe = mean(limrets)/std(limrets)
	append!(shrp,sharpe)
	push!(limits,(i,j))
	append!(rets,sum(limrets))
end
min1=1000
diff=Float64[]
for (i,j) in enumerate(rets)
	rday = j/length(rets)
	sl = abs(limits[i][1])
        append!(diff,abs(sl-rday))
	#if(diff<min1)
	#    global min1=diff
	#    global ind = i
	#    end
end
limind = findall(x->x==minimum(diff),diff)[1]	
print(limits[limind])







	   





