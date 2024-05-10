#!/usr/bin/env python
# coding: utf-8

# # develop environment specs

# In[12]:


#importing necessary libraries
import csv
import pandas as pd
# creating class
class Environment:
    def __init__(self, type, depth, length, width):# creating constructor
        self.type = type
        self.depth = depth
        self.length = length
        self.width= width
        

    
    def get_environment_specs(self):# function to environment_specs
        return {
            'depth': self.depth,
            'length': self.length,
            'width': self.width      
        }
class MiningSimulation:# creating mining simulation
    def __init__(self, environment):# creating constructor
        
        self.environment = environment



    
def read_data_from_file(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        environments=[]
        for row in reader: 
            environment=Environment(
                type=row['Type'],
                depth=row['Depth'],
                length=row['Length'],
                width=row['Width']
            )
            environments.append(environment)
        return environments


# Read data from CSV file
environments = read_data_from_file('geo.csv')



# Initialize Simulation
mine_simulations = []
for environment in environments:
    mine_simulation=MiningSimulation(environment)
    mine_simulations.append(mine_simulation)
    
#print environment specs for each simulation
for i, mine_simulation in enumerate(mine_simulations):
    environment_specs=mine_simulation.environment.get_environment_specs()
    print(f"Simulation {i+1}: ")
    print(f"Environment: {mine_simulation.environment.type}")
    print(f"Depth: {environment_specs['depth']} m")
    print(f"Length: {environment_specs['length']} m")
    print(f"Width : {environment_specs['width']} m")
    print()
    







# # develop integration with drilling and hauling

# In[14]:


#importing necessary libraries
import csv
import pandas as pd
class Environment:
    def __init__(self, type, depth, length, width):
        self.type = type
        self.depth = depth
        self.length = length
        self.width = width
    def get_environment_specs(self):
        return {
            'depth': self.depth,
            'length': self.length,
            'width': self.width
        }
class MiningSimulation:
    def __init__(self, environment):
        self.environment = environment
    def drill(self):
        # Placeholder for drilling functionality
        print("Drilling operation initiated in", self.environment.type)
    def haul(self):
        # Placeholder for hauling functionality
        print("Hauling operation initiated in", self.environment.type)
def read_data_from_file(file_path):
    environments = []
    try:
        data = pd.read_csv(file_path)
        for _, row in data.iterrows():
            environment = Environment(
                type=row['Type'],
                depth=(row['Depth']),
                length=(row['Length']),
                width=(row['Width'])
            )
            environments.append(environment)
    except Exception as e:
        print("Error reading data from CSV:", e)
    return environments
# Read data from CSV file
file_path = 'geo.csv'
environments = read_data_from_file(file_path)
# Initialize Simulation for each environment
mine_simulations = [MiningSimulation(env) for env in environments]
# Perform drilling and hauling for each Simulation
for i, mine_simulation in enumerate(mine_simulations):
    print(f"Simulation {i+1}:")
    mine_simulation.drill()
    mine_simulation.haul()
    print()


# In[ ]:




