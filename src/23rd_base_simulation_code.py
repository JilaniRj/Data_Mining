#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing necessary libraries
import pandas as pd


# # importing data from mm

# In[2]:


data=pd.read_csv("mm.csv")
data


# In[3]:


data2=pd.read_csv("MM2.CSV")
data2


# In[5]:


data3=pd.read_csv("MM3.csv")
data3


# In[6]:


data4=pd.read_csv("mm4.csv")
data4


# In[7]:


data5=pd.read_csv("MM5.csv")
data5


# In[8]:


data6=pd.read_csv("MM6.csv")
data6


# In[9]:


data7=pd.read_csv("MM7.csv")
data7


# In[10]:


data8=pd.read_csv("mm8.csv")
data8


# # importing data 

# In[19]:


df=pd.read_excel("quipment.xlsx")
df


# In[20]:


df2=pd.read_excel("geo.xlsx")
df2


# In[21]:


df3=pd.read_excel("utility.xlsx")
df3


# # class definitions

# In[2]:


class Equipment:#class creation
    def __init__(self, name, type, capacity, power,utilization,mtbf,mttr):# creating constructor
        self.name = name
        self.type = type
        self.capacity = capacity
        self.power = power
        self.utilization=utilization
        self.mtbf=mtbf
        self.mttr=mttr
        
    def __str__(self):# creating constructor
        return f"{self.name} - {self.type} - {self.capacity} - {self.power} - {self.utilization} - {self.mtbf} - {self.mttr}"
    
class Environment:#class creation
    def __init__(self, section,type, depth, length,width):# creating constructor
        self.section = section
        self.type = type
        self.depth = depth
        self.length = length
        self.width=width
    def __str__(self):# creating constructor
        return f"{self.section} - type: {self.type}, depth: {self.depth}, length: {self.length}, width : {self.width}"

#importing data
equipment_objects = [
    Equipment("Drill1", "Rotary", 706.29, 4500,0.6,300,48),
             ("Drill2", "Hammer",529.72,3500,0,0,0),
              ("Truck1","Diesel",100,4362.34,0.75,200,24),
              ("Truck2","Diesel",100,4362.34,0.9,200,48),
              ("Loader","Electrical",3.24,2000,0,0,0),
              ("Truck1a","Diesel",100,4362.34,1.35,200,48),
              ("Truck1b","Diesel",100,4362.34,1.5,300,24),
              ("Truck1c","Diesel",100,4362.34,1.65,300,24),
              ("Truck1d","Diesel",100,4362.34,1.8,300,24)
]
environment_objects = [#importing given data
    Environment("east","surface",200,1000,800),
               ("east","surface",200,1000,800),
            ("east","surface",200,10250,400),
             ("east","surface",200,12080,400),
              ("east","surface",200,10250,400),
             ("west","underground",200,12081,400),
             ("west","underground",200,10250,400),
             ("west","underground",200,10250,400),
             ("west","underground",800,500,10)
]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import pandas as pd
# Load CSV file into a DataFrame
file_path = 'equipment.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)
# Extract unique equipment names
equipment_names = df['Equipment'].unique()
# Initialize a dictionary to store equipment specs
equipment_specs = {}
# Iterate through each equipment type
for equipment_name in equipment_names:
    # Filter rows for the current equipment
    equipment_df = df[df['Equipment'] == equipment_name]
    # Extract and store unique capacity and power values
    capacity_values = equipment_df['Capacity'].unique()
    power_values = equipment_df['Power'].unique()
    # Store equipment specs in the dictionary
    equipment_specs[equipment_name] = {
        'Capacity': capacity_values.tolist(),
        'Power': power_values.tolist()
    }
# Print the equipment specifications
for equipment, specs in equipment_specs.items():
    print(f"{equipment} Specs:")
    print(f"Capacity: {specs['Capacity']}")
    print(f"Power: {specs['Power']}\n")


# In[ ]:


.import random
# Sample CSV data (replace this with your actual data)
csv_data = """
Drilling,Type,Capacity,Power,Cost,Section,Type,Depth,Length,Width
Drill1,Rotary,2000m,4500kW,NA,East,Surface,200m,1000m,800m
Drill2,Hammer,1500m,3500kW,NA,East,Surface,200m,1000m,800m
Truck1,Diesel,100t,5850HP,NA,East,Surface,200m,10250m,400m
Truck2,Diesel,100t,5850HP,NA,East,Surface,200m,10250m,400m
Loader1,Electrical,12yd3,2000kW,NA,West,Underground,200m,12081m,400m
Loader1,Electrical,12yd3,2000kW,NA,West,Underground,200m,10250m,400m
Loader1,Electrical,12yd3,2000kW,NA,West,Underground,200m,10250m,400m
Loader1,Electrical,12yd3,2000kW,NA,West,Underground,800m,500m,10m
"""
# Split CSV data into lines
lines = csv_data.strip().split('\n')
# Extract relevant information into dictionaries
drilling_data = {}
hauling_data = {}
for line in lines[1:]:  # Skip header
    fields = line.split(',')
    equipment_type = fields[0].strip()
    if "Drill" in equipment_type:
        drilling_data[equipment_type] = {
            'type': fields[1].strip(),
            'capacity': fields[2].strip(),
            'power': fields[3].strip(),
            'depth': fields[7].strip(),
        }
    elif "Truck" in equipment_type:
        hauling_data[equipment_type] = {
            'type': fields[1].strip(),
            'capacity': fields[2].strip(),
            'power': fields[3].strip(),
            'length': fields[8].strip(),
            'width': fields[9].strip(),
        }
