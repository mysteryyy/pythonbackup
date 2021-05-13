import datetime
import random
import nolds
from datetime import date, timedelta
from numpy.lib.stride_tricks import as_strided
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt1
from scipy.stats import norm
import pandas as pd
import numpy as np
from  pathlib import Path
from os import path
import shutil
import os
import pdb
from mle import *

pr = pd.DataFrame(columns=["Open","High","Low","Close",],data=np.ones((20,4)))
print(pr)
for i in range(len(pr)):
    print(pr.iloc[i])
