using SpecialFunctions
using Distributions
using Zygote
using Flux.Tracker
using PyCall

function nigpdf1(alpha,beta,mean,scale,x)
          extra = (alpha^2-beta^2)^.5
          num = alpha*scale*besselk(1,alpha*(scale^2 + (x-mean)^2)^.5)*exp(extra*scale+beta*(x-mean))
          den = pi*(scale^2 + (x-mean)^2)^.5
          pdf = num/den
          return pdf
end


sp = pyimport("scipy.stats")
pd = pyimport("pandas")
file_dir="/home/sahil/pythonbackup"
k = pd.read_pickle(file_dir+"/todays_stock1.pkl")
ret=Array(k.ret)
train_len=Int(round(.5*length(ret)))
train=ret[1:train_len]
test=ret[train_len:Int(round(0.8*end))]
params = sp.wald.fit(train)
alpha = zeros(length(test))
beta = zeros(length(test))
mean = zeros(length(test))
scale = zeros(length(test))
alpha[1]=params[1]
beta[1]=params[2]
mean[1]=params[3]
scale[1]=params[4]
for(i,j) in enumerate(train)
	grad = Tracker.gradient(nigpdf1(alpha[i],beta[i],mean[i],scale[i]))
	scale[i+1]=scale[i]+lam*grad 


