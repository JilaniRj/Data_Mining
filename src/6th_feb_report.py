#!/usr/bin/env python
# coding: utf-8

# # create repos with pandas and matplotlib
# 

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv("annual_data.csv")


# In[3]:


a=df['Period'].head(80)
b=df['Inst_sector_code'].head(80)

plt.bar(a,b)


# In[4]:


x=df['Period']
y=df['Asset_liability_code']
plt.bar(x,y)


# In[5]:


x=df['Period']
y=df['Inst_sector']
plt.bar(x,y)


# # overlay density maps

# In[7]:


data=pd.read_csv("mm8.csv")


# In[9]:


data.plot(x='Equipment',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Equipment")
plt.ylabel("Target_TPH V/S Actual_TPH")
plt.title("Equipment v/s TPH")


# In[10]:


data.plot(x='Operator',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Operator")
plt.ylabel("TPH")
plt.title("Operator vs TPH")


# In[11]:


data.plot(x='Mine',y=['Target_TPH','Actual TPH'],kind='bar')
plt.xlabel("Mine")
plt.ylabel("TPH")
plt.title("Mine vs TPH")


# In[ ]:





# # interactive data visualization , framework,log format

# In[1]:


import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objs as go
import logging


# In[2]:


app = dash.Dash()
app.layout = html.Div(children=[
   html.H1(children='Hello Dash'),
   html.Div(children='Dash Framework: A web application framework for Python')])


# In[3]:


df = pd.read_csv('mm8.csv')
df['Date']=pd.to_datetime(df['Date'])
logging.warning('date format is set to yyyy-mm-dd format')
def generate_table(dataframe, max_rows=10):
    return html.Table(
      # Header
      [html.Tr([html.Th(col) for col in dataframe.columns])] +
      # Body
      [html.Tr([
         html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
      ]) for i in range(min(len(dataframe), max_rows))]
   )
app = dash.Dash()
app.layout = html.Div(children=[
   html.H4(children='Material Management Data'),
   generate_table(df)
])
if __name__ == '__main__':
    app.run_server(debug=True)


# In[4]:


app.layout = html.Div([
   dcc.Graph(
      id='Material Management',
      figure={
         'data': [
            go.Scatter(
               x=df[df['Equipment'] == i]['Target_TPH'],
               y=df[df['Equipment'] == i]['Actual TPH'],
               text=df[df['Equipment'] == i],
               mode='markers',
               opacity=0.7,
               marker={
                  'size': 15,
                  'line': {'width': 0.5, 'color': 'white'}
               },
               name=i
            ) for i in df.Equipment.unique()
         ],
         'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'Expected TPH'},
            yaxis={'title': 'Actual TPH'},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
         )
      }
   )
])

if __name__ == '__main__':
    app.run_server()


# # plot real - time charts

# In[16]:


data1=pd.read_csv("mm.csv")


# In[17]:


x=data1['Equipment']
y=data1['WorkHours']
plt.bar(x,y)


# In[18]:


z=data1['FuelConsumed']
plt.bar(x,z)


# In[19]:


a=data1['Availability']# availability of equipment is considered
plt.bar(x,a)


# In[20]:


df1=pd.read_csv("MM2.csv")


# In[21]:


x=df1['Date']
y=df1['BlastsDone']
plt.bar(x,y)


# In[22]:


x=df1['ExplosivesUsed']
y=df1['BlastsDone']
plt.bar(x,y)


# In[23]:


a=pd.read_csv("MM3.csv")


# In[24]:


x=a['Equipment']
y=a['TotalOre']
plt.bar(x,y)


# In[25]:


x=a['Equipment']
y=a['StrippingRatio']
plt.bar(x,y)


# In[26]:


m4=pd.read_csv("mm4.csv")


# In[27]:


x=m4['Equipment']
y=m4['FuelConsumed']
plt.bar(x,y)


# In[28]:


x=m4['Equipment']
y=m4['DistanceTravelled']
plt.bar(x,y)


# In[29]:


x=m4['Equipment']
y=m4['MaterialMoved']
plt.bar(x,y)


# In[30]:


m5=pd.read_csv("MM6.csv")


# In[31]:


x=m5['EquipmentCategory']
y=m5['BreakDownHours']
plt.bar(x,y)


# In[32]:


m7=pd.read_csv("MM7.csv")


# In[33]:


x=m7['HeavyEquipment']
y=m7['NoOfLoads']
plt.bar(x,y)


# In[34]:


x=m7['HeavyEquipment']
y=m7['AvgLoadWeight']
plt.bar(x,y)


# In[35]:


x=m7['HeavyEquipment']
y=m7['TotalWeightMaterialMoved']
plt.bar(x,y)


# In[36]:


x=data['Equipment']
y=data['Hours_Worked']
plt.bar(x,y)


# In[37]:


y=data['Target_TPH']
plt.bar(x,y)


# In[38]:


y=data['Actual TPH']
plt.bar(x,y)


# In[42]:


df=pd.read_csv("annual_data.csv")

plt.hist(df['Inst_sector_code'])


# In[43]:


x=df['Period']
y=df['Asset_liability_code']
plt.scatter(x,y)


# In[44]:


plt.bar(x,y)


# # develop intgration in equipment

# In[66]:


import matplotlib.pyplot as plt
# Simulation variables
simulation_periods = range(1, 11)  # Assuming 10 time periods
# Lists to store data for plotting
extracted_ore_over_time = []
fuel_level_over_time = []
# Simulate Extraction and Hauling for 10 time periods
for period in simulation_periods:
    mine_simulation.simulate_extraction(time_period=1)
    mine_simulation.simulate_hauling(time_period=1)
    # Collect data for plotting
    extraction_status = mine_simulation.get_extraction_status()
    equipment_statuses = mine_simulation.get_equipment_statuses()
    extracted_ore_over_time.append(extraction_status['extracted_ore'])
    fuel_level_over_time.append(equipment_statuses['hauling_status']['current_fuel_level'])
# Plotting
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(simulation_periods, extracted_ore_over_time, marker='o', linestyle='-')
plt.title('Ore Extraction Over Time')
plt.xlabel('Time Period')
plt.ylabel('Extracted Ore (tons)')
plt.subplot(2, 1, 2)
plt.plot(simulation_periods, fuel_level_over_time, marker='o', linestyle='-')
plt.title('Hauling Equipment Fuel Level Over Time')
plt.xlabel('Time Period')
plt.ylabel('Fuel Level (%)')
plt.tight_layout()
plt.show()


# # develop equipment specs

# In[6]:


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


# In[3]:


import matplotlib.pyplot as plt
class Equipment:# creating class
    def __init__(self, name, capacity, power):# creating constructor
        self.name = name
        self.capacity = capacity
        self.power = power
        
def generate_plans(equipment_list):
    plans = []
    for equipment in equipment_list:
        plans.append(f"Plan for {equipment.capacity} {equipment.power} {equipment.name}(s)")
    return plans
equipment_list = [
    Equipment("Drill1", 2000, 4500),
    Equipment("Drill2", 1500, 3500),
    Equipment("Truck1", 283.16, 4362.34),
    Equipment("Truck1", 283.16, 4362.34),
    Equipment("Truck2", 283.16, 4362.34),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000)
]
# Extracting equipment names, capacities, and powers
equipment_names = [equipment.name for equipment in equipment_list]
capacities = [equipment.capacity for equipment in equipment_list]
powers = [equipment.power for equipment in equipment_list]
# Creating a bar chart for capacities and powers
fig, ax = plt.subplots(2, 1, figsize=(10, 8))
ax[0].bar(equipment_names, capacities, color='blue')
ax[0].set_ylabel('Capacity')
ax[0].set_title('Equipment Capacities')
ax[1].bar(equipment_names, powers, color='green')
ax[1].set_ylabel('Power')
ax[1].set_title('Equipment Powers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()







# # develop integration with drilling and hauling

# In[3]:


#importing necessary libraries
import csv
import pandas as pd
class Environment:#created class
    def __init__(self, type, depth, length, width):#creating constructor
        self.type = type
        self.depth = depth
        self.length = length
        self.width = width
    def get_environment_specs(self):#function to get environment specs
        return {
            'depth': self.depth,
            'length': self.length,
            'width': self.width
        }
class MiningSimulation:#creating class
    def __init__(self, environment):# created constructor
        self.environment = environment
    def drill(self):# function for drill
        # Placeholder for drilling functionality
        print("Drilling operation initiated in", self.environment.type)
    def haul(self):#function for haul
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


# In[5]:


import matplotlib.pyplot as plt
# Count the occurrences of each environment type
environment_types = [env.type for env in environments]
environment_counts = {env_type: environment_types.count(env_type) for env_type in set(environment_types)}
# Create the pie chart
plt.figure(figsize=(8, 6))
plt.pie(environment_counts.values(), labels=environment_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Environment Types')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[8]:


import matplotlib.pyplot as plt
import pandas as pd
# Read data from CSV file
file_path = 'geo.csv'
data = pd.read_csv(file_path)
# Initialize counters for length, width, and depth
total_length = 0
total_width = 0
total_depth = 0
# Calculate total values for length, width, and depth
for _, row in data.iterrows():
    total_length += int(row['Length'])
    total_width += int(row['Width'])
    total_depth += int(row['Depth'])
# Calculate percentages for length, width, and depth
total_sum = total_length + total_width + total_depth
length_percentage = (total_length / total_sum) * 100
width_percentage = (total_width / total_sum) * 100
depth_percentage = (total_depth / total_sum) * 100
# Create the pie chart
plt.figure(figsize=(8, 6))
plt.pie([length_percentage, width_percentage, depth_percentage],
        labels=['Length', 'Width', 'Depth'],
        autopct='%1.1f%%',
        startangle=140)
plt.title('Distribution of Environment Attributes')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# # design and develop mine planning

# In[81]:


class Mine:#creating class mine
    def __init__(self, name, location):#creating constructor
        self.name = name
        self.location = location
        self.resources = {}
        
    def add_resource(self, resource, quantity):#function to define resources
        self.resources[resource] = quantity
    
class MiningPlan:#class mining plan
    def __init__(self):#creating constructor
        self.mines = []
        
    def add_mine(self,mine):#add mine
        self.mines.append(mine)
        
    def assess_resources(self):#assess resources
        for mine in self.mines:
            total_resources = sum(mine.resources.values())
            print(f"Total resources in {mine.name}: {total_resources}")
        
mining_plan=MiningPlan()
#defining the data
mine1 = Mine("Utkal zinc", "Location1")
mine1.add_resource("zinc", 358)
mine1.add_resource("Iron ore", 1257)

mine2 = Mine("lig12","Location2")
mine2.add_resource("Gold",11556)
mine2.add_resource("Silver",365722)

mine3 = Mine("Utkal galena","location3")
mine3.add_resource("lead ore",0)

mine4 = Mine("Hindustan zinc LTD","location4")
mine4.add_resource("Zins/silver",0)

mine5 = Mine("Maharastra minerals","location5")
mine5.add_resource("coal",0)
mine5.add_resource("soil",0)

mine6 = Mine("Vasanth coal mine","Mumbai")
mine6.add_resource("overburden",4735)

mine7 = Mine("Vasanth coal mine","Hyderabad")
mine7.add_resource("coal",725)

mine8 = Mine("Reddy coal mine","Bangalore")
mine8.add_resource("overburden",4210)

mine9 = Mine("Reddy coal mine","Delhi")
mine9.add_resource("coal",855)

mine10 = Mine("RP minerals","Jaipur")
mine10.add_resource("overburden",6320)

mine11 = Mine("RP minerals","Mumbai")
mine11.add_resource("coal",1050)

mining_plan.add_mine(mine1)
mining_plan.add_mine(mine2)
mining_plan.add_mine(mine3)
mining_plan.add_mine(mine4)
mining_plan.add_mine(mine5)
mining_plan.add_mine(mine6)
mining_plan.add_mine(mine7)
mining_plan.add_mine(mine8)
mining_plan.add_mine(mine9)
mining_plan.add_mine(mine10)
mining_plan.add_mine(mine11)



mining_plan.assess_resources()



# In[82]:


import matplotlib.pyplot as plt
# Extracting data
mine_names = [mine.name for mine in mining_plan.mines]
total_resources = [sum(mine.resources.values()) for mine in mining_plan.mines]
# Plotting
plt.figure(figsize=(10, 6))
plt.barh(mine_names, total_resources, color='skyblue')
plt.xlabel('Total Resources')
plt.ylabel('Mines')
plt.title('Total Resources in Each Mine')
plt.gca().invert_yaxis()  # Invert y-axis to have mine with highest resources on top
plt.tight_layout()
# Show plot
plt.show()


# # material movement plan with mining equipment

# In[84]:


import csv#importing necessary libraries
class MaterialMovementPlan:#class creation
    def __init__(self, material_moved_per_day):#creating constructor
        self.material_moved_per_day = material_moved_per_day
        
    @classmethod
    def from_csv(cls,csv_file):#reading csv file
        material_moved_per_day_list = []
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                material_moved_per_day_list.append(float(row[0]))
        return [cls(material_moved) for material_moved in material_moved_per_day_list]
    
    def assess_equipment_needs(self):#function to assess equipment needs
        equipment_requirements = {}
        # logic for equipment assessment based on material moved per day
        if self.material_moved_per_day < 1000:
            
            equipment_requirements["Dump Truck"] = 1
        elif 1000 <= self.material_moved_per_day < 1250:
            equipment_requirements["Truck2"] = 2
            
        else:
            equipment_requirements["Excavator"] = 3
            equipment_requirements["Truck1"] = 4
        return equipment_requirements

csv_file_path = "material_moved.csv"
mine_plans = MaterialMovementPlan.from_csv(csv_file_path)
for idx, mine_plan in enumerate(mine_plans):
    print(f"Equipment Requirements for Mine {idx + 1}:")
    equipment_needs = mine_plan.assess_equipment_needs()
    for equipment, quantity in equipment_needs.items():
        print(f"{equipment}: {quantity}")


# In[85]:


import matplotlib.pyplot as plt
# Example data
mine_names = [f"Mine {i+1}" for i in range(len(mine_plans))]
equipment_counts = [len(mine_plan.assess_equipment_needs()) for mine_plan in mine_plans]
# Plotting
plt.figure(figsize=(8, 6))
plt.bar(mine_names, equipment_counts, color='skyblue')
plt.xlabel('Mines')
plt.ylabel('Equipment Count')
plt.title('Equipment Requirements for Mines')
plt.xticks(rotation=45)
plt.tight_layout()
# Show plot
plt.show()


# # design equipment fleet modelling

# In[87]:


class Equipment:
    def __init__(self,equipment_id, equipment_type, capacity, fuel_consumption):#added equipment_id as 1,2,3...
        self.equipment_id = equipment_id
        self.equipment_type = equipment_type
        self.capacity = capacity
        self.fuel_consumption = fuel_consumption
        self.status = "Available"  # Initial status
        
    def assign_task(self, task):#assignig task to available equipments
        if self.status == "Available":
            if task == "Excavation":
                self.perform_excavation()
            elif task == "Transportation":
                self.perform_transportation()
            else:
                print(f"Equipment {self.equipment_id} cannot perform task: {task}.")
        else:
            print(f"Equipment {self.equipment_id} cannot perform task: {task}.")
       
    def perform_excavation(self):#function to perform excavation
        self.status = "busy"
        print(f"Equipment {self.equipment_id} is performing excavation.")
        
    
    def perform_transportation(self):#function to perform transportation
        self.status = "busy"
        print(f"Equipment {self.equipment_id} is transporting materials.")
        
    def complete_task(self):# function to get status of task completion
        self.status = "Available"
        print(f"Equipment {self.equipment_id} completed task")
        
class EquipmentFleet:#creating fleet class
    def __init__(self):
        self.equipment_list = []
        
    def add_equipment(self, equipment):#function o add equipment
        self.equipment_list.append(equipment)
        
    def find_available_equipment(self):#funcion to find availability of equipment
        return [equipment for equipment in self.equipment_list if equipment.status == "Available"]

# Create equipment fleet
fleet = EquipmentFleet()

# Add equipment to the fleet
fleet.add_equipment(Equipment("1", "Truck1", 100, 210))# as equipment ID is not provided (helps to know the availability of the equipments), it is taken as numbers 1,2,3,... and I
fleet.add_equipment(Equipment("2", "Truck2", 100, 160))
fleet.add_equipment(Equipment("3","Loader1",3.24,210))

# Find available equipment
available_equipment = fleet.find_available_equipment()
print("Available Equipment:")
for equipment in available_equipment:
    print(f"{equipment.equipment_id}: {equipment.equipment_type}")
    
# Assign task to available equipment
if available_equipment:
    task = "Transportation"
    available_equipment[0].assign_task(task)
    
# Complete task
fleet.equipment_list[0].complete_task()


# In[88]:


import matplotlib.pyplot as plt
# Extracting data
equipment_ids = [equipment.equipment_id for equipment in fleet.equipment_list]
fuel_consumptions = [equipment.fuel_consumption for equipment in fleet.equipment_list]
# Plotting
plt.figure(figsize=(8, 6))
plt.bar(equipment_ids, fuel_consumptions, color='skyblue')
plt.xlabel('Equipment ID')
plt.ylabel('Fuel Consumption')
plt.title('Fuel Consumption of Equipment in Fleet')
plt.xticks(rotation=45)
plt.tight_layout()
# Show plot
plt.show()


# # model operational process- drilling, hauling

# In[89]:


class DrillingSite:
    def __init__(self, location, resources):
        self.location = location
        self.resources = resources
        self.drilling_sequence = []
        
    def plan_drilling(self):#determine drilling sequence
        self.drilling_sequence = ["Well1", "Well2", "Well3"]
    
    def drill_boreholes(self):#simulate drilling boreholes based on drilling sequence
        for well in self.drilling_sequence:
            print(f"Drilling borehole: {well}")
        
    def extract_resources(self):#simulate resource extraction
        print(f"Extracting {self.resources} from boreholes at {self.location}")
        
        
class Hauling:
    def __init__(self, material, destination):
        self.material = material
        self.destination = destination
        
    def transport_material(self):#simulate transporting material from source to destination
        print(f"Transporting {self.material} to {self.destination}")
        
    def process_material(self):#simulate processing the material at the destination
        print(f"Processing {self.material} at {self.destination}")
        
    def store_or_distribute(self):#simulate storing or distributing the processed material
        print(f"Storing or distributing {self.material} from {self.destination}")
        

drilling_site_A = DrillingSite(location="Mumbai", resources="Overburden")
drilling_site_A.plan_drilling()
drilling_site_A.drill_boreholes()
drilling_site_A.extract_resources()

hauling_process_A = Hauling(material="Overburden", destination="Refinery")
hauling_process_A.transport_material()
hauling_process_A.process_material()
hauling_process_A.store_or_distribute()

drilling_site_B = DrillingSite(location="Hyderabad", resources="coal")
drilling_site_B.plan_drilling()
drilling_site_B.drill_boreholes()
drilling_site_B.extract_resources()

hauling_process_B = Hauling(material="coal", destination="Refinery")
hauling_process_B.transport_material()
hauling_process_B.process_material()
hauling_process_B.store_or_distribute()

drilling_site_C = DrillingSite(location="Banglore", resources="Overburden")
drilling_site_C.plan_drilling()
drilling_site_C.drill_boreholes()
drilling_site_C.extract_resources()

hauling_process_C = Hauling(material="Overburden", destination="Refinery")
hauling_process_C.transport_material()
hauling_process_C.process_material()
hauling_process_C.store_or_distribute()

drilling_site_D = DrillingSite(location="Delhi", resources="Coal")
drilling_site_D.plan_drilling()
drilling_site_D.drill_boreholes()
drilling_site_D.extract_resources()

hauling_process_D = Hauling(material="Coal", destination="Refinery")
hauling_process_D.transport_material()
hauling_process_D.process_material()
hauling_process_D.store_or_distribute()

drilling_site_E = DrillingSite(location="Jaipur", resources="Overburden")
drilling_site_E.plan_drilling()
drilling_site_E.drill_boreholes()
drilling_site_E.extract_resources()

hauling_process_E = Hauling(material="Overburden", destination="Refinery")
hauling_process_E.transport_material()
hauling_process_E.process_material()
hauling_process_E.store_or_distribute()

drilling_site_F = DrillingSite(location="Mumbai", resources="Coal")
drilling_site_F.plan_drilling()
drilling_site_F.drill_boreholes()
drilling_site_F.extract_resources()

hauling_process_F = Hauling(material="Coal", destination="Refinery")
hauling_process_F.transport_material()
hauling_process_F.process_material()
hauling_process_F.store_or_distribute()







# In[90]:


import matplotlib.pyplot as plt
# Data
locations = ["Mumbai", "Hyderabad", "Bangalore", "Delhi", "Jaipur"]
borehole_counts = [3, 3, 3, 3, 3]  # Assuming 3 boreholes drilled at each site
# Plotting
plt.figure(figsize=(8, 6))
plt.bar(locations, borehole_counts, color='skyblue')
plt.xlabel('Location')
plt.ylabel('Number of Boreholes Drilled')
plt.title('Number of Boreholes Drilled at Each Drilling Site')
plt.xticks(rotation=45)
plt.tight_layout()
# Show plot
plt.show()


# # equipment performance improvement scenarios

# In[92]:


# creating class
class Equipment:
    def __init__(self, name, status="Operational"):
        self.name = name
        self.status = status
        
    def perform_maintenance(self):
        print(f"Maintenance performed on {self.name}")
        
    def monitor_performance(self):
        print(f"Monitoring performance of {self.name}")
        
    def train_operators(self):
        print(f"Training operators for {self.name}")
        
    def integrate_technology(self):
        print(f"Integrating technology for {self.name}")
        
    def optimize_energy(self):
        print(f"optimizing energy efficiency for {self.name}")
        
    def optimize_material_handling(self):
        print(f"optimizing material handling for {self.name}")
        
    def manage_supply_chain(self):
        print(f"managing supply chain for {self.name}")
        
    def make_data_driven_decisions(self):
        print(f"Making data driven decisions for {self.name}")
        
    def enhance_safety(self):
        print(f"Enhancing safety for {self.name}")
        
# creating class
class MiningEquipment(Equipment):
    def __init__(self, name, status="Operational", mining_type="Surface"):
        super().__init__(name, status)
        self.mining_type = mining_type
        
if __name__ == "__main__":
    mining_equipments = [
        MiningEquipment(name="Excavators"),
        MiningEquipment(name="Dump Truck"),
        MiningEquipment(name="Drill"),
        MiningEquipment(name="Backhoe"),
        MiningEquipment(name="Loader"),
        MiningEquipment(name="Scrapper"),
        MiningEquipment(name="Shovel"),
        MiningEquipment(name="Truck"),
        MiningEquipment(name="Dragline")
        
    ]
    
    for equipment in mining_equipments:
        equipment.perform_maintenance()
    
    #monitor performance
        equipment.monitor_performance()
    
    #train operations
        equipment.train_operators()
    
    #integrate technology
        equipment.integrate_technology()
    
    #optimize energy
        equipment.optimize_energy()
    
    #optimize material handling
        equipment.optimize_material_handling()
    
    #manage supply chain
        equipment.manage_supply_chain()
    
    #make data driven decisions
        equipment.make_data_driven_decisions()
    
    #enhance safety
        equipment.enhance_safety()
    


# In[93]:


import matplotlib.pyplot as plt
# Data
equipment_names = [equipment.name for equipment in mining_equipments]
maintenance_counts = [1 for _ in mining_equipments]  # Assuming 1 maintenance operation performed for each equipment
# Plotting
plt.figure(figsize=(10, 6))
plt.bar(equipment_names, maintenance_counts, color='skyblue')
plt.xlabel('Equipment')
plt.ylabel('Number of Maintenance Operations')
plt.title('Number of Maintenance Operations Performed for Each Equipment')
plt.xticks(rotation=45)
plt.tight_layout()
# Show plot
plt.show()


# # setup environment simulation

# In[94]:


import pandas as pd# importing necessary libraries

class MiningSimulation:#creating class
    def __init__(self, data):# creating constructor
        self.data = data
        self.minerals = {}
    def extract_minerals(self, location, mineral_type):
        # Simulate extraction of minerals based on the type found at the location
        print(f"Extracting {mineral_type} at {location}...")
    def simulate_mining(self):
        for index, row in self.data.iterrows():
            location = (row['Length'], row['Width'], row['Depth'])
            mineral_type = row['Mineral']
            if location not in self.minerals:
                self.minerals[location] = []
            self.minerals[location].append(mineral_type)
            self.extract_minerals(location, mineral_type)
            
#defining data
data = pd.DataFrame({
    'Length': [1000, 1000, 10250, 12080, 10250,12081, 10250, 10250, 500],
    'Width': [800, 800, 400, 400, 400, 400, 400, 400, 10],
    'Depth': [200, 200, 200, 200, 200, 200, 200, 200, 800],
    'Mineral': ['Gold', 'Coal', 'Iron', 'Silver', 'Zinc', 'Lead', 'Soil', 'TPH', 'Overburden']
})

sim = MiningSimulation(data)
sim.simulate_mining()


# In[95]:


import matplotlib.pyplot as plt
# Data
locations = data[['Length', 'Width', 'Depth']]
# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(locations['Length'], locations['Width'], c='blue', label='Mining Locations')
plt.xlabel('Length')
plt.ylabel('Width')
plt.title('Mining Locations')
plt.legend()
plt.grid(True)
plt.tight_layout()
# Show plot
plt.show()


# # build geological models

# In[9]:


#Build geological models
import matplotlib.pyplot as plt
import pandas as pd

# Read data from the provided CSV file
data = pd.read_csv('geo.csv')
#class MiningSection:
#    def __init__(self, env, name, length, width, depth):
 #       self.env = env
  #      self.name = name
   #     self.length = length
    #    self.width = width
     #   self.depth = depth
      #  self.equipment_queue = simpy.Store(env)
        
   
        
def visualize_geological_layers(data):
    
    fig, ax = plt.subplots(figsize=(8, 6))
    for _, section in data.iterrows():
        depth_start = section['Depth']
        depth_end = depth_start + section['Length']
        width = section['Width']
        ax.fill_betweenx(y=[depth_start, depth_end], x1=0, x2=width, label=section['Section'])
    ax.set_xlabel('Width')
    ax.set_ylabel('Depth')
    ax.set_title('Geological Layers')
    ax.legend()
    plt.show()
    
# Visualize geological layers based on the provided data
visualize_geological_layers(data)







# In[6]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import re
# Read data from the provided CSV file
data = pd.read_csv('geo.csv')
# Remove non-numeric characters and convert to numeric
data['Length'] = pd.to_numeric(data['Length'].replace(r'[^\d.]', '', regex=True))
data['Depth'] = pd.to_numeric(data['Depth'].replace(r'[^\d.]', '', regex=True))
data['Width'] = pd.to_numeric(data['Width'].replace(r'[^\d.]', '', regex=True))
def visualize_geological_layers_3d(data):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    # Sort the data by the 'Depth' column
    data_sorted = data.sort_values(by='Depth')
    for _, section in data_sorted.iterrows():
        depth_start = section['Depth']
        depth_end = depth_start + section['Length']
        width = section['Width']
        # Adjust the X-axis position for east and west
        if 'east' in section['Section']:
            x_pos = 1  # Adjust as needed
        elif 'west' in section['Section']:
            x_pos = -1  # Adjust as needed
        else:
            x_pos = 0
        ax.bar3d(x_pos, depth_start, 0, width, section['Length'], depth_end - depth_start, shade=True, label=section['Section'])
    ax.set_xlabel('Width')
    ax.set_ylabel('Depth')
    ax.set_zlabel('Length')
    ax.set_title('Geological Layers - 3D Model')
    
    plt.show()
# Visualize geological layers in 3D based on the modified data
visualize_geological_layers_3d(data)


# # Mine Plans - equipments

# In[100]:


class Equipment:# creating class
    def __init__(self, name, capacity, power):# creating constructor
        self.name = name
        self.capacity = capacity
        self.power = power
        
def generate_plans(equipment_list):# function to generate plans
    plans = []
    for equipment in equipment_list:
        plans.append(f"Plan for {equipment.capacity} {equipment.power} {equipment.name}(s)")
    return plans

equipment_list = [
    Equipment("Drill1", 2000, 4500),
    Equipment("Drill2", 1500, 3500),
    Equipment("Truck1", 283.16, 4362.34),
    Equipment("Truck1", 283.16, 4362.34),
    Equipment("Truck2", 283.16, 4362.34),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000)
]
plans = generate_plans(equipment_list)
for plan in plans:
    print(plan)


# In[119]:


class Equipment:# creating class
    def __init__(self, name, capacity, power):# creating constructor
        self.name = name
        self.capacity = capacity
        self.power = power
def generate_plans(equipment_list):
    plans = []
    for equipment in equipment_list:
        plans.append(f"Plan for {equipment.capacity} {equipment.power} {equipment.name}(s)")
    return plans
equipment_list = [
    Equipment("Drill1", 2000, 4500),
    Equipment("Drill2", 1500, 3500),
    Equipment("Truck1", 283.16, 4362.34),
    Equipment("Truck1", 283.16, 4362.34),
    Equipment("Truck2", 283.16, 4362.34),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000),
    Equipment("Loader1", 9.17, 2000)
]
# Extracting equipment names, capacities, and powers
equipment_names = [equipment.name for equipment in equipment_list]
capacities = [equipment.capacity for equipment in equipment_list]
powers = [equipment.power for equipment in equipment_list]
# Creating a bar chart for capacities and powers
fig, ax = plt.subplots(2, 1, figsize=(10, 8))
ax[0].bar(equipment_names, capacities, color='blue')
ax[0].set_ylabel('Capacity')
ax[0].set_title('Equipment Capacities')
ax[1].bar(equipment_names, powers, color='green')
ax[1].set_ylabel('Power')
ax[1].set_title('Equipment Powers')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()







