import sys
import unittest

sys.path.append('../')

from scrape import *


"""
Testing fighters statistics.
I highly recommend you run some testing before using.
This some basic testing functionlity that was good as of 05/19/2023.
However, these statistics change, so feel free to update the test cases and share.
Unfortunately, you will have to manually update the test cases using data form the UFC website.
"""


# The test case
class TestAddFunction(unittest.TestCase):

    def test_leon_edwards(self):
        name = 'leon-edwards'
        data = get_athlete_data(name)
        self.assertEqual(data['wins_by_knockout'], '7')
        self.assertEqual(data['wins_by_submission'], '3')
        self.assertEqual(data['first_round_finishes'], '5')
    
    def test_jon_jones(self):
        name = 'jon-jones'
        data = get_athlete_data(name)
        self.assertEqual(data['take_downs_landed'], '36')
        self.assertEqual(data['take_downs_attempted'], '97')

    def test_alexander_volkanovski(self):
        name = 'alexander-volkanovski'
        data = get_athlete_data(name)
        self.assertEqual(data['wins_by_knockout'], '12')
        self.assertEqual(data['wins_by_submission'], '3')
        self.assertEqual(data['first_round_finishes'], '7')

# Run the test case
if __name__ == '__main__':
    unittest.main()