#!/usr/bin/env python
# coding: utf-8

# # develop equipment specs

# In[2]:


#importing necessary libraries


# In[10]:


import csv
import pandas as pd
# creating class
class MiningEquipment:
    def __init__(self, name, equipment_capacity, equipment_power):# creating constructor
        self.name = name
        self.equipment_capacity = equipment_capacity
        self.equipment_power = equipment_power
        

    
    def get_equipment_specs(self):# function to equipment_specs
        return {
            'capacity': self.equipment_capacity,
            'power': self.equipment_power
        }
class MiningSimulation:# creating mining simulation
    def __init__(self, mining_equipment):# creating constructor
        
        self.mining_equipment = mining_equipment
        



    
#def read_data_from_file(file_path):
 #   with open(file_path, 'r') as file:
  #      reader = csv.DictReader(file)
   #     for lines in reader: 
    #        return lines


# Read data from CSV file
data = pd.read_excel('equipment1.xlsx')



# Define Mining Equipment
equipment = MiningEquipment(
    name=data['Equipment'],
    equipment_capacity=(data['Capacity']),
    equipment_power=(data['Power'])
)

# Initialize Simulation
mine_simulation = MiningSimulation(
    
    mining_equipment=equipment
    
)



# Get Equipment Specs

equipment_specs = mine_simulation.mining_equipment.get_equipment_specs()
print("\nSimulation Completed.")
print(f"Equipment : {data['Equipment']}.")
print(f"Equipment Capacity: {equipment_specs['capacity']} tons per hour")
print(f"Equipment Power: {equipment_specs['power']} kW")


# # develop integration

# In[8]:


#import necessary libraries
import csv
import pandas as pd

class OreDeposit:#creating class
    def __init__(self, name, total_reserve, average_grade):#creating constructor
        self.name = name
        self.total_reserve = total_reserve
        self.average_grade = average_grade
        
class MiningEquipment:#creating class
    def __init__(self, name, mining_rate):#creating constructor
        self.name = name
        self.mining_rate = mining_rate
        
    
        
class DrillingEquipment:#creating class
    def __init__(self, name, drilling_rate):#creating constructor
        self.name = name
        self.drilling_rate = drilling_rate
         


class HaulingEquipment:# creating class
    def __init__(self, name, hauling_rate, capacity, fuel_consumption_rate):#creating instructor
        self.name = name
        self.hauling_rate = hauling_rate
        self.capacity = capacity
        self.fuel_consumption_rate = fuel_consumption_rate
        self.current_fuel_level = 100  # Assuming full fuel tank initially

    def simulate_fuel_consumption(self, time_period):# function for fuel consumption simulation
        self.current_fuel_level -= self.fuel_consumption_rate * time_period

    def get_equipment_status(self):# function for equipment status
        return {
            'current_fuel_level': self.current_fuel_level
        }

class MiningSimulation:#creating class
    def __init__(self, ore_deposit, mining_equipment, drilling_equipment, hauling_equipment):#creating constructor
        self.ore_deposit = ore_deposit
        self.mining_equipment = mining_equipment
        self.drilling_equipment = drilling_equipment
        self.hauling_equipment = hauling_equipment
        
        self.current_reserve = ore_deposit.total_reserve
        self.extracted_ore = 0
        

    def simulate_extraction(self, time_period):# function for simulation extraction
        # Simulate drilling
        drilled_this_period = self.drilling_equipment.drilling_rate * time_period
        self.current_reserve -= drilled_this_period

        # Simulate mining
        mined_this_period = self.mining_equipment.mining_rate * time_period
        if self.current_reserve >= mined_this_period:
            self.extracted_ore += mined_this_period
            print(f"{mined_this_period} tons of ore extracted.")
        else:
            print("Not enough ore left to meet extraction demand.")

    def simulate_hauling(self, time_period):
        # Simulate hauling
        hauled_this_period = self.hauling_equipment.hauling_rate * time_period
        if self.extracted_ore >= hauled_this_period:
            self.extracted_ore -= hauled_this_period

            # Simulate fuel consumption
            self.hauling_equipment.simulate_fuel_consumption(time_period)

            print(f"{hauled_this_period} tons of ore hauled.")
        else:
            print("Not enough ore extracted to meet hauling demand.")

    def get_extraction_status(self):#function for extraction status
        return {
            'current_reserve': self.current_reserve,
            'extracted_ore': self.extracted_ore
            
        }

    def get_equipment_statuses(self):#function for equipment status
    
        hauling_status = self.hauling_equipment.get_equipment_status()

        return {
            
            'hauling_status': hauling_status
        }

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = next(reader)  
        return data


# Read data from CSV file
data = read_data_from_file('quipment.csv')

# Define Ore Deposit
gold_deposit = OreDeposit(
    name=data['ore_name'],
    total_reserve=float(data['total_reserve']),
    average_grade=float(data['average_grade'])
)

# Define Mining Equipment
excavator = MiningEquipment(
    name=data['Equipment'],
    mining_rate=float(data['mining_rate'])
    
)

# Define Drilling Equipment
drill = DrillingEquipment(
    name=data['drilling_equipment_name'],
    drilling_rate=float(data['drilling_rate'])
    
)

# Define Hauling Equipment
truck = HaulingEquipment(
    name=data['hauling_equipment_name'],
    hauling_rate=float(data['hauling_rate']),
    capacity=float(data['haul_capacity']),
    fuel_consumption_rate=float(data['Fuel_consumed'])
)

# Initialize Simulation
mine_simulation = MiningSimulation(
    ore_deposit=gold_deposit,
    mining_equipment=excavator,
    drilling_equipment=drill,
    hauling_equipment=truck
)

