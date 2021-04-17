import pandas as pd
import numpy as np
from dateutil import parser
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from scipy.stats import ttest_ind
df = pd.read_csv('/home/sahil/Downloads/LegalTrackerDated1.csv')
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
df['doctype'] = df['Long Title of Document']
df['reviewers'] = df['Reviewed By']
df['bs'] = df['Business Segment']
df['tat'] = df['TAT Days']
cats=['SOW','PSA/MSA','NDA']
sowmed = df[df.doctype=='SOW'].pages.median()
psamsamed = df[(df.doctype=='PSA') | (df.doctype=='MSA')].pages.median()
ndamed = df[df.doctype=='NDA'].pages.median()
cols = ['SOW'+'<'+str(sowmed)+'pages','SOW'+'>'+str(sowmed)+' pages','MSA/PSA'+'<'+str(psamsamed)+'pages','MSA/PSA'+'>'+str(psamsamed)+'pages','NDA'+'<'+str(ndamed)+'pages','NDA'+'>'+str(ndamed)+'pages']
ind = ['Q-Tempelate','Non Q-tempelate']
dftt = pd.DataFrame()
dftt.loc[ind[0],cols[0]] = df[(df.doctype=='SOW') & (df.qornot=='Yes') & (df.pages<sowmed)].tat.mean()
dftt.loc[ind[1],cols[0]] = df[(df.doctype=='SOW') & (df.qornot=='No') & (df.pages<sowmed)].tat.mean()
dftt.loc[ind[0],cols[1]] = df[(df.doctype=='SOW') & (df.qornot=='Yes') & (df.pages>sowmed)].tat.mean()
dftt.loc[ind[1],cols[1]] = df[(df.doctype=='SOW') & (df.qornot=='No') & (df.pages>sowmed)].tat.mean()
dftt.loc[ind[0],cols[2]] = df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='Yes') & (df.pages<psamsamed)].tat.mean()
dftt.loc[ind[1],cols[2]] = df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='No') & (df.pages<psamsamed)].tat.mean()
dftt.loc[ind[0],cols[3]] = df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='Yes') & (df.pages>psamsamed)].tat.mean()
dftt.loc[ind[1],cols[3]] = df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='No') & (df.pages>psamsamed)].tat.mean()
dftt.loc[ind[0],cols[4]] = df[(df.doctype=='NDA') & (df.qornot=='Yes') & (df.pages<ndamed)].tat.mean()
dftt.loc[ind[1],cols[4]] = df[(df.doctype=='NDA') & (df.qornot=='No') & (df.pages<ndamed)].tat.mean()
dftt.loc[ind[0],cols[5]] = df[(df.doctype=='NDA') & (df.qornot=='Yes') & (df.pages>ndamed)].tat.mean()
dftt.loc[ind[1],cols[5]] = df[(df.doctype=='NDA') & (df.qornot=='No') & (df.pages>ndamed)].tat.mean()
def tat_analysis(df):
    ttdf = pd.DataFrame(columns=df.doctype.unique(),index = ['Q-Tempelate','Non-Q Tempelate'])
    for i in ttdf.columns:
        for j in ttdf.index:
            qornot = 'Yes' if j=='Q-Tempelate' else 'No'
            tat  = df[(df.doctype==i) & (df.qornot==qornot)]['Turnaround Time']
            if(len(tat)>5):
                ttdf.loc[j,i]= tat.mean()
            else:
                ttdf.loc[j,i]= "Not enough data"
    return ttdf
def tat_analysis_reviewers(df):
    ttdf = pd.DataFrame(columns=df.doctype.unique(),index =df.reviewers.unique()) 
    for i in ttdf.columns:
        for j in ttdf.index:
            #qornot = 'Yes' if j=='Q-Tempelate' else 'No'
            tat  = df[(df.doctype==i) & (df.reviewers==j)]['Turnaround Time']
            if(len(tat)>5):
                ttdf.loc[j,i]= tat.mean()
            else:
                ttdf.loc[j,i]= "Not enough data"
    return ttdf
def tat_analysis_stat_test(df):
    ttdf = pd.DataFrame(columns=df.doctype.unique(),index = ['Q-Tempelate','Non-Q Tempelate','pvalue'])
    for i in ttdf.columns:
        tat1  = df[(df.doctype==i) & (df.qornot=='Yes')]['Turnaround Time']
        tat2  = df[(df.doctype==i) & (df.qornot=='No')]['Turnaround Time']
        if(len(tat1)<5 or len(tat2)<5):

           ttdf.loc['pvalue',i] = "Not enough data"

        p=ttest_ind(tat1,tat2,equal_var=False).pvalue
        ttdf.loc['pvalue',i] = p

        for j in ttdf.index[0:2]:
            qornot = 'Yes' if j=='Q-Tempelate' else 'No'
            tat  = df[(df.doctype==i) & (df.qornot==qornot)]['Turnaround Time']
            if(len(tat)>5):
                ttdf.loc[j,i]= tat.mean()
            else:
                ttdf.loc[j,i]= "Not enough data"
    return ttdf
def tat_analysis_stat_test_bs(df):
    ttdf = pd.DataFrame(columns=['AWS','GCP'],index = ['Q-Tempelate','Non-Q Tempelate','pvalue'])
    for i in ttdf.columns:
        tat1  = df[(df.bs==i) & (df.qornot=='Yes')]['Turnaround Time']
        tat2  = df[(df.bs==i) & (df.qornot=='No')]['Turnaround Time']
        if(len(tat1)<5 or len(tat2)<5):

           ttdf.loc['pvalue',i] = "Not enough data"

        p=ttest_ind(tat1,tat2,equal_var=False,alternative='greater').pvalue
        ttdf.loc['pvalue',i] = p

        for j in ttdf.index[0:2]:
            qornot = 'Yes' if j=='Q-Tempelate' else 'No'
            tat  = df[(df.bs==i) & (df.qornot==qornot)]['Turnaround Time']
            if(len(tat)>5):
                ttdf.loc[j,i]= tat.mean()
            else:
                ttdf.loc[j,i]= "Not enough data"
    return ttdf


ttdf1 = tat_analysis(df[df.pages>5])
ttdf2 = tat_analysis(df[df.pages<5])
ttdf3 = tat_analysis_reviewers(df)
ttdf4 = tat_analysis_stat_test(df)
ttdf5 = tat_analysis_stat_test_bs(df)

# funtion
def multiple_dfs(df_list, sheets, file_name, spaces):
    writer = pd.ExcelWriter(file_name,engine='xlsxwriter')   
    row = 0
    for dataframe in df_list:
        dataframe.to_excel(writer,sheet_name=sheets,startrow=row , startcol=0)   
        row = row + len(dataframe.index) + spaces + 1
    writer.save()

# list of dataframes
dfs = [ttdf1,ttdf2]

# run function
multiple_dfs(dfs, 'Validation', 'test1.xlsx', 3)
dtr=DecisionTreeRegressor(min_samples_split=10)
