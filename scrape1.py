import bs4 as bs
import requests
import pandas as pd
import numpy as np
url='https://www.moneycontrol.com/financials/adanigaslimited/ratiosVI/ADG01#ADG01'
soup = bs(requests.get(url),'html.parser')
tab = soup.find_all('table',class_='table4')[1]
datarow = []
ind=[]
columns =[]
c=0
for i in tab.find_all('tr'):
   if(i.has_attr('height')):
      if(i['height']=='22px'):
           c = c+1
           datarow=[]
           ind.append(i.td.text.encode('ascii'))
           cond =[j for j in i.find_all('td') if j['align']=='right']           
           for j in cond:
              if(c==1):
                columns.append(j.td.text.encode('ascii'))
              else:
                
                datarow.append(np.float(j.text)) if len(j.text)>0 else datarow.append(np.float('nan'))
          if(c!=1):
            data.append(datarow)
df = pd.DataFrame(data=data,columns=columns,index=ind)
print(df)     
             
                 
       

