# equipment.py

class Equipment:
    def __init__(self, equipment, mine, material, prod_date, work_hours, fuel_consumed, availability):
        self.equipment = equipment
        self.mine = mine
        self.material = material
        self.prod_date = prod_date
        self.work_hours = work_hours
        self.fuel_consumed = fuel_consumed
        self.availability = availability

class MinePlan:
    def __init__(self):
        self.equipment_list = []

    def add_equipment(self, equipment):
        self.equipment_list.append(equipment)
