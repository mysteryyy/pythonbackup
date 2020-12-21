import tensorflow as tf
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
