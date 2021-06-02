import pandas as pd
import numpy as np
import datetime
df = pd.read_csv("/home/sahil/Downloads/AnalysisSheet.csv")
print(df.columns)
df['title'] = df['Title of Document']
df['doa'] = pd.to_datetime(df['Date of Origination'])
df['doa'] = df.doa.apply(lambda x:x.date())
df['doi'] = df['Date of Initial Review by Legal']
df['doe'] = df['Execution Date']
df['doi'] = pd.to_datetime(df.doi).apply(lambda x:x.date())
df['doe'] = pd.to_datetime(df.doe).apply(lambda x:x.date())
df['TATC'] = (df.doe-df.doi)
df['TATC']= df['TATC']/np.timedelta64(1,'D')
df1=df[(df.title=='NDA - client') | (df.title=='NDA - Vendor')]
df['title'] = df.title.apply(lambda x:x[0:3] if isinstance(x,str) else "")
df1=df[df.title=='MSA']
#by date
print(df1[(df1.doa>=datetime.date(2021,1,1)) & (df1.doa<=datetime.date(2021,3,15))]['TATC'].mean())
print(df1[(df1.doa>=datetime.date(2021,3,15)) & (df1.doa<=datetime.date(2021,5,31))]['TATC'].mean())

