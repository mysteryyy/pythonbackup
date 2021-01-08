using SpecialFunctions
using Distributions
using Zygote
using Flux
using PyCall
function nigpdf1(mean,scale,alpha,beta,x)
          extra = (alpha^2-beta^2)^.5
          num = alpha*scale*besselk(1,alpha*(scale^2 + (x-mean)^2)^.5)*exp(extra*scale+beta*(x-mean))
          den = pi*(scale^2 + (x-mean)^2)^.5
          pdf = num/den
          return pdf
end
