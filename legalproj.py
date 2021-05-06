import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import RMSprop
import numpy as np
from dateutil import parser
from supervised.automl import AutoML
import tensorflow as tf
import tensorflow_probability as tfp
tfd = tfp.distributions
tfpl = tfp.layers
tfb = tfp.bijectors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,mean_absolute_percentage_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostClassifier,RandomForestClassifier,RandomForestRegressor
from scipy.stats import ttest_ind
def doctypes(l):
    if l=='PSA'or l=='MSA':
        return 'PSA/MSA'
    else:
        return l

automl=AutoML(mode='Compete',total_time_limit=60)
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
df['doctype1'] = df.doctype.apply(lambda x:doctypes(x))
cats=['SOW','PSA/MSA','NDA']
sowmed = df[df.doctype=='SOW'].pages.median()
psamsamed = df[(df.doctype=='PSA') | (df.doctype=='MSA')].pages.median()
ndamed = df[df.doctype=='NDA'].pages.median()
cols = ['SOW'+'<'+str(sowmed)+'pages','SOW'+'>'+str(sowmed)+' pages','MSA/PSA'+'<'+str(psamsamed)+'pages','MSA/PSA'+'>'+str(psamsamed)+'pages','NDA'+'<'+str(ndamed)+'pages','NDA'+'>'+str(ndamed)+'pages']
ind = ['Q-Tempelate','Non Q-tempelate','pvalue']
def ttest(a,b):
    return ttest_ind(a,b,equal_var=False,alternative='greater').pvalue
df1 = df[['doctype1','bs','reviewers','qornot','pages','tat']]
df1=df1.dropna()
inpvars1 = df1[['doctype1','bs','reviewers','qornot']]
inpvars2 = df1[['pages']]
outvars = df1[['tat']]
def nll(y_true,y_pred):
    return -y_pred.log_prob(y_true)
x = np.concatenate((OneHotEncoder(sparse=False).fit_transform(inpvars1),np.matrix(inpvars2)),axis=1)
x=StandardScaler().fit_transform(x)
x=MinMaxScaler().fit_transform(x)
y = np.array(np.float32(np.array(outvars)))
y =y.reshape(len(y),)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.3)
model = Sequential([
Dense(input_shape=(x_train.shape[1],), units=15,kernel_initializer=tf.constant_initializer(50),
          bias_initializer=tf.constant_initializer(0)),
    tfpl.DistributionLambda(lambda t:tfd.Exponential(rate=t),
                           convert_to_tensor_fn=tfd.Distribution.sample)
])
model.compile(loss=nll,
optimizer=RMSprop(learning_rate=0.01))
model.fit(x_train, y_train, epochs=1000, verbose=True);
tr = RandomForestRegressor(n_estimators=50,max_depth=6,min_samples_split=10)
clf=tr
#clf = AdaBoostClassifier(base_estimator=tr,n_estimators=80,random_state=50,learning_rate=1.0)
clf.fit(x_train,y_train)
print(mean_absolute_percentage_error(clf.predict(x_test),y_test))
dftt = pd.DataFrame()

dftt.loc[ind[0],cols[0]] = df[(df.doctype=='SOW') & (df.qornot=='Yes') & (df.pages<sowmed)].tat.mean()
dftt.loc[ind[1],cols[0]] = df[(df.doctype=='SOW') & (df.qornot=='No') & (df.pages<sowmed)].tat.mean()
dftt.loc[ind[2],cols[0]] =ttest(df[(df.doctype=='SOW') & (df.qornot=='Yes') & (df.pages<sowmed)].tat,df[(df.doctype=='SOW') & (df.qornot=='No') & (df.pages<sowmed)].tat) 
dftt.loc[ind[0],cols[1]] = df[(df.doctype=='SOW') & (df.qornot=='Yes') & (df.pages>sowmed)].tat.mean()
dftt.loc[ind[1],cols[1]] = df[(df.doctype=='SOW') & (df.qornot=='No') & (df.pages>sowmed)].tat.mean()
dftt.loc[ind[2],cols[1]] =ttest(df[(df.doctype=='SOW') & (df.qornot=='Yes') & (df.pages<sowmed)].tat,df[(df.doctype=='SOW') & (df.qornot=='No') & (df.pages>sowmed)].tat) 

dftt.loc[ind[0],cols[2]] = df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='Yes') & (df.pages<psamsamed)].tat.mean()
dftt.loc[ind[1],cols[2]] = df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='No') & (df.pages<psamsamed)].tat.mean()
dftt.loc[ind[2],cols[2]] =ttest(df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='Yes') & (df.pages<psamsamed)].tat,df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='No') & (df.pages<psamsamed)].tat) 
dftt.loc[ind[0],cols[3]] = df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='Yes') & (df.pages>psamsamed)].tat.mean()
dftt.loc[ind[1],cols[3]] = df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='No') & (df.pages>psamsamed)].tat.mean()
dftt.loc[ind[2],cols[3]]=ttest(df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='Yes') & (df.pages>psamsamed)].tat,df[((df.doctype=='MSA') | (df.doctype=='PSA')) & (df.qornot=='No') & (df.pages>psamsamed)].tat)  
dftt.loc[ind[0],cols[4]] = df[(df.doctype=='NDA') & (df.qornot=='Yes') & (df.pages<ndamed)].tat.mean()
dftt.loc[ind[1],cols[4]] = df[(df.doctype=='NDA') & (df.qornot=='No') & (df.pages<ndamed)].tat.mean()
dftt.loc[ind[2],cols[4]]=ttest(df[(df.doctype=='NDA') & (df.qornot=='Yes') & (df.pages<ndamed)].tat,df[(df.doctype=='NDA') & (df.qornot=='No') & (df.pages<ndamed)].tat)
dftt.loc[ind[0],cols[5]] = df[(df.doctype=='NDA') & (df.qornot=='Yes') & (df.pages>ndamed)].tat.mean()
dftt.loc[ind[1],cols[5]] = df[(df.doctype=='NDA') & (df.qornot=='No') & (df.pages>ndamed)].tat.mean()
dftt.loc[ind[2],cols[5]]=ttest(df[(df.doctype=='NDA') & (df.qornot=='Yes') & (df.pages>ndamed)].tat,df[(df.doctype=='NDA') & (df.qornot=='No') & (df.pages>ndamed)].tat)
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

def tat_page_cor(df):
   corrdf = pd.DataFrame(columns=['SOW','NDA','PSA/MSA'],index = ['corr'])
   for i in corrdf.columns:
       if (i=='PSA/MSA'):
           df1 = df[(df.doctype=='MSA') | (df.doctype=='PSA')]
       else:
           df1 = df[df.doctype==i]
       corrdf.loc['corr',i] = df1[['pages','tat']].corr().tat.iloc[0]
   return corrdf
def tat_page_cor_bs(df):
   corrdf = pd.DataFrame(columns=['AWS','GCP'],index = ['corr'])
   for i in corrdf.columns:
       df1 = df[df.bs==i]
       corrdf.loc['corr',i] = df1[['pages','tat']].corr().tat.iloc[0]
   return corrdf


ttdf1 = tat_analysis(df[df.pages>5])
ttdf2 = tat_analysis(df[df.pages<5])
ttdf3 = tat_analysis_reviewers(df)
ttdf4 = tat_analysis_stat_test(df)
ttdf5 = tat_analysis_stat_test_bs(df)
corrdf = tat_page_cor(df)
corrdfbs=tat_page_cor_bs(df)
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
