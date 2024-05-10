#!/usr/bin/env python
# coding: utf-8

# In[1]:


class DrillingSite:# creating class
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




