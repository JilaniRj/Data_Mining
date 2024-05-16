import unittest
import pandas as pd

# Import the class you want to test
import sys

sys.path.append(r'C:\Users\CW\Downloads\Data_mining\Data_mining\tests')  # Adjust the path as needed


# Now you can import modules from src
from simulation_timeframe import MiningSimulation

#from ..src.simulation_timeframe import MiningSimulation

import unittest
from unittest.mock import patch
#from my_module import MiningSimulation

import unittest
import pandas as pd

class TestMiningSimulation(unittest.TestCase):
    def setUp(self):
        # Create sample data for testing
        data = pd.DataFrame({
            'Length': [10, 20, 30],
            'Width': [5, 10, 15],
            'Depth': [3, 6, 9],
            'Mineral': ['Gold', 'Silver', 'Copper']
        })
        self.sim = MiningSimulation(data)

    def test_extract_minerals(self):
        # Test whether extract_minerals method correctly prints the extraction message
        location = (10, 5, 3)
        mineral_type = 'Gold'
        expected_output = f"Extracting Gold at {location}..."
        
        # Redirect stdout to capture print output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output
        
        self.sim.extract_minerals(location, mineral_type)
        
        # Reset redirect
        sys.stdout = sys.__stdout__
        
        # Get printed message
        printed_message = captured_output.getvalue().strip()
        
        self.assertEqual(printed_message, expected_output)

    def test_simulate_mining(self):
        # Test whether simulate_mining method correctly updates the minerals dictionary
        self.sim.simulate_mining()

        # Check if minerals dictionary is updated as expected
        expected_minerals = {
            (10, 5, 3): ['Gold'],
            (20, 10, 6): ['Silver'],
            (30, 15, 9): ['Copper']
        }
        self.assertEqual(self.sim.minerals, expected_minerals)

if __name__ == '__main__':
    unittest.main()

    