# # Graphs using new data

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd .read_csv("geo.csv")
x = data['Section']
y = data['Length']

plt.bar(x,y)


# In[11]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd .read_csv("geo.csv")
x = data['Section']
y = data['Width']

plt.bar(x,y)


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd .read_csv("geo.csv")
x = data['Type']
y = data['Length']

plt.bar(x,y)


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd .read_csv("geo.csv")
x = data['Type']
y = data['Width']

plt.bar(x,y)


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd .read_excel("equipment1.xlsx")
x = data['Equipment']
y = data['Capacity']

plt.bar(x,y)


# In[16]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd .read_excel("equipment1.xlsx")
x = data['Equipment']
y = data['Power']

plt.bar(x,y)


# In[108]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd .read_excel("utility.xlsx")
x = data['Equipment']
y = data['Utilization']

plt.bar(x,y)


# In[19]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd .read_excel("utility.xlsx")
x = data['Equipment']
y = data['MTBF']

plt.bar(x,y)


# In[21]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd .read_excel("utility.xlsx")
x = data['Equipment']
y = data['MTTR']

plt.bar(x,y)


# # create variance of simulation and time and do the integration part 

# In[2]:


#importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Define Simulation Variables

num_simulations = 1000# SAMPLE NUMBER
num_years = 2
ore_grades = np.random.uniform(4.56, 92, num_simulations)
equipment_efficiency = np.random.normal(0.58,1.8, num_simulations)

