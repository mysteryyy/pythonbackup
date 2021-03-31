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
df['qornot']=df['Whether Q Template \n(Yes / No)']
