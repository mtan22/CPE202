# CPE 202 Location Class Test Cases, Lab 1: Michelle Tan
# Instructor: Prof. Parkinson

import unittest
from location import *


class TestLocation(unittest.TestCase):

    def test_init(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(loc.name, 'SLO')
        self.assertEqual(loc.lat, 35.3)
        self.assertEqual(loc.lon, -120.7)

    def test_eq(self) -> None:
        loc1 = Location('San Jose', 32.5, 20.4)
        loc2 = Location('San Jose', 32.5, 20.4)
        loc3 = Location('Paris', -14.3, -130.2)
        loc4 = Location('SLO', 35.3, -120.7)
        self.assertTrue(loc1 == loc2)
        self.assertTrue(loc1.__eq__(loc2))
        self.assertNotEqual(loc1, loc3)
        self.assertNotEqual(loc4, loc1)
        self.assertEqual(loc2, loc1)

    def test_eq_not_location(self) -> None:
        loc = Location('Denmark', -28.7, 178.3)
        self.assertFalse(loc.__eq__(None))

    def test_repr(self) -> None:
        loc = Location('SLO', 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")


if __name__ == "__main__":
    unittest.main()
