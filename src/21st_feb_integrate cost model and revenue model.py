#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# Load data into a DataFrame
data = pd.read_excel("cd.xlsx")



data


# In[2]:


data.drop(data.tail(2).index,inplace=True)


# In[3]:


data.isnull().sum()


# In[4]:


data['Coal.Weight']=data['Coal.Weight'].fillna(data['Coal.Weight'].mean())


# In[5]:


# Calculate total cost
data['Total Cost'] = data['Freight Chrgs']


# In[6]:


data.head()


# In[7]:


# Calculate total revenue
data['Total Revenue'] = data['Coal.Weight'] * data['Freight Fair']


# In[8]:


data


# In[9]:


# Calculate profit (revenue - cost)
data['Profit'] = data['Total Revenue'] - data['Total Cost']


# In[10]:


data


# In[11]:


# Analyze profitability
total_profit = data['Profit'].sum()
print("Total Profit:", total_profit)


# In[ ]:




