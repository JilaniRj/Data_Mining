#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


m8=pd.read_csv("mm8.csv")


# In[3]:


m8


# In[4]:


m8['Date']=pd.to_datetime(m8['Date'])


# In[8]:


m8


# In[ ]:


#total Petroleum Hydrocarbons (TPH) is a term used to describe a broad family of several hundred chemical
#compounds that originally come from crude oil.


# In[5]:


m8.plot(x='Equipment',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Equipment")
plt.ylabel("Target_TPH V/S Actual_TPH")
plt.title("Equipment v/s TPH")


# In[6]:


m8.plot(x='Operator',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Operator")
plt.ylabel("TPH")
plt.title("Operator vs TPH")


# In[7]:


m8.plot(x='Mine',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Mine")
plt.ylabel("TPH")
plt.title("Mine vs TPH")


# In[ ]:




