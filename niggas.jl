using SpecialFunctions
using Ipopt
using JuMP
using GLPK
using Distributions
using Zygote
using Flux
using Flux.Tracker
using Flux.Tracker: update!
using PyCall
using DataFrames
using Debugger
model=Model(Ipopt.Optimizer)
model=Model()
set_optimizer(model, Ipopt.Optimizer);
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
@variable(model,0 <= lam_scale <= 2)
@variable(model,0 <= lam_beta <= 2)
@variable(model,0 <= lam_alpha <= 2)
@variable(model,0 <= lam_mean <= 2)
function grads(x)
	grad = Tracker.gradient(()->nigpdf1(x),Flux.params(alpha,beta,mean,scale))
	return grad
end
loglikbestfit=sum(nigpdf1.(train))
loglike=0
function gas(lams,data)
	lam1=lams[1]
	lam2=lams[2]
	lam3=lams[3]
	lam4=lams[4]
	for(i,j) in enumerate(data)
		global loglike
		try:
			loglike=loglike+nigpdf1(j)
			grad_scale=Tracker.data(grads(j)[scale])
			
			update!(scale,lam1*grads(j)[scale])
			grad_beta=Tracker.data(grads(j)[beta])
			update!(beta,lam2*grads(j)[beta])
			grad_alpha=Tracker.data(grads[j][alpha])
			update!(alpha,lam3*grads(j)[alpha])
			grad_mean=Tracker.data(grads(j)[mean])
			if(alpha<0)
				loglike=loglike-1000
			update!(mean,lam4*grads(j)[mean])
			println(err)
		catch err
			loglike = loglike-1000
		        continue
		end

		println(scale)
	end
	return -loglike
end
function trial(a)
        a = a[1]
	b = a[2]
	c=  a[3]
	d=  a[4]
	return a[1]^2+a[2]^3-a[3]-a[4]
end
#register(model,:gas,4,gas,autodiff=true)
#@NLobjective(model,Max,gas(lam_scale,lam_beta,lam_alpha,lam_mean,train))
#optimize!(model)
println(optimize(lamg->gas(lamg,test),[.1,.1,.1,.1]))
