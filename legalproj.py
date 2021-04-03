import pandas as pd
import numpy as np
from dateutil import parser
df = pd.read_csv('/home/sahil/Downloads/LegalTrackerDated.csv')
#df = df[df['Deal Created date'].notna()]
df = df[df['Date of Initial Review by Legal'].notna()]
#df['Deal Created date']=df['Deal Created date'].apply(lambda x:parser.parse(x))
df['Date of Origination']=df['Date of Origination'].apply(lambda x:parser.parse(x))
df['Date of Initial Review by Legal']=df['Date of Initial Review by Legal'].apply(lambda x:parser.parse(x))
df['initreview']=df['Date of Initial Review by Legal']
df['Turnaround Time'] = (df.initreview- df['Date of Origination']).apply(lambda x:x.days)
df= df[df['No. of pages '].notna()]
df['pages'] = df['No. of pages ']
df= df[df.pages!='RFP']
df['qornot']=df['Whether Q Template \n(Yes / No)']
df['pages'] = df.pages.astype(float)
df['doctype'] = df['Short Title of Document']
ttdf = pd.DataFrame(columns=df.doctype.unique(),index = ['Q-Tempelate','Non-Q Tempelate'])
for i in ttdf.columns:
    for j in ttdf.index:
        qornot = 'Yes' if j=='Q-Tempelate' else 'No'
        tat  = df[(df.doctype==i) & (df.qornot==qornot)]['Turnaround Time']
        if(len(tat)>5):
            ttdf.loc[j,i]= tat.mean()
        else:
            ttdf.loc[j,i]= "Not enough data"

