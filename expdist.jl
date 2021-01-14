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
file_dir="/home/sahil/pythonbackup"
k = pd.read_pickle(string(file_dir,"/todays_stock1.pkl"))
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


k = pd_to_df(k)
ret=k.retlog
train_len=Int(round(.5*length(ret)))
train=ret[1:train_len]
test=ret[train_len:Int(round(0.8*end))]
data =copy(train)
l=length(data)
mu=zeros(l+1)
alpha=zeros(l+1)
beta=zeros(l+1)
delta=zeros(l+1)
scale=zeros(l+1)
var=zeros(l+1)
skew=zeros(l+1)
kurt=zeros(l+1)
lamscale=.94
lamalpha=.94
lambeta=.94
loglike=0
for (i,j) in enumerate(data)
	var[i+1]=lamscale*var[i]+(1-lamscale)*j^2
        v=var[i+1] 
	skew[i+1]=(lamscale*skew[i]+(1-lamscale)*j^3)/(var[i+1]^(1.5))
	s = skew[i+1]
	kurt[i+1]=(lamscale*skew[i]+(1-lamscale)*j^4)/(var[i+1]^(2.))
	k=kurt[i+1]
	beta[i]=skew[i+1]*(var[i+1]^.5)*kurt[i+1]^2*3^-1
	sigma=3/(5*3^.5*kurt[i+1]-5*skew[i+1]^2)
	delta[i] = var[i+1]*sigma^3/(beta[i]^2*sigma^2)
	mu[i]=beta*delta[i]*sigma^-1
	alpha[i]=(sigma^2+beta[i]^2)^.5
	loglike=loglike+nigpdf2(alpha[i],beta[i],mu[i],delta[i])

end