# Simulate Extraction and Hauling for 10 time periods
for _ in range(10):
    mine_simulation.simulate_extraction(time_period=1)
    mine_simulation.simulate_hauling(time_period=1)

# Get Extraction Status and Equipment Statuses
extraction_status = mine_simulation.get_extraction_status()
equipment_statuses = mine_simulation.get_equipment_statuses()

print("\nSimulation Completed.")
print(f"Current Reserve: {extraction_status['current_reserve']} tons")
print(f"Total Extracted: {extraction_status['extracted_ore']} tons")


print("\nEquipment Statuses:")

print(f"Hauling Equipment Fuel Level: {equipment_statuses['hauling_status']['current_fuel_level']}%")


# # Constructing mine sections - surface, underground integration with the code already written

# In[36]:


#importing necessary libraries
import csv
import pandas as pd

class OreDeposit:#create class
    def __init__(self, name, total_reserve, average_grade):#creating constructor
        self.name = name
        self.total_reserve = total_reserve
        self.average_grade = average_grade

class DrillingEquipment:#create class
    def __init__(self, name, drilling_rate):#create constructor
        self.name = name
        self.drilling_rate = drilling_rate
        
    
class HaulingEquipment:#create class
    def __init__(self, name, hauling_rate, capacity, fuel_consumption_rate):#create constructor
        self.name = name
        self.hauling_rate = hauling_rate
        self.capacity = capacity
        self.fuel_consumption_rate = fuel_consumption_rate
        self.current_fuel_level = 100  # Assuming full fuel tank initially

    def simulate_fuel_consumption(self, time_period):#function for simulating fuel consumption
        self.current_fuel_level -= self.fuel_consumption_rate * time_period

    def get_equipment_status(self):#function for equipment status
        return {
            'current_fuel_level': self.current_fuel_level
        }

class SurfaceMineSection:#create class
    def __init__(self, depth,length,width):#create constructor
        self.depth = depth
        self.length = length
        self.width = width
        

class UndergroundMineSection:#create class
    def __init__(self,depth,length,width ):# create constructor
        self.depth = depth
        self.length = length
        self.width = width
        
class MiningSimulation:#create class
    def __init__(self, mine_section):#create constructor
        self.mine_section = mine_section
        
    def simulate_extraction(self, time_period):#function for simulating extraction
        # Simulate drilling
        drilled_this_period = self.mine_section.drilling_equipment.drilling_rate * time_period
        self.current_reserve -= drilled_this_period

        # Simulate mining
        mined_this_period = self.mine_section.mining_equipment.mining_rate * time_period
        if self.current_reserve >= mined_this_period:
            self.extracted_ore += mined_this_period

            print(f"{mined_this_period} tons of ore extracted from {self.mine_section.name}.")
        else:
            print(f"Not enough ore left in {self.mine_section.name} to meet extraction demand.")

    def simulate_hauling(self, time_period):
        # Simulate hauling
        hauled_this_period = self.mine_section.hauling_equipment.hauling_rate * time_period
        if self.extracted_ore >= hauled_this_period:
            self.extracted_ore -= hauled_this_period

            # Simulate fuel consumption
            self.mine_section.hauling_equipment.simulate_fuel_consumption(time_period)

            print(f"{hauled_this_period} tons of ore hauled from {self.mine_section.name}.")
        else:
            print(f"Not enough ore extracted in {self.mine_section.name} to meet hauling demand.")

    def get_extraction_status(self):# function for extraction status
        return {
            'current_reserve': self.current_reserve,
            'extracted_ore': self.extracted_ore
            
        }

    def get_equipment_statuses(self):#function for equipment status
        
        hauling_status = self.mine_section.hauling_equipment.get_equipment_status()

        return {
            
            'hauling_status': hauling_status
        }

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = next(reader)  
        return data




# Read data from CSV file
data_list = read_data_from_file('quipment.csv')


    # Define Ore Deposit
ore_deposit = OreDeposit(
        name=data['ore_name'],
        total_reserve=float(data['total_reserve']),
        average_grade=float(data['average_grade'])
    )

    # Define Mining Equipment
mining_equipment = MiningEquipment(
        name=data['Equipment'],
        mining_rate=(data['mining_rate'])

        
    )

    # Define Drilling Equipment
drilling_equipment = DrillingEquipment(
        name=data['drilling_equipment_name'],
        drilling_rate=float(data['drilling_rate'])
        
    )

    # Define Hauling Equipment
hauling_equipment = HaulingEquipment(
        name=data['hauling_equipment_name'],
        hauling_rate=float(data['hauling_rate']),
        capacity=float(data['haul_capacity']),
        fuel_consumption_rate=float(data['Fuel_consumed'])
    )

    # Define Surface Mine Section
surface_mine_section = SurfaceMineSection(
        depth=data["Depth"],
        length=data["Length"],
        width=data["Width"]
    )

    # Define Underground Mine Section
underground_mine_section = UndergroundMineSection(
        depth=data["Depth"],
        length=data["Length"],
        width=data["Width"]
        
    )

    # Initialize Surface Mine Simulation
surface_mine_simulation = MiningSimulation(
        mine_section=surface_mine_section
    
    )

    
    # Initialize Underground Mine Simulation
underground_mine_simulation = MiningSimulation(
        mine_section=underground_mine_section
    )

    
print("\nSurface Mine Simulation Completed:")
    
    

   
print("\nUnderground Mine Simulation Completed:")
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


pip install pyautogui


# In[4]:


import pyautogui
import time

while True:

    time.sleep(5)

    x,y= pyautogui.position()
    pyautogui.click(x,y)


# In[ ]:




