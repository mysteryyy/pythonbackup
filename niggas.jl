using SpecialFunctions
using Distributions
using Zygote
using Flux.Tracker
using Flux.Tracker: update!
using PyCall
using DataFrames
using Debugger

function nigpdf1(x)
          extra = (alpha^2-beta^2)^.5
          num = alpha*scale*besselk(1,alpha*(scale^2 + (x-mean)^2)^.5)*exp(extra*scale+beta*(x-mean))
          den = pi*(scale^2 + (x-mean)^2)^.5
          pdf = num/den
	  return log(pdf)
end

function alpha_grad(alpha,beta,mean,scale,x)
	grad = Tracker.gradient(alpha1->nigpdf1(alpha1,beta,mean,scale),param(alpha))[1]
        return grad
end
function beta_grad(alpha,beta,mean,scale,x)
	grad = Tracker.gradient(beta1->nigpdf1(alpha,beta1,mean,scale),param(beta))[1]
        return grad
end
function scale_grad(alpha,beta,mean,scale,x)
	grad = Tracker.gradient(scale1->nigpdf1(alpha,beta,mean,scale1),param(scale))[1]
        return grad

end


function mean_grad(alpha,beta,mean,scale,x)
	grad = Tracker.gradient(mean1->nigpdf1(alpha,beta,mean1,scale),param(mean))[1]
        return grad

end
sp = pyimport("scipy.stats")
pd = pyimport("pandas")
investpy=pyimport("investpy")
#k1=investpy.search_quotes(text='AARTIIND',products=['stocks'],countries=['India'],n_results=2)[0].retrieve_historical_data(from_date='01/01/2017',to_date='07/12/2020')

file_dir="/home/sahil/pythonbackup"
k = pd.read_pickle(string(file_dir,"/todays_stock1.pkl"))
function pd_to_df(df_pd)
    df= DataFrame()
    for col in df_pd.columns
        df[!, col] = getproperty(df_pd, col).values
    end
    df
end
k = pd_to_df(k)
ret=k.ret
train_len=Int(round(.5*length(ret)))
train=ret[1:train_len]
test=ret[train_len:Int(round(0.8*end))]
params = sp.norminvgauss.fit(train)
alpha,beta,mean,scale=params
#alpha=param(12.2)
#beta=param(-.2)
#mean=param(0.0)
#scale=param(3.4)
alpha=param(alpha)
beta=param(beta)
mean=param(mean)
scale=param(scale)
lam=0.1
function grads(x)
	grad = Tracker.gradient(()->nigpdf1(x),Flux.params(alpha,beta,mean,scale))
	return grad
end
loglikbestfit=sum(nigpdf1.(train))
loglike=0
for(i,j) in enumerate(train)
	global loglike
	loglike=loglike+nigpdf1(j)
	try
		update!(mean,lam*grads(j)[mean])
		update!(scale,lam*grads(j)[scale])
		update!(beta,lam*grads(j)[beta])
		update!(alpha,lam*grads(j)[alpha])
	catch err
		continue
	end

	println(scale)
end



