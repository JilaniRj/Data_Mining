#!/usr/bin/env python
# coding: utf-8

# # Create reports and dashboards
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("nd.csv")
df


# In[3]:


df.drop('SR.NO.', axis=1)


# In[4]:


import seaborn as sns

# Convert numeric columns to numeric types
numeric_cols = [ 'WIGHT', 'RATE','AMOUNT', 'DEBIT']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col])
# Convert DATE column to datetime type
df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%m-%Y')
# Print the DataFrame
print(df)





# In[5]:


# Line plot of AMOUNT over DATE
plt.figure(figsize=(10, 6))
sns.lineplot(x='DATE', y='AMOUNT', data=df)
plt.title('Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[6]:


# Bar plot of AMOUNT for each VEHICLE_NO.
plt.figure(figsize=(12, 6))
sns.barplot(x='VEHICLE NO.', y='AMOUNT', data=df)
plt.title('Amount by Vehicle')
plt.xlabel('Vehicle Number')
plt.ylabel('Amount')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[7]:


# Histogram of WEIGHT
plt.figure(figsize=(8, 6))
sns.histplot(df['WIGHT'], bins=20, kde=True)
plt.title('Weight Distribution')
plt.xlabel('Weight')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


# In[8]:


# Box plot of AMOUNT
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['AMOUNT'])
plt.title('Amount Boxplot')
plt.xlabel('Amount')
plt.tight_layout()
plt.show()


# In[9]:


import matplotlib.pyplot as plt
# Define the bins for categorization
bins = [0, 25000, 50000, 75000, 100000, float('inf')]
labels = ['0-25k', '25k-50k', '50k-75k', '75-100K', '100k+']
# Create a new column with categories
df['AMOUNT_Category'] = pd.cut(df['AMOUNT'], bins=bins, labels=labels)
# Group by the categories and sum the amounts
amount_by_category = df.groupby('AMOUNT_Category')['AMOUNT'].sum()
# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(amount_by_category, labels=amount_by_category.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Amount')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[23]:


df=df.drop('AMOUNT_Category',axis=1)


# In[25]:


df=df.drop('CREDIT',axis=1)


# In[27]:


df=df.drop('RATE',axis=1)


# In[29]:


df=df.drop('SR.NO.',axis=1)


# In[30]:


df


# # Set up Jupyter Notebook for manipulating time series data frames using Pandas
# 

# In[10]:


data=pd.read_csv("nd.csv")
data


# In[11]:


data=data.drop(columns=['SR.NO.','CREDIT','RATE','VEHICLE NO.','DEBIT','WIGHT'])


# In[12]:


data['DATE']=pd.to_datetime(data['DATE'])


# In[13]:


data


# In[14]:


time_series = data.groupby('DATE')['AMOUNT'].sum()


# In[15]:


plt.figure(figsize=(10,6))
plt.plot(time_series.index,time_series.values,marker='o',linestyle='-')
plt.title('Time series of Amounts')
plt.xlabel("Date")
plt.ylabel("Amount")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[21]:


# Importing necessary libraries
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
# Reading the data
#data = pd.read_csv("your_data.csv")
# Preprocessing the data
data['DATE'] = pd.to_datetime(data['DATE'])  # Convert DATE column to datetime
data.set_index('DATE', inplace=True)
# Splitting data into training and testing sets
train = data.iloc[:int(0.8*len(data))]
test = data.iloc[int(0.8*len(data)):]
# Creating and fitting the ARIMA model
model = ARIMA(train, order=(5,1,0))  # Adjust order as needed
fitted_model = model.fit()
# Making predictions
predictions = fitted_model.forecast(steps=len(test))
# Plotting the forecast
plt.plot(test.index, test, label='Actual')
plt.plot(test.index, predictions, label='Predicted')
plt.legend()
plt.show()
# Evaluating the model
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(test, predictions)
print("Mean Absolute Error:", mae)


# # Build pricing forecast models

# In[31]:


df


# In[32]:


df['WIGHT']=pd.to_numeric(df['WIGHT'])
df['DEBIT']=pd.to_numeric(df['DEBIT'])


# In[ ]:


#linear regression


# In[33]:


# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# Reading the data
#data = pd.read_csv("your_data.csv")
# 'Wight' and 'Debit' are the features and 'Amount' is the target variable
X = df[['WIGHT', 'DEBIT']]
y = df['AMOUNT']
# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initializing and training the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Making predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
# Evaluating the model
train_mse = mean_squared_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)
print("Training Mean Squared Error:", train_mse)
print("Testing Mean Squared Error:", test_mse)


# In[ ]:


#ridge


# In[34]:


# Importing necessary libraries
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
# Initializing and training the Ridge regression model with cross-validation
model = Ridge(alpha=1.0)  # You can adjust the alpha parameter for regularization strength
cv_scores = cross_val_score(model, X_train, y_train, scoring='neg_mean_squared_error', cv=5)
avg_cv_mse = -cv_scores.mean()
# Training the model on the entire training set
model.fit(X_train, y_train)
# Making predictions on the testing set
y_pred_test = model.predict(X_test)
# Evaluating the model
test_mse = mean_squared_error(y_test, y_pred_test)
print("Cross-Validation Mean Squared Error:", avg_cv_mse)
print("Testing Mean Squared Error:", test_mse)


# In[ ]:


#feature engineering


# In[35]:


from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
# Hyperparameter Tuning: Search for the best value of alpha using cross-validation
from sklearn.model_selection import GridSearchCV
param_grid = {'alpha': [0.001, 0.01, 0.1, 1, 10, 100]}
ridge = Ridge()
grid_search = GridSearchCV(ridge, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train_poly, y_train)
best_alpha = grid_search.best_params_['alpha']
# Retrain the model with the best alpha
best_model = Ridge(alpha=best_alpha)
best_model.fit(X_train_poly, y_train)
# Evaluate the model on the testing set
y_pred_test = best_model.predict(X_test_poly)
test_mse = mean_squared_error(y_test, y_pred_test)
print("Best Alpha:", best_alpha)
print("Testing Mean Squared Error:", test_mse)


# In[ ]:




