from bs4 import BeautifulSoup as bsoap
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
from os import path
import shutil

if(path.exists('/home/sahil/fundamentals4')):
    shutil.rmtree('fundamentals4')
os.mkdir('fundamentals4')
os.chdir('/home/sahil/fundamentals4')
options=Options()
options.headless=True
driver = webdriver.Firefox(options=options,executable_path='/home/sahil/Downloads/geckodriver')
driver.get('https://www.moneycontrol.com/markets/earnings/latest-results/latest/yoy/standalone/')
pg = bsoap(driver.page_source,'html.parser')
k=[]
for i in pg.find_all('a',class_='op_gld13'):
    driver.get(i['href'])
    try:
     driver.find_element_by_class_name('Ratios').click()
    except:
     continue
    pg1 = bsoap(driver.page_source,'html.parser')
    title = pg1.find('h1',class_='pcstname').text
    c=0
    while(1):
	    try:
              c=c+1
              print('on')
              url = driver.current_url
	      k1 = pd.read_html(url,header=0)[0]
	      k1['title'] = title
              k1.to_csv(title+str(c)+'.csv')
              k.append(k1)
              try:
                driver.find_element_by_class_name('nextpaging').click()
              except:
                continue
              if(driver.current_url.encode('ascii')==url.encode('ascii')):
                 break
	    except:
	      break
    print(i)
print(k[0])
