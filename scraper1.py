from bs4 import BeautifulSoup as bsoap
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re
import os
from os import path
import shutil
import time
os.chdir('/home/sahil')
if(path.exists('/home/sahil/fundamentals6')):
    shutil.rmtree('/home/sahil/fundamentals6')
os.mkdir('fundamentals6')
options = Options()
options.headless=True
driver = webdriver.Firefox(options=options,executable_path='/home/sahil/Downloads/geckodriver')
driver.get('https://www.moneycontrol.com/markets/earnings/latest-results/latest/yoy/standalone/')
os.chdir('/home/sahil/fundamentals6')
def ext_symb(pg):
 sym = pg.find('ctag',class_='mob-hide').text.encode('ascii')
 bse = re.findall('\d+',sym[sym.find('BSE')+3:])
 nse = re.findall('\w+',sym[sym.find('NSE')+3:])
 return bse,nse
urls =[]
def map1(lst):
  urls.append(lst['href'])
pg = bsoap(driver.page_source,'html.parser')
map(map1,pg.find_all('a',class_='op_gld13'))
k=[]
for i in range(2732):
    try:
	    driver.get(urls[i])
    except:
            continue
    try:
     driver.find_element_by_class_name('Ratios').click()
    except:
     print('exception caught')
     continue
    pg1 = bsoap(driver.page_source,'html.parser')
    title = pg1.find('h1',class_='pcstname').text
    bse,nse = ext_symb(pg1)
    c=0
    flag=0
    while(flag==0):
            try:
              c=c+1
              print('on')
              url = driver.current_url
	      k1 = pd.read_html(url,header=0)[0]
              print(len(k1))
	      k1['title'] = title
              k1['NSE']= ''
              k1['BSE'] = ''
              if len(bse)!=0: k1['BSE'] = bse[0]
              if len(nse)!=0: k1['NSE'] = nse[0]
              k1.to_csv(title+str(c)+'.csv')
              k.append(k1)
              try:
                driver.find_element_by_class_name('nextpaging').click()
                
              except:
                continue
              if(driver.current_url.encode('ascii')==url.encode('ascii')):
                 flag=1
            except:
              flag=1
    print(urls[i])
print(k[0])
