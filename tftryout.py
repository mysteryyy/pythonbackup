import time
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
jds = tfd.JointDistributionSequential([
    tfd.Normal(loc=0., scale=1.),   # m
    tfd.Normal(loc=0., scale=1.),   # b
    lambda b, m: tfd.Normal(loc=m*X + b, scale=1.) # Y
])
def _make_val_and_grad_fn(value_fn):
  @functools.wraps(value_fn)
  def val_and_grad(x):
    return tfp.math.value_and_gradient(value_fn, x)
  return val_and_grad
print('gradient ',tfp.math.value_and_gradient(jds,[1,2,3]))
import numpy as np
x = tf.Variable(0.1)
beta = tf.Variable(1.36)
q = tf.Variable(2.1)
x.assign(2.25)
with tf.GradientTape() as tape:
    upgamma = (3-q)/(2*(q-1))
    num = (3.14**.5)*tf.math.exp(tf.math.lgamma(upgamma))
    downgamma = 1/(q-1)
    den = ((q-1)**.5)*tf.math.exp(tf.math.lgamma(downgamma))
    cq = num/den
    pd = tf.math.pow((1-(1-q)*beta*x**2),1/(1-q))*(beta**.5)*(1/cq)
    lpd = tf.math.log(pd)
x.assign(4.2)
with tf.GradientTape() as tape1:
    trial = tf.math.exp(x)
print(tape.gradient(lpd,[beta,q]))
print(tape1.gradient(trial,[x]))
