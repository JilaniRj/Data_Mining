#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#https://www.analyticsvidhya.com/blog/2022/02/optimal-resource-allocation-using-python/


# # Python script for resource optimization using optimization libraries
# 

# In[1]:


import pandas as pd
import pulp as plp
import numpy as np


# In[2]:


get_ipython().system('pip install pulp')


# In[2]:


df=pd.read_csv("mm8.csv")


# In[3]:


df


# In[7]:


location_df=df.iloc[:,[6,8]]


# In[8]:


location_df


# In[9]:


work_df=df.iloc[:,[2,9]]


# In[10]:


work_df


# In[11]:


model = plp.LpProblem("Resource_allocation_prob", plp.LpMinimize)


# In[13]:


no_of_location = location_df.shape[0]
no_of_work = work_df.shape[0]
x_vars_list = []
for l in range(1,no_of_location+1):
    for w in range(1,no_of_work+1):
        temp = str(l)+str(w)
        x_vars_list.append(temp)
x_vars = plp.LpVariable.matrix("R", x_vars_list, cat = "Integer", lowBound = 0)
final_allocation = np.array(x_vars).reshape(6,6)
print(final_allocation)


# In[ ]:


#res_equation = plp.lpSum(final_allocation*resource_cost)
#model +=  res_equation


# In[15]:


for l1 in range(no_of_location):
    model += plp.lpSum(final_allocation[l1][w1] for w1 in range(no_of_work)) <= location_df['Target_TPH'].tolist()[l1]
for w2 in range(no_of_work):
    model += plp.lpSum(final_allocation[l2][w2] for l2 in range(no_of_location)) >= work_df['Actual TPH'].tolist()[w2]


# In[16]:


model


# In[17]:


model.solve()
status = plp.LpStatus[model.status]
print(status)


# In[ ]:


#print("Optimal overall resouce cost: ",str(plp.value(model.objective)))
#for each in model.variables():
 #   print("Optimal cost of ", each, ": "+str(each.value()))


# # Git for version control of the optimization tool

# ![Screenshot%20%283%29.png](attachment:Screenshot%20%283%29.png)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[18]:


get_ipython().system('pip install scipy')


# In[19]:


from scipy.optimize import minimize

# Objective function to minimize
def objective_function(x):
    # In this example, the objective function is a simple quadratic function
    return x[0]**2 + 4 * x[1]**2

# Constraint function
def constraint(x):
    # In this example, there is a simple linear constraint
    return x[0] + x[1] - 1

# Initial guess
initial_guess = [0.5, 0.5]

# Define bounds for variables
bounds = [(0, None), (0, None)]  # Non-negativity constraint for both variables

# Define constraints
constraints = ({'type': 'eq', 'fun': constraint})

# Use the minimize function to find the optimal solution
result = minimize(objective_function, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

# Print the result
print("Optimal solution:")
print("x =", result.x)
print("Optimal value =", result.fun)


# In[ ]:




