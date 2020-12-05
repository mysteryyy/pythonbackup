import datetime
from datetime import date, timedelta
from numpy.lib.stride_tricks import as_strided
import pandas as pd
import numpy as np
from  pathlib import Path
from os import path
import shutil
import os
import pdb
from digfilters import filters
filt=filters()
k = pd.read_pickle('projdir/dailydata.pkl')
k1 =k[k.Symbol==k.Symbol.unique()[0]]
k=k1
k['ret'] = k.Close-k.Open
k['dec'] = filt.highpass2(k.Close,10)-filt.highpass2(k.Close,5)
k['avg'] = k.Close.rolling(10).mean()- k.Close.rolling(5).mean()
k['retm'] = 0
for i in range(1,6):
    k['retm']+= k.ret.shift(-i)

