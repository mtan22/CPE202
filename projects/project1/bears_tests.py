# Project 1 - bears_tests.py: Michelle Tan
# Instructor: Prof. Parkinson

import unittest
from bears import *


class TestAssign1(unittest.TestCase):
    def test_bear_01(self) -> None:
        # Tests a case of 250 as n
        self.assertTrue(bears(250))

    def test_bear_02(self) -> None:
        # Tests a case of 42 as n
        self.assertTrue(bears(42))

    def test_bear_03(self) -> None:
        # Tests a case of 53 as n
        self.assertFalse(bears(53))

    def test_bear_04(self) -> None:
        # Tests a case of 41 as n
        self.assertFalse(bears(41))

    def test_bear_05(self) -> None:
        # Tests a case of 100 as n
        self.assertFalse(bears(100))


if __name__ == "__main__":
    unittest.main()
