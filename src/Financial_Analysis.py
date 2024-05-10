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


data


# In[5]:


data.isnull().sum()


# In[6]:


data['Coal.Weight'].count()


# In[7]:


data['Coal.Weight']=data['Coal.Weight'].fillna(data['Coal.Weight'].mean())


# In[8]:


data.isnull().sum()


# In[9]:


data


# In[10]:


data.head()


# In[11]:


data.tail()


# In[12]:


data['Company Name'].unique()


# In[13]:


data['Contact Person No'].unique()


# In[14]:


data['Delivery Order No'].unique()


# In[15]:


data['Tranporter Details'].unique()


# In[16]:


data['Tranport C P'].nunique()


# In[17]:


data['Loading Point'].unique()


# In[18]:


data['Unloading Point'].unique()


# In[19]:


data['Freight Fair'].nunique()


# In[20]:


data=data.drop(columns = ['Loading Point','S.NO','Freight Fair','Unloading Point','Tranport C P','Delivery Order No','Contact Person No','Company Name'])


# In[21]:


data


# In[22]:


data=data.drop(columns=['Tranporter Details','Truck No.'])


# In[23]:


data


# In[24]:


data.info()


# In[25]:


#data['Date']=pd.to_datetime(data['Date'])


# In[26]:


data.info()


# In[27]:


data


# In[28]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')
# Convert 'Coal.Weight' and 'Freight Chrgs' to numeric
data['Coal.Weight'] = pd.to_numeric(data['Coal.Weight'])
data['Freight Chrgs'] = pd.to_numeric(data['Freight Chrgs'])

# Split data into features (X) and target (y)
X = data.drop(['Freight Chrgs'], axis=1)
y = data['Freight Chrgs']

X = X.select_dtypes(include='number')
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train Random Forest Regressor model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
# Make predictions on the test set
predictions = model.predict(X_test)
# Evaluate model
mse = mean_squared_error(y_test, predictions)
print('Mean Squared Error:', mse)






# In[29]:


data


# In[30]:


data['Year'] =data['Date'].dt.year
data['Month'] =data['Date'].dt.month


# In[31]:


data


# In[32]:


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor



from sklearn import tree
from sklearn.preprocessing import OneHotEncoder

from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.metrics import *
from sklearn import metrics


# In[33]:


x = data.drop(['Date','Freight Chrgs'], axis=1)


# In[34]:


y= data['Freight Chrgs']


# In[35]:


x


# In[36]:


y


# In[37]:


rf = RandomForestRegressor(n_estimators = 100)
rf.fit(x, y)
RandomForestRegressor()
# checking the feature importance



# In[38]:


x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, random_state = 0)


# In[39]:


lr = LinearRegression()
lr.fit(x_train, y_train)
LinearRegression()
y_pred = lr.predict(x_test)

from math import *
print("R2 Score: ", r2_score(y_test, y_pred))
print("MSE Score: ", mean_squared_error(y_test, y_pred))
print("RMSE : ", sqrt(mean_squared_error(y_test, y_pred)))


# In[40]:


#Decision Tree
dtree = DecisionTreeRegressor()
dtree.fit(x_train, y_train)
DecisionTreeRegressor()
y_pred1 = dtree.predict(x_test)


print("R2 Score: ", r2_score(y_test, y_pred1))
print("MSE Score: ", mean_squared_error(y_test, y_pred1))
print("RMSE : ", sqrt(mean_squared_error(y_test, y_pred1)))


# In[41]:


#Random Forest
rf1 = RandomForestRegressor(n_estimators = 100)
rf1.fit(x_train, y_train)
RandomForestRegressor()
y_pred2 = rf1.predict(x_test)


print("R2 Score: ", r2_score(y_test, y_pred2))
print("MSE Score: ", mean_squared_error(y_test, y_pred2))
print("RMSE : ", sqrt(mean_squared_error(y_test, y_pred2)))


# In[42]:


knn = KNeighborsRegressor()
knn.fit(x_train, y_train)
KNeighborsRegressor()
y_pred3 = knn.predict(x_test)


print("R2 Score: ", r2_score(y_test, y_pred3))
print("MSE Score: ", mean_squared_error(y_test, y_pred3))
print("RMSE : ", sqrt(mean_squared_error(y_test, y_pred3)))


# In[43]:


y_pred_final = (y_pred1 + y_pred2)/2.0


print("R2 Score: ", r2_score(y_test, y_pred_final))
print("MSE Score: ", mean_squared_error(y_test, y_pred_final))
print("RMSE : ", sqrt(mean_squared_error(y_test, y_pred_final)))


# In[ ]:




