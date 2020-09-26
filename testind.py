import datetime
from datetime import date, timedelta
from numpy.lib.stride_tricks import as_strided
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
from sklearn.cluster import MeanShift, estimate_bandwidth
from scipy.signal import argrelextrema
from keras.models import load_model
from keras.models import Sequential
from keras.utils import to_categorical
from keras.optimizers import SGD
from keras import initializers
from keras.layers import Flatten,TimeDistributed,Dense,Activation,LSTM,Dropout,MaxPooling1D,BatchNormalization
from keras.layers import GlobalAveragePooling1D
from keras.layers import Conv1D
from keras import metrics
from keras.metrics import binary_accuracy
from  pathlib import Path
from hurst import compute_Hc, random_walk
from os import path
import shutil
import os
import pdb
import numpy as np
import pandas as pd
import datetime
os.chdir('/home/sahil')
from trainauto4 import neural
from keras.utils import to_categorical
f = neural(20,10)
x,y,yh,x1,y1,yh1,yd,yd1,ys,ys1=f.genarr2(datetime.date(2008,1,2),datetime.date(2019,6,1),'rsift')
f.mlplstm(x,y,yh,x1,y1,yh1,yd,yd1,ys,ys1,'lstm',7)
