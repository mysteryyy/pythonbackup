using SpecialFunctions
using Distributions
using Zygote
using Flux.Tracker
using Flux.Tracker: update!
using PyCall
using DataFrames

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
alpha = zeros(length(test)+1)
beta = zeros(length(test)+1)
mean = zeros(length(test)+1)
scale = zeros(length(test)+1)
alpha[1]=params[1]
beta[1]=params[2]
mean[1]=params[3]
scale[1]=params[4]
lam=0.1
for(i,j) in enumerate(train)
    mean[i+1]=mean[i]+lam*mean_grad(alpha[i],beta[i],mean[i],scale[i],train[i])
    scale[i+1]=scale[i]+lam*scale_grad(alpha[i],beta[i],mean[i+1],scale[i],train[i])
    beta[i+1]=beta[i]+lam*beta_grad(alpha[i],beta[i],mean[i+1],scale[i+1],train[i])
    alpha[i+1]=alpha[i]+lam*alpha_grad(alpha[i],beta[i+1],mean[i+1],scale[i+1],train[i])
end



