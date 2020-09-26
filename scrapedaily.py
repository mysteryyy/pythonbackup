

import requests
from bs4 import BeautifulSoup as bsoap
import re
import os
import nsepy
import pandas as pd
import numpy as np
from os import path
import shutil
import time
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from nsepy import get_history
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
import os
os.chdir('/home/sahil/projdir/fundamentals8')

# open it, go to a website, and get results
driver = webdriver.Chrome('chromedriver',options=options)
ch='d'
k = pd.read_csv('ind_nifty500list.csv')
lg = k.Symbol.unique()
nmlist=[]
for i in lg:
  
  k1=k[k.Symbol==i]
  if(len(k1)!=0):
   nmlist.append(list(k1[k.columns[-1]])[0])
symlist=nmlist
os.chdir('/home/sahil/projdir/fundamentals8')
def dailydata(s):
  driver.get('https://www.moneycontrol.com/india/stockpricequote/')
  print(driver.current_url)
  tbox = driver.find_element_by_xpath('//*[@id="company"]')
  tbox.send_keys(s)
  btxpath =  "div.MT2:nth-child(1) > input:nth-child(2)"
  flag=0
  c=0
  while(flag==0):
      try:
        driver.find_element_by_css_selector(btxpath).click()
        flag=1
      except Exception as e:
        print(e)
        c=c+1
        if(c==3): 
          flag=1
        print('sleeping')
        time.sleep(5)
  print(driver.current_url)
  hpxpath= "Historical Prices"
  flag=0
  c=0
  while(flag==0):
      try:
        driver.find_element_by_link_text(hpxpath).click()
        flag=1
      except Exception as e:
        print(e)
        c=c+1
        print('sleeping')
        if(c==3):
          flag=1
        time.sleep(5)
  pg = bsoap(driver.page_source,'html.parser')
  driver.get(pg.find('a',title='Click Here')['href'])
  nse1 = Select(driver.find_element_by_css_selector('#ex'))
  if(ch=='d'):
      nse1.select_by_visible_text('NSE')
      nse = Select(driver.find_element_by_name('frm_dy'))
      nse.select_by_visible_text('01')
      nse = Select(driver.find_element_by_name('frm_mth'))
      nse.select_by_visible_text('Mar')
      nse = Select(driver.find_element_by_name('frm_yr'))
      nse.select_by_visible_text('2000')
      nse = Select(driver.find_element_by_name('to_dy'))
      nse.select_by_visible_text('01')
      nse = Select(driver.find_element_by_name('to_mth'))
      nse.select_by_visible_text('Mar')
      nse = Select(driver.find_element_by_name('to_yr'))
      nse.select_by_visible_text('2020')
      p = driver.find_element_by_css_selector('#mc_mainWrapper > div.PA10 > div > div.PT15 > div.PT10 > div.brdb > table > tbody > tr > td:nth-child(1) > form > div:nth-child(4) > input[type="image"]:nth-child(4)')
      p.click()
  else:
      nse =Select(driver.find_element_by_name('mth_frm_mth'))
      nse.select_by_visible_text('Mar')
      nse =Select(driver.find_element_by_name('mth_frm_yr'))
      nse.select_by_visible_text('2000')
      nse =Select(driver.find_element_by_name('mth_to_mth'))
      nse.select_by_visible_text('Mar')
      nse =Select(driver.find_element_by_name('mth_to_yr'))
      nse.select_by_visible_text('2019')
      p = driver.find_element_by_css_selector('td.PT15:nth-child(3) > form:nth-child(1) > div:nth-child(4) > input:nth-child(3)')
      p.click()


  k=[]
  flag=0
  while(True):
     try:
        pg = bsoap(driver.page_source,'html.parser')

        tab = pg.find_all('table',class_='tblchart')[0]
        
        k.append(pd.read_html(str(tab)))        
        #k.append(pd.read_html(driver.current_url,attrs={'class':'tblchart'}))
        #url = str(driver.current_url.encode('ascii'))
        url = driver.current_url
        url = url[0:url.find('?')]
        elem = pg.find_all('a',class_='nextprev')
        flag=1
     except Exception as e:
        print(e)
     if(len(elem)==0):
          break
      #    url1 = str(elem[0]['href'].encode('ascii'))

      #url1 = elem[0]['href'].decode('utf-8')
     url1 = elem[0]['href']
     url = url+url1
     driver.get(url)
     print(k)
     print('next')
  with open('daily_data','a+b') as d:
       pck.dump(k,d)
  flag=1
  print(k)
  k =pd.concat(k[0:][0])
  k['id'] = s
  return k
driver.quit()
for i in symlist:
  dailydata(i)
