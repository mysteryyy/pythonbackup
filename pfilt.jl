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
     ,n_results=2)[0].retrieve_historical_data(from_date=start_date,to_date=end_date)
     k1 = pd_to_df(k1)
     return k1
     print("stock data downloaded")
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

function likelihood(x,vol)
	sd=exp(vol)
	prob=0
	for i in rand(Normal(mean_mu,mean_sd),1000)
	    prob = prob + pdf(Normal(i,sd),x)/1000
	end
	return prob
end

function sample(w,x)
  ind=get_sample_indices(w)
  w = w[ind]
  w =w/sum(w)
  x = x[ind]
  return w,x
step_size=0.05
vol_mean = 0.6
vol_sd=0.24
mean_mu = -.2
mean_sd=.1

