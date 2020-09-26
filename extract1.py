from bs4 import BeautifulSoup as bsoap
import re
import os
import nsepy
from os import path
import shutil
import time
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import date
from nsepy import get_history
import pandas as pd
import numpy as np
import pickle as pck
import os
os.chdir('/home/sahil/fundamentals8')
k=[]
s = []
def ext_df(k):
   df = k
   s.append(k['NSE'][0])
with open('finalkfr','rb') as f:
  try:
      while True:
        k.append(pck.load(f))
  except EOFError:
        pass
np1=[]   
p=pd.DataFrame()        
def mid(i):
    df1 = pd.DataFrame(index=['returns'])
    def validcol(cn):
        if(re.search('\d{2}',cn)!=None):
            val = re.findall('\d{2}',cn)[0]
            nc = i[cn]
            val = '20'+val
            val = int(val)
            t = date(val,3,1)
            t1 = date(val+1,3,1)
            d = get_history(symbol=i['NSE'][0],start = t,end=t1)
            p=d
            ret2 = d.Close[-1]
            ret1 = d.Close[0]
            year_rets =(((ret2-ret1)/ret1)*100)
            df1[cn] = year_rets
    map(validcol,i.columns)
    i =i.append(df1)
    np1.append(i)
    print(i['NSE'][0])
map(mid,k)
print(np1[0])

    

    
