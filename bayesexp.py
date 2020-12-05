from pybayes.pdfs import CPdf,MLinGaussCPdf,GaussPdf,AbstractEmpPdf
import datetime
import nolds
from datetime import date, timedelta
from numpy.lib.stride_tricks import as_strided
import matplotlib.pyplot as plt
from  matplotlib import pyplot as plt1
from scipy.stats import norm
import pandas as pd
import numpy as np
from  pathlib import Path
from os import path
import shutil
import os
import pdb
from mle import *
#import julia
import scipy.optimize as opt
#from julia.api import Julia
#j=julia.Julia(compiled_modules=False)
#from julia import  Main
from scipy.integrate import quad,dblquad

class MyEmpPdf(AbstractEmpPdf):
    
    def __init__(self, init_particles,weights, rv = None):
        r"""Initialise empirical pdf.

        :param init_particles: 2D array of initial particles; shape (*n*, *m*)
           determines that *n* *m*-dimensioned particles will be used. *Warning:
           EmpPdf does not copy the particles - it rather uses passed array
           through its lifetime, so it is not safe to reuse it for other
           purposes.*
        :type init_particles: :class:`numpy.ndarray`
        """
        if init_particles.ndim != 2:
            raise TypeError("init_particles must be a 2D array")
        self.particles = init_particles
        # set n weights to 1/n
        self.weights =weights 

        self._set_rv(init_particles.shape[1], rv)

    def mean(self, cond = None):
        ret = np.zeros(self.particles.shape[1])
        for i in range(self.particles.shape[0]):
            # ret += self.weights[i] * self.particles[i]:
            np.add_vv(ret, np.multiply_vs(self.particles[i], self.weights[i]), ret)
        return ret

    def variance(self, cond = None):
        ret = np.zeros(self.particles.shape[1])
        for i in range(self.particles.shape[0]):
            # ret += self.weights[i] * self.particles[i]**2
            np.add_vv(ret, np.multiply_vs(np.power_vs(self.particles[i], 2.), self.weights[i]), ret)
        # return ret - self.mean()**2
        return np.subtract_vv(ret, np.power_vs(self.mean(), 2.), ret)

    def eval_log(self, x, cond = None):
        raise NotImplementedError("eval_log doesn't make sense for discrete distribution")

    def sample(self, cond = None):
        raise NotImplementedError("Sample for empirical pdf not (yet?) implemented")

    def resample(self):
        """Drop low-weight particles, replace them with copies of more weighted
        ones. Also reset weights to uniform."""
        np.reindex_mv(self.particles, self.get_resample_indices())
        self.weights[:] = 1./self.weights.shape[0]
        return True


