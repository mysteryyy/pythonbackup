using SpecialFunctions
using LinearAlgebra
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
pyimport("scipy.stats")
pd = pyimport("pandas")
file_dir="/home/sahil/pythonbackup"
k1 = pd.read_pickle(string(file_dir,"/todays_stock1.pkl"))
function nigpdf2(params)
	  alpha=params[1]
	  beta=params[2]
	  mean=params[3]
	  scale=params[4]
	  x = params[5]
          extra = (alpha^2-beta^2)^.5
          num = alpha*scale*besselk(1,alpha*(scale^2 + (x-mean)^2)^.5)*exp(extra*scale+beta*(x-mean))
          den = pi*(scale^2 + (x-mean)^2)^.5
          pdf = num/den
	  return log(pdf)
end


function pd_to_df(df_pd)
    df= DataFrame()
    for col in df_pd.columns
        df[!, col] = getproperty(df_pd, col).values
    end
    df
end
function nigpdf2(params)
	  alpha=params[1]
	  beta=params[2]
	  mean=params[3]
	  scale=params[4]
	  x = params[5]
          extra = (alpha^2-beta^2)^.5
          num = alpha*scale*besselk(1,alpha*(scale^2 + (x-mean)^2)^.5)*exp(extra*scale+beta*(x-mean))
          den = pi*(scale^2 + (x-mean)^2)^.5
          pdf = num/den
	  return log(pdf)
end


k1 = pd_to_df(k1)
ret=k1.retlog
train_len=Int(round(.5*length(ret)))
train=ret[1:train_len]
test=ret[train_len:Int(round(0.8*end))]
data =copy(train)
#data=rand(Normal(),1000)
l=length(data)
mu=zeros(l+1)
alpha=zeros(l+1)
beta=zeros(l+1)
delta=zeros(l+1)
scale=zeros(l+1)
var=zeros(l+1)
skew=zeros(l+1)
kurt=zeros(l+1)
function weights(d,w=[1.])
	ind=0
	for i in 2:1:200
		push!(w,-w[end]*(d-i+2)/(i-1))
		if abs(w[i])<0.01
		   ind=i-1
		   break
             end
        end
	return w[1:ind]
end

w=weights(.3)
loglike=0
for (i,j) in enumerate(data)
	global loglike
	lenw = length(w)
	if(i<=lenw)
           continue
	end
	var[i+1]=dot(data[i-lenw+1:i].^2,w)
	v=var[i+1]
	skew[i+1] = dot(data[i-lenw+1:i].^3,w)*(v^-1.5)

	s = skew[i+1]
	kurt[i+1] = dot(data[i-lenw+1:i].^4,w)*(v^-2)

	k = kurt[i+1]
end




