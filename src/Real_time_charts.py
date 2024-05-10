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


data.info()


# In[5]:


data.describe()


# In[6]:


data['ProdDate']=pd.to_datetime(data['ProdDate'],format="mixed")


# In[7]:


data


# In[9]:


x=data['Equipment']
y=data['WorkHours']
plt.bar(x,y)


# In[10]:


z=data['FuelConsumed']
plt.bar(x,z)


# In[11]:


a=data['Availability']
plt.bar(x,a)


# In[12]:


df=pd.read_csv("MM2.csv")


# In[13]:


df


# In[14]:


df['Date']=pd.to_datetime(df['Date'])


# In[15]:


df


# In[16]:


df.info()


# In[17]:


df.describe()


# In[18]:


x=df['Date']
y=df['BlastsDone']
plt.bar(x,y)


# In[19]:


x=df['ExplosivesUsed']
y=df['BlastsDone']
plt.bar(x,y)


# In[25]:


a=pd.read_csv("MM3.csv")


# In[27]:


a


# In[28]:


a.info()


# In[29]:


a.describe()


# In[30]:


x=a['Equipment']
y=a['TotalOre']
plt.bar(x,y)


# In[31]:


x=a['Equipment']
y=a['StrippingRatio']
plt.bar(x,y)


# In[34]:


m4=pd.read_csv("mm4.csv")


# In[35]:


m4


# In[36]:


m4.info()


# In[37]:


m4.describe()


# In[38]:


x=m4['Equipment']
y=m4['FuelConsumed']
plt.bar(x,y)


# In[39]:


x=m4['Equipment']
y=m4['DistanceTravelled']
plt.bar(x,y)


# In[40]:


x=m4['Equipment']
y=m4['MaterialMoved']
plt.bar(x,y)


# In[ ]:





# In[41]:


m5=pd.read_csv("MM6.csv")


# In[42]:


m5


# In[43]:


m5.info()


# In[44]:


m5.describe()


# In[45]:


x=m5['EquipmentCategory']
y=m5['BreakDownHours']
plt.bar(x,y)


# In[ ]:





# In[55]:


m7=pd.read_csv("MM7.csv")


# In[56]:


m7


# In[57]:


m7.info()


# In[58]:


m7.describe()


# In[50]:


x=m7['HeavyEquipment']
y=m7['NoOfLoads']
plt.bar(x,y)


# In[59]:


x=m7['HeavyEquipment']
y=m7['AvgLoadWeight']
plt.bar(x,y)


# In[60]:


x=m7['HeavyEquipment']
y=m7['TotalWeightMaterialMoved']
plt.bar(x,y)


# In[ ]:





# In[61]:


m8=pd.read_csv("mm8.csv")


# In[62]:


m8


# In[63]:


m8['Date']=pd.to_datetime(m8['Date'])


# In[64]:


m8


# In[65]:


m8.info()


# In[66]:


m8.describe()


# In[67]:


x=m8['Equipment']
y=m8['Hours_Worked']
plt.bar(x,y)


# In[68]:


y=m8['Target_TPH']
plt.bar(x,y)


# In[69]:


y=m8['Actual TPH']
plt.bar(x,y)


# In[ ]:




