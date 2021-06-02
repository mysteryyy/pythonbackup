import pandas as pd
import datetime
df = pd.read_csv("/home/sahil/Downloads/AnalysisSheet.csv")
print(df.columns)
df['title'] = df['Title of Document']
df['doa'] = pd.to_datetime(df['Date of Origination'])
df['doa'] = df.doa.apply(lambda x:x.date())
df1=df[(df.title=='NDA - client') | (df.title=='NDA - Vendor')]
df1=df[(df.title=='NDA - client') | (df.title=='NDA - Vendor') | (df.title=='MSA-Vendor')]
df['title1'] = df.title.str.extract(r'(^w{3})')
df1=df[df.title1=='MSA']
#by date
print(df1[(df1.doa>=datetime.date(2021,1,1)) & (df1.doa<=datetime.date(2021,3,15))]['TAT.1'].mean())
print(df1[(df1.doa>=datetime.date(2021,3,15)) & (df1.doa<=datetime.date(2021,5,31))]['TAT.1'].mean())