# Simulation function
def simulate_drilling_and_hauling(drilling_data, hauling_data):
    for drill, drill_info in drilling_data.items():
        print(f"Simulating drilling with {drill}: {drill_info['depth']} depth.")
        # Simulate hauling after drilling
        for truck, truck_info in hauling_data.items():
            print(f"Hauling with {truck}: {truck_info['length']} length, {truck_info['width']} width.")
            # Simulate loading with loader
            print("Loading with Loader1.")
            # Add any additional simulation logic as needed
            # Calculate costs or other metrics based on simulation
            print("\n")
# Run the simulation
simulate_drilling_and_hauling(drilling_data, hauling_data)


# In[1]:


import random
# Sample CSV data (replace this with your actual data)
csv_data = """
Drilling,Type,Capacity,Power,Cost,Section,Type,AreaDepth,AreaLength,AreaWidth
Drill1,Rotary,2000m,4500kW,NA,Surface,Surface,200m,1000m,800m
Drill2,Hammer,1500m,3500kW,NA,Surface,Surface,200m,1000m,800m
Truck1,Diesel,100t,5850HP,NA,Surface,Surface,200m,10250m,400m
Truck2,Diesel,100t,5850HP,NA,Surface,Surface,200m,10250m,400m
Loader1,Electrical,12yd3,2000kW,NA,Underground,Underground,200m,12081m,400m
Loader1,Electrical,12yd3,2000kW,NA,Underground,Underground,200m,10250m,400m
Loader1,Electrical,12yd3,2000kW,NA,Underground,Underground,200m,10250m,400m
Loader1,Electrical,12yd3,2000kW,NA,Underground,Underground,800m,500m,10m
"""
# Split CSV data into lines
lines = csv_data.strip().split('\n')
# Extract relevant information into dictionaries
drilling_data = {}
hauling_data = {}
construction_data = {}
for line in lines[1:]:  # Skip header
    fields = line.split(',')
    equipment_type = fields[0].strip()
    if "Drill" in equipment_type:
        drilling_data[equipment_type] = {
            'type': fields[1].strip(),
            'capacity': fields[2].strip(),
            'power': fields[3].strip(),
            'area_depth': fields[7].strip(),
            'area_length': fields[8].strip(),
            'area_width': fields[9].strip(),
            'section': fields[5].strip(),
        }
    elif "Truck" in equipment_type:
        hauling_data[equipment_type] = {
            'type': fields[1].strip(),
            'capacity': fields[2].strip(),
            'power': fields[3].strip(),
            'area_length': fields[8].strip(),
            'area_width': fields[9].strip(),
            'section': fields[5].strip(),
        }
    elif "Loader" in equipment_type:
        construction_data[equipment_type] = {
            'type': fields[1].strip(),
            'capacity': fields[2].strip(),
            'power': fields[3].strip(),
            'area_length': fields[8].strip(),
            'area_width': fields[9].strip(),
            'section': fields[5].strip(),
        }
# Simulation function
def simulate_mine_operations(drilling_data, hauling_data, construction_data):
    for drill, drill_info in drilling_data.items():
        print(f"Simulating drilling with {drill} in {drill_info['section']} section: {drill_info['area_depth']} depth, {drill_info['area_length']} length, {drill_info['area_width']} width.")
        # Simulate hauling after drilling
        for truck, truck_info in hauling_data.items():
            print(f"Hauling with {truck} in {truck_info['section']} section: {truck_info['area_length']} length, {truck_info['area_width']} width.")
            # Simulate loading with loader
            for loader, loader_info in construction_data.items():
                print(f"Constructing with {loader} in {loader_info['section']} section: {loader_info['area_length']} length, {loader_info['area_width']} width.")
                # Add any additional simulation logic as needed
                # Calculate costs or other metrics based on simulation
                print("\n")
# Run the simulation
simulate_mine_operations(drilling_data, hauling_data, construction_data)














# In[ ]:




