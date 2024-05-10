#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv("annual_data.csv")


# In[3]:


df


# In[4]:


df.shape


# In[5]:


df.size


# In[6]:


df.describe()


# In[7]:


df.info()


# In[8]:


df.head()


# In[9]:


df.tail(10)


# In[10]:


df['Period']=pd.to_datetime(df['Period'])


# In[11]:


df.head()


# In[12]:


df.isnull().sum()


# In[13]:


df['Inst_sector'].value_counts().unique()


# In[14]:


df['Inst_sector_code'].value_counts().unique()


# In[15]:


df['Inst_sector'].unique()


# In[16]:


df['Inst_sector'].value_counts()


# In[17]:


df['Descriptor'].value_counts()


# In[18]:


df['Descriptor'].unique()


# In[19]:


df['Asset_liability_code'].unique()


# In[20]:


df.head()


# In[21]:


df['SNA08TRANS'].unique()


# In[22]:


df['SNA08TRANS'].value_counts()


# In[23]:


df.shape


# In[24]:


df=df.drop('SNA08TRANS',axis='columns')


# In[25]:


df


# In[26]:


df=df.drop("Inst_sector",axis='columns')


# In[27]:


df=df.drop('Descriptor',axis='columns')


# In[28]:


df=df.drop('Asset_liability_code',axis='columns')


# In[29]:


df


# In[30]:


import warnings
warnings.filterwarnings('ignore')


# In[31]:


df.info()


# In[32]:


df


# In[33]:


a=df['Period'].head(80)
b=df['Inst_sector_code'].head(80)

plt.bar(a,b)


# In[ ]:






# In[ ]:





# In[ ]:




