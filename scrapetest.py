import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
url ='https://www.moneycontrol.com/financials/surbhiindustries/ratiosVI/SI50#SI50'
soup=requests.get(url).content
soup=BeautifulSoup(soup,'html.parser')
tab = soup.find_all('table',class_='mctable1')[0]
columns =[]
ind=[]
data=[]
na = u'--'.encode('utf-8')
c=0
for i in tab.find_all('tr'):
   
      
      c = c+1
      datarow =[]
      if len(i.td.text)!=0:
         ind.append(i.td.text)
      for j in i.find_all('td'):
		   if(c==1):
		     columns.append(j.text)
		   else:
                      if(len(j.text)!=0):
                   
                       if(j.text.encode('utf-8')==na):
                         datarow.append(np.float('nan'))
                       else:
                        if(j.text.encode('utf-8').isdigit()):
                          datarow.append(np.float(j.text.encode('ascii')))
                        else:
                            ind.append(j.text)
                      else:
                       datarow.append(np.float('nan'))
              
      
      if(c!=1):        
       data.append(datarow)
col =['ratio']
col.append(i for i in columns)
df = pd.DataFrame(columns=col,data=data,index=ind)
df['compname'] = soup.find('h1',class_='pcstname').text
df.to_csv('scraped2.csv')
print('test')