# Step 2: Generate Scenarios

ore_grade_scenario = np.random.choice(ore_grades, size=num_years)
equipment_efficiency_scenario = np.random.choice(equipment_efficiency, size=num_years)


# Step 3: Run Simulations

def simulate_mining(ore_grade, equipment_efficiency):
    production = ore_grade * equipment_efficiency 
    return production

# Step 4: Analyze Results

total_production = []
for i in range(num_simulations):
    production_scenario = []
    for year in range(num_years):
        production = simulate_mining(ore_grade_scenario[year], equipment_efficiency_scenario[year])
        production_scenario.append(production)
    total_production.append(sum(production_scenario))

# Visualization
plt.hist(total_production, bins=30, edgecolor='black')
plt.xlabel('Total Production')
plt.ylabel('Frequency')
plt.title('Distribution of Total Production over {} Years'.format(num_years))
plt.show()


# #    To showcase improvement in asset utilization rates percentage wise 
# 

# In[112]:


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


# In[114]:


utilization_rates = {
    'drill1': 0.6,
    'truck1a': 0.75,
    'truck2a': 0.9,
    'truck3': 1.05,
    'truck4': 1.2,
    'truck1b': 1.35,
    'truck1c': 1.5,
    'truck1d': 1.65,
    'truck1e': 1.8,
    'truck2b': 0.58
}
# Reference utilization rate
reference_utilization_rate = 0.55
# Calculate percentage change for each equipment
percentage_changes = {equipment: ((utilization_rate - reference_utilization_rate) / reference_utilization_rate) * 100
                      for equipment, utilization_rate in utilization_rates.items()}
# Plotting the percentage changes
plt.figure(figsize=(10, 6))
plt.bar(percentage_changes.keys(), percentage_changes.values(), color='skyblue')
plt.axhline(0, color='gray', linewidth=0.5)  # Add a horizontal line at y=0 for reference
plt.title('Percentage Change in Utilization Rates')
plt.xlabel('Equipment')
plt.ylabel('Percentage Change')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# #   To showcase average monthly production
# 

# In[115]:


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


# In[116]:


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
# Plotting the monthly production data
plt.figure(figsize=(10, 6))
plt.bar(monthly_production.keys(), monthly_production.values(), color='skyblue')
plt.title('Monthly Production Data')
plt.xlabel('Month')
plt.ylabel('Production (tons)')
plt.axhline(average_monthly_production, color='red', linestyle='--', linewidth=1, label='Average')  # Add average line
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()





# # To showcase Reduced maintenance if any by referring to the overall data provided till date
# 

# In[117]:


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





# In[ ]:




