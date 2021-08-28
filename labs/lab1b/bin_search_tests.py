# CPE 202 Lab 1b: Michelle Tan
# Instructor: Prof. Parkinson

import unittest
from bin_search import *
from typing import List


class TestLab1b(unittest.TestCase):

    def test_bin_search_iter_01(self) -> None:
        # Tests a "general" case with all positive numbers
        tlist: List = [5, 9, 18, 23, 55, 72]
        self.assertEqual(bin_search_iter(tlist, 5), 0)

    def test_bin_search_iter_02(self) -> None:
        # Tests a case with the input list as None and makes sure it raises a ValueError
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            bin_search_iter(tlist, 5)

    def test_bin_search_iter_03(self) -> None:
        # Tests a case with an input list but a target that is not included, and makes sure it returns None
        tlist = [-3, 5, 6, 25]
        self.assertEqual(bin_search_iter(tlist, 64), None)

    def test_bin_search_iter_04(self) -> None:
        # Tests a case with zeros, negative, and positive numbers
        tlist: List = [-34, -3, 0, 0, 45]
        self.assertEqual(bin_search_iter(tlist, 45), 4)

    def test_bin_search_rec_01(self) -> None:
        # Tests a "general" case with all positive numbers
        tlist: List = [0, 3, 6, 29, 74, 94, 99]
        self.assertEqual(bin_search_rec(tlist, 6), 2)

    def test_bin_search_rec_02(self) -> None:
        # Tests a case with the input list as None and makes sure it raises a ValueError
        tlist = None
        with self.assertRaises(ValueError):  # uses context manager for checking exception
            bin_search_rec(tlist, 3)

    def test_bin_search_rec_03(self) -> None:
        # Tests a case with an input list but a target that is not included, and makes sure it returns None
        tlist: List = [-3, 5, 6, 19]
        self.assertEqual(bin_search_rec(tlist, 88), None)

    def test_bin_search_rec_04(self) -> None:
        # Tests a case with zeros, negative, and positive numbers
        tlist: List = [-24, 0, 2, 56, 67]
        self.assertEqual(bin_search_rec(tlist, 56), 3)


if __name__ == "__main__":
    unittest.main()
