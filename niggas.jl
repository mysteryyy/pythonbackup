using SpecialFunctions
using Distributions
using Zygote
using Flux
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
test=ret[train_len:end]
params = sp.wald.fit(train)
alpha = Array{Float64}(length(test))
fill!(alpha,0)


