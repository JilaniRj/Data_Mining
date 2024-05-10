#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data=pd.read_csv("mm.csv")


# In[3]:


data


# In[4]:


data.shape


# In[5]:


data.size


# In[6]:


data.info()


# In[7]:


data.describe()


# In[8]:


data.isnull().sum()


# In[9]:


data.head()


# In[10]:


data.tail()


# In[14]:


data['ProdDate']=pd.to_datetime(data['ProdDate'],format="mixed")


# In[15]:


data


# In[ ]:


##100% availability of iron ore in geoth mine ,which can be extracted within 7 hours of mining using Komatsu Dump Truck is the 
#best choice to increase the production rate of iron .


# # second set


# In[16]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[17]:


df=pd.read_csv("MM2.csv")


# In[18]:


df


# In[19]:


df['Date']=pd.to_datetime(df['Date'])


# In[20]:


df


# In[21]:


df.info()


# In[22]:


df.describe()


# In[23]:


df


# In[24]:


##B7 South blockid is better to use because 18250T ore is extracted by 2 blasts with 2100kg emulsion.


# # THIRD SET


# In[25]:


a=pd.read_csv("MM3.csv")


# In[26]:


a


# In[27]:


#In surface mining, stripping ratio or strip ratio refers to the amount of waste (or overburden) 
#that must be removed to release a given ore quantity.


# In[28]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

a['TotalOre']=le.fit_transform(a['TotalOre'])


# In[29]:


a.info()


# In[30]:


a.plot(x='Equipment',y='TotalOre',kind='bar')


# # fourthset


# In[31]:


m4=pd.read_csv("mm4.csv")


# In[32]:


m4


# In[33]:


#Truck1 is more efficient as it travelled 800km compared to Truck2


# # fifth set


# In[34]:


m5=pd.read_csv("MM6.csv")


# In[35]:


m5


# In[36]:


#35T Dump Truck is better as breakdown hour is 0.


# # sixth set


# In[37]:


m7=pd.read_csv("MM7.csv")


# In[38]:


m7


# In[40]:


m7


# In[41]:


#PC200 CAT Excavator has 105kg load and total weight moved is 1312500kg.


# # seventh set


# In[42]:


m8=pd.read_csv("mm8.csv")


# In[43]:


m8


# In[44]:


m8['Date']=pd.to_datetime(m8['Date'])


# In[45]:


m8


# In[ ]:


#total Petroleum Hydrocarbons (TPH) is a term used to describe a broad family of several hundred chemical
#compounds that originally come from crude oil.


# In[46]:


m8.plot(x='Equipment',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Equipment")
plt.ylabel("Target_TPH V/S Actual_TPH")
plt.title("Equipment v/s TPH")


# In[47]:


m8.plot(x='Operator',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Operator")
plt.ylabel("TPH")
plt.title("Operator vs TPH")


# In[48]:


m8.plot(x='Mine',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Mine")
plt.ylabel("TPH")
plt.title("Mine vs TPH")


# In[ ]:






# In[ ]:




