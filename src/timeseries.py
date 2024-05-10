#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv("annual_data.csv")


# In[3]:


df


# In[4]:


df=df.drop('SNA08TRANS',axis=1)


# In[5]:


df=df.drop('Descriptor',axis=1)


# In[6]:


df=df.drop('Inst_sector',axis=1)


# In[7]:


df


# In[8]:


df.info()


# In[9]:


df['Period']=pd.to_datetime(df['Period'])


# In[10]:


df


# In[11]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Period']=le.fit_transform(df['Period'])
df['Asset_liability_code']=le.fit_transform(df['Asset_liability_code'])
df.info()


# In[18]:


df


# In[4]:


plt.hist(df['Inst_sector_code'])


# In[5]:


x=df['Period']
y=df['Asset_liability_code']
plt.scatter(x,y)


# In[21]:


plt.bar(x,y)


# In[ ]:







# In[ ]:







# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[23]:


import warnings
warnings.filterwarnings('ignore')


# In[24]:


get_ipython().system('pip install prophet')


# In[25]:


df=pd.read_csv("annual_data.csv")


# In[26]:


df


# In[27]:


df['Period']=pd.to_datetime(df['Period'])


# In[28]:


df


# In[29]:


df.plot()


# In[30]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Asset_liability_code']=le.fit_transform(df['Asset_liability_code'])


# In[31]:


df=df.drop('Inst_sector',axis=1)


# In[32]:


df=df.drop('Descriptor',axis=1)


# In[33]:


df=df.drop('SNA08TRANS',axis=1)


# In[34]:


df.plot()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


data=pd.read_csv("mm8.csv")


# In[3]:


data


# In[4]:


data['Date']=pd.to_datetime(data['Date'])


# In[5]:


data


# In[6]:


data.set_index('Date',inplace=True)


# In[7]:


data


# In[8]:


data=data.drop('Mine',axis=1)


# In[9]:


data=data.drop('Equipment',axis=1)


# In[10]:


data=data.drop('Material',axis=1)


# In[11]:


data=data.drop('Shift',axis=1)


# In[12]:


data=data.drop('Operator',axis=1)


# In[13]:


data=data.drop('Address',axis=1)


# In[14]:


data=data.drop('Hours_Worked',axis=1)


# In[16]:


data=data.drop('Target_TPH',axis=1)


# In[17]:


data


# In[21]:


from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(data, order=(0, 1, 1)) 
results_ARIMA = model.fit()

results_ARIMA.summary()


# In[27]:


a=results_ARIMA.forecast(3)


# In[32]:


a


# In[31]:


a
data.plot()
plt.show()


# In[ ]:




