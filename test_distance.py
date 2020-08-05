import unittest
from distance import calculateDistance

class TestDistance(unittest.TestCase):

    def test_distance (self):
        self.assertAlmostEqual(calculateDistance(0,0,0,0),0)
        self.assertAlmostEqual(calculateDistance(1,1,1,1),0)

    def test_values(self):
        self.assertRaises(ValueError , calculateDistance , -2,1,2,6)