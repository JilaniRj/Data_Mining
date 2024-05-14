import unittest
from equipment import Equipment, MinePlan

class TestEquipment(unittest.TestCase):
    def test_equipment_initialization(self):
        equipment = Equipment("Excavator", "MineA", "Coal", "2023-05-01", "8 hours", "100 gal diesel", "90%")
        self.assertEqual(equipment.equipment, "Excavator")
        self.assertEqual(equipment.mine, "MineA")
        self.assertEqual(equipment.material, "Coal")
        self.assertEqual(equipment.prod_date, "2023-05-01")
        self.assertEqual(equipment.work_hours, "8 hours")
        self.assertEqual(equipment.fuel_consumed, "100 gal diesel")
        self.assertEqual(equipment.availability, "90%")

class TestMinePlan(unittest.TestCase):
    def test_mine_plan_initialization(self):
        mine_plan = MinePlan()
        self.assertIsInstance(mine_plan.equipment_list, list)

    def test_add_equipment(self):
        mine_plan = MinePlan()
        equipment = Equipment("Excavator", "MineA", "Coal", "2023-05-01", "8 hours", "100 gal diesel", "90%")
        mine_plan.add_equipment(equipment)
        self.assertEqual(len(mine_plan.equipment_list), 1)
        self.assertEqual(mine_plan.equipment_list[0], equipment)

if __name__ == '__main__':
    unittest.main()
