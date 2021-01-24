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
function get_resample_indices(weights)
	n1 = length(weights)
	cum_weights=cumsum(weights)
	u = zeros(n1)
	fuzz =rand(Uniform(0,1),1)[1]
	for i in 1:n1
		u[i] = (i+fuzz)/n1
	end
	baby_indices = [0 for i in 1:n1]
	j=1
	for i in 1:n1
		while u[i] > cum_weights[j]
			j += 1
		end
		baby_indices[i] = Int64(j)
	
	end
	return baby_indices
end
