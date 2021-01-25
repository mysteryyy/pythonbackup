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
investpy = pyimport("investpy")
function pd_to_df(df_pd)
    df= DataFrame()
    for col in df_pd.columns
        df[!, col] = getproperty(df_pd, col).values
    end
    df
end

function get_data(name,prod,start_date,end_date)
     k1=investpy.search_quotes(text=name,products=[prod],countries=["India"]
     ,n_results=2)[1].retrieve_historical_data(from_date=start_date,to_date=end_date)
     k1 = pd_to_df(k1)
     return k1
end

mutable struct ParticleFilter{T<:Number}
	step_size::T
	mean_mu::T
	mean_sd::T
end

function get_resample_indices(weights)
	n1 = length(weights)
	cum_weights=cumsum(weights)
	u = zeros(n1)
	fuzz =rand(Uniform(0,1),1)[1]
	for i in 1:n1
		u[i] = (i-1+fuzz)/n1
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

function likelihood(pf :: ParticleFilter,x,vol)
	mean_mu=pf.mean_mu
	mean_sd=pf.mean_sd
	sd=exp(vol)
	prob=0
	for i in rand(Normal(mean_mu,mean_sd),1000)
	    prob = prob + pdf(Normal(i,sd),x)/1000
	end
	return prob
end

function gen_sample(w,x)
  ind=get_resample_indices(w)
  w = w[ind]
  w =w/sum(w)
  x = x[ind]
  return w,x
end
function update_sample(pf :: ParticleFilter,w,samps,val)
	step_size=pf.step_size
	for (i,j) in enumerate(samps)
		old_samp=j
		new_samp = rand(Normal(old_samp,step_size),1)[1]
		weight = likelihood(val,new_samp)
		w[i] = weight
		samps[i] = new_samp
	end	
	w = w/sum(w)
	w,samps=gen_sample(w,samps)
	return w,samps
end

step_size=0.05
vol_mean = 0.6
vol_sd=0.24
mean_mu = -.2
mean_sd=.1
k1.dayret=(k1.Close./k1.Open .- 1)*100
ret=k1.dayret
w=zeros(1000)
vols=zeros(length(ret))
samps=rand(Normal(vol_mean,vol_sd),1000)





