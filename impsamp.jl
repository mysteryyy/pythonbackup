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

mean1 = Normal(-0.2,.05)
sd = Normal(0.6,0.24)
p=0
for i in rand(Uniform(1,10),1000)
    global p
    mu = rand(mean1,1000)
    for j in mu
	var = rand(sd,1000)
	for k in var
		p = p + pdf(Normal(j,exp(k)),i)/(pdf(mean1,j)*pdf(sd,k))
        end
end
end
print(8*p/1000^3)

