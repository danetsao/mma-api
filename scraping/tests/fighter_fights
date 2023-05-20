import sys
import unittest

sys.path.append('../')

from scrape import *


"""
Testing fighters fights.
I highly recommend you run some testing before using.
This some basic testing functionlity that was good as of 05/19/2023.
However, these statistics change, so feel free to update the test cases and share.
Unfortunately, you will have to manually update the test cases using data form the UFC website.
"""

# Not yet implemented

def config_data(name: str) -> dict:
    data = get_athlete_data(name)
    fights = data['fights']
    return fights

# The test case
class TestAddFunction(unittest.TestCase):

    def test_leon_edwards(self):
        fights = config_data('leon-edwards')
        self.assertEqual(0, 0)
    
    def test_jon_jones(self):
        fights = config_data('jon-jones')
        self.assertEqual(0, 0)

# Run the test case
if __name__ == '__main__':
    unittest.main()