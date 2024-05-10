#!/usr/bin/env python
# coding: utf-8

# # Equipment performance improvement scenarios

# In[1]:


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
    


# In[ ]:




