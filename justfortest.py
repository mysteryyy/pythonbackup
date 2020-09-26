from bs4 import BeautifulSoup as bsoap
import re
import os
from os import path
import shutil
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from nsepy import get_history
from datetime import date
import pandas as pd
import numpy as np
import pickle as pck
import os
import re
from  loading_data import ext
et = ext()
k1=et.give_file('/home/sahil/fundamentals8','monthly_data')
k=et.give_file('/home/sahil/fundamentals8','finalkfr')
kk=[]
kk1=[]
allsym = [j.title[0] for j in k1]
def prepro(kp):
  print(kp.columns)
  kp['yearly'] = (kp.Close-kp.Close.shift(12))/kp.Close.shift(12)
  kp['quarterly'] = (kp.Close-kp.Close.shift(4))/kp.Close.shift(4)
  kk.append(kp)

def prepro1(k):
  tit = k.title[0].encode('ascii')
  tit = tit[0:tit.find('Ltd.')-1]+' '
  knew=dict()
  knew[k.columns[0]] = 'returns'
  if(tit in allsym):
   ret_k = [j for j in k1 if j.title[0]==tit][0]
  else:
    print('not found')
    return
  for i in k.columns:
    if(len(re.findall('\d{2}',i))!=0):
        yr = i.split(' ')
        if(yr[0] in ['Jun','Jul']):
            if(yr[0]=='Jun'):
                yr[0]='June'
            else:
                yr[0]='July'
        yrst = yr[0]+' '+'20'+yr[1]
        print(ret_k.Date[0]==yrst)
        print(ret_k.Date[0])
        print(yrst)
        print(yrst in  list(ret_k.Date))
        k[yrst] = k[i]
        k = k.drop(i,axis=1)
        ln = len(list(ret_k[ret_k.Date==yrst].yearly))
        if(ln!=0):
         knew[yrst] = list(ret_k[ret_k.Date==yrst].yearly)[0]
        else:
         knew[yrst] = np.nan
  
  k = k.append(knew,ignore_index=True)
  kk1.append(k)      
map(prepro,k1)
k1 =kk

map(prepro1,k)
        





