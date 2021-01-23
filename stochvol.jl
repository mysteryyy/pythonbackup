using SpecialFunctions
using ForwardDiff
using Optim
using ReverseDiff
#using Ipopt
#using JuMP
#using GLPK
using Distributions
using Zygote
using Flux
using Flux.Tracker
using Flux.Tracker: update!
using PyCall
using DataFrames
using Debugger
using Turing,StatsBase,StatsPlots,MCMCChains
#
sp = pyimport("scipy.stats")
pd = pyimport("pandas")
investpy=pyimport("investpy")
k1=investpy.search_quotes(text="GAIL",products=["stocks"],countries=["India"],n_results=2)[1].retrieve_historical_data(from_date="01/01/2015",to_date="07/12/2020")

file_dir="/home/sahil/pythonbackup"
#k = pd.read_pickle(string(file_dir,"/todays_stock1.pkl"))
function pd_to_df(df_pd)
    df= DataFrame()
    for col in df_pd.columns
        df[!, col] = getproperty(df_pd, col).values
    end
    df
end
k = pd_to_df(k1)
k.ret = (k.Close./k.Open .- 1)*100
ret=k.ret
@model normalwalk(x) = begin
	T=length(x)
	step_size ~ Exponential(10)
	sigma = Vector(undef,T)
	mu ~ Uniform(-1,1)
	for i in 2:T
		sigma[i] ~ Normal(sigma[i-1],step_size)
		x[i] ~ Normal(mu,exp(sigma))
	end
end


