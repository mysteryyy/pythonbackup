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
train_len=Int(round(.7*length(ret)))
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
lamscale=.97
lamalpha=.94
lambeta=.94
loglike=0
for (i,j) in enumerate(data)
	global loglike
	j=j+.0001
	var[i+1]=lamscale*var[i]+(1-lamscale)*j^2
        v=var[i+1] 
	inst_skew = j^3/(v)^1.5
	skew[i+1]=lamscale*skew[i]+(1-lamscale)*inst_skew
	s = skew[i+1]
	inst_kurt = j^4/(v^2)
	kurt[i+1]=lamscale*kurt[i]+(1-lamscale)*inst_kurt
	k=kurt[i+1]
	if(i>100)
	try
		fac1 = k-5/3*(s^2)-3
		fac2 = 3*k-4*(s^2)-9
		mean=3*s*v^.5/(fac2)
		bet=s/(v^.5*fac1) 
		al = fac2^.5/(v^.5*fac1)
		del =(3^1.5*(v*fac1)^.5)/fac2
		alpha[i+1]=al
		beta[i+1]=bet
		scale[i+1]=del
		mu[i+1]=mean
		logd=nigpdf2([alpha[i],beta[i],mu[i],scale[i],j])
		loglike=loglike+logd	
        catch err
		println(err)
		alpha[i]=alpha[i-1]
		beta[i]=beta[i-1]
		scale[i]=scale[i-1]
		mu[i]=mu[i-1]

		loglike=loglike+nigpdf2([alpha[i],beta[i],mu[i],scale[i],j])
       end
       end

end


