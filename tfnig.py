import time
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import numpy as np

import tensorflow.compat.v2 as tf
import tensorflow_probability as tfp
from functools import *
from tensorflow_probability import bijectors as tfb
from tensorflow_probability import distributions as tfd
from tensorflow_probability.python.internal import dtype_util
from tensorflow_probability.python.internal import prefer_static as ps
from tensorflow_probability.python.internal import tensorshape_util
tf.enable_v2_behavior()
X = tf.constant(1.0)
def _make_val_and_grad_fn(value_fn):
  @functools.wraps(value_fn)
  def val_and_grad(x):
    return tfp.math.value_and_gradient(value_fn, x)
  
  return val_and_grad
def logp(x,y,z):
    X = tf.constant(z) 
    u=0
    jds = tfd.JointDistributionSequential([
    tfd.Normal(loc=x, scale=1.),   # m
    tfd.Normal(loc=y, scale=1.),   # b
    lambda b, m: tfd.Normal(loc=m*X + b, scale=1.) # Y

])
   
    return jds.log_prob(x,y,z)
print('gradient ',tfp.math.value_and_gradient(logp,[1.5,2.4,2.1],use_gradient_tape=True))
grad=tfp.math.value_and_gradient(logp,[1.5,2.4,2.1])
