#!/usr/bin/env python
# coding: utf-8

# # 2.	To showcase improvement in asset utilization rates percentage wise 

# In[3]:


# Utilization rates for each equipment
utilization_rates = {
    'drill1': 0.6,
    'truck1a': 0.75,
    'truck2a': 0.9,
    'truck3' :1.05,
     'truck4' : 1.2,
    'truck1b': 1.35,
    'truck1c': 1.5,
    'truck1d': 1.65,
    'truck1e': 1.8,
    'truck2b': 0.58
}
# Reference utilization rate
reference_utilization_rate = 0.55# sample number
# Calculate percentage change for each equipment
percentage_changes = {equipment: ((utilization_rate - reference_utilization_rate) / reference_utilization_rate) * 100
                      for equipment, utilization_rate in utilization_rates.items()}
# Print percentage changes for each equipment
for equipment, change in percentage_changes.items():
    print(f"{equipment}: {change:.2f}% change")


# # 1.	To showcase average monthly production

# In[4]:


# Monthly production data (tons)
monthly_production = {
    'January': 5460,
    'February': 436393,
    'March': 1370000,
    'May': 7370
    
    
}
# Calculate total production
total_production = sum(monthly_production.values())

# Calculate the number of months
num_months = len(monthly_production)

# Calculate the average monthly production
average_monthly_production = total_production / num_months
print(f"The average monthly production in mining is {average_monthly_production:.2f} tons")


# # 3.	To showcase Reduced maintenance if any by referring to the overall data provided till date 

# In[6]:


#importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Given hours of usage for each equipment
equipment = ['drill1','truck1a','truck2a','truck3','truck4','truck1b','truck1c','truck1d','truck1e','truck2b','loader','dump truck','shovel1','truck1f','truck2c','dragline1','truck1g']
hours_of_usage = [300,200,200,200,200,200,200,300,300,300,8,7,8,8,8,10,10]
 
# Creating a DataFrame
df = pd.DataFrame({'Equipment': equipment, 'Hours_of_Usage': hours_of_usage})
# Plotting the results
plt.figure(figsize=(10, 6))
plt.bar(df['Equipment'], df['Hours_of_Usage'], color='skyblue')
plt.title('Hours of Usage per Equipment')
plt.xlabel('Equipment')
plt.ylabel('Hours of Usage')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# In[ ]:




