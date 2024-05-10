#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_excel("cd.xlsx")
data


# In[3]:


data.drop(data.tail(2).index,inplace=True)


# In[4]:


data.isnull().sum()


# In[5]:


data['Coal.Weight'].count()


# In[6]:


data['Coal.Weight']=data['Coal.Weight'].fillna(data['Coal.Weight'].mean())


# In[7]:


data.isnull().sum()


# In[8]:


data


# In[9]:


data=data.drop(columns = ['Loading Point','S.NO','Freight Fair','Unloading Point','Tranport C P','Delivery Order No','Contact Person No','Company Name'])


# In[10]:


data


# In[12]:


data.info()


# In[13]:


data['Date']=pd.to_datetime(data['Date'])


# In[25]:


data


# In[18]:


x=data['Date']
y=data['Coal.Weight']
plt.bar(x,y)


# In[24]:


x= data['Date'].head(20)
y=data['Truck No.'].head(20)
plt.bar(x,y)


# In[37]:


import pandas as pd
import matplotlib.pyplot as plt

# Line Chart (Freight Charges over Time)
plt.figure(figsize=(10, 6))
plt.bar(data['Date'], data['Freight Chrgs'])#, marker='o')
plt.xlabel('Date')
plt.ylabel('Freight Charges')
plt.title('Freight Charges over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[32]:


# Bar Chart (Coal Weight by Transporter)
plt.figure(figsize=(10, 6))
plt.bar(data['Tranporter Details'], data['Coal.Weight'])
plt.xlabel('Transporter Details')
plt.ylabel('Coal Weight')
plt.title('Coal Weight by Transporter')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# In[33]:


# Pie Chart (Distribution of Freight Charges by Transporter)
plt.figure(figsize=(8, 8))
plt.pie(data.groupby('Tranporter Details')['Freight Chrgs'].sum(), labels=data['Tranporter Details'].unique(), autopct='%1.1f%%')
plt.title('Distribution of Freight Charges by Transporter')
plt.show()


# In[34]:


# Scatter Plot (Coal Weight vs. Freight Charges)
plt.figure(figsize=(10, 6))
plt.scatter(data['Coal.Weight'], data['Freight Chrgs'])
plt.xlabel('Coal Weight')
plt.ylabel('Freight Charges')
plt.title('Coal Weight vs. Freight Charges')
plt.grid(True)
plt.show()


# In[ ]:




