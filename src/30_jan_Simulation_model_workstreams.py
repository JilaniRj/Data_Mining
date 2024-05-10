#!/usr/bin/env python
# coding: utf-8

# # DESIGN AND DEVELOP MINE PLANNING

# In[ ]:


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



# # material movement plan with mining equipment

# In[12]:


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


# # Design equipment fleet modelling

# In[14]:


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
fleet.add_equipment(Equipment("1", "Truck1", 100, 210))
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


# # model operational process, drilling and hauling

# In[20]:


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







# In[ ]:




