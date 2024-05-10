#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv('annual_data.csv')


# In[3]:


df


# In[4]:


x=df['Period']
y=df['Asset_liability_code']
plt.bar(x,y)


# In[5]:


a=df[(df['Asset_liability_code']=='L000000')]


# In[6]:


a


# In[8]:


x=df['Period']
y=df['Inst_sector']
plt.bar(x,y)


# In[9]:


b=df[(df['Asset_liability_code']=='L000000') & (df['Inst_sector']=='Total all sectors')]


# In[10]:


b


# In[ ]:





