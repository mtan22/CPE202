# CPE 202 Lab 1 Test Cases: Michelle Tan
# Instructor: Prof. Parkinson

import unittest
from lab1a import *


class TestLab1(unittest.TestCase):

    def test_max_list_01(self) -> None:
        # Tests a "general" case with all positive integers
        tlist: list = [1, 2, 3]
        self.assertEqual(max_list_iter(tlist), 3)

    def test_max_list_02(self) -> None:
        # Tests a case of a mix of positive, negative numbers and a zero
        tlist: list = [-3, 2, 6, -24, 0]
        self.assertEqual(max_list_iter(tlist), 6)

    def test_max_list_03(self) -> None:
        # Tests a case when the input list is None and makes sure it raises a ValueError
        tlist = None
        with self.assertRaises(ValueError):
            max_list_iter(tlist)

    def test_max_list_04(self) -> None:
        # Tests a case of an empty string and makes sure it returns None
        tlist: list = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_reverse_list_01(self) -> None:
        # Tests a "general" case of all positive numbers
        intlist: list = [1, 2, 3]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [3, 2, 1])
        self.assertEqual(intlist, [1, 2, 3])

    def test_reverse_list_02(self) -> None:
        # Tests a case of a mix of positive, negative numbers and a zero
        intlist: list = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1]
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])
        self.assertEqual(intlist, [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1])

    def test_reverse_list_03(self) -> None:
        # Tests a case when the input list of None and makes sure it raises a ValueError
        intlist = None
        with self.assertRaises(ValueError):
            reverse_list(intlist)

    def test_reverse_list_04(self) -> None:
        # Tests a case of an empty string and make sure it returns None
        intlist: list = []
        revlist = reverse_list(intlist)
        self.assertEqual(revlist, None)
        self.assertEqual(intlist, [])

    def test_reverse_mutate_01(self) -> None:
        # Tests a general case of all positive numbers
        intlist: list = [1, 2, 3]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [3, 2, 1])

    def test_reverse_mutate_02(self) -> None:
        # Tests a case of a mix of positive, negative numbers and a zero
        intlist: list = [-325, 3, 0, -3, -555]
        reverse_list_mutate(intlist)
        self.assertEqual(intlist, [-555, -3, 0, 3, -325])

    def test_reverse_mutate_03(self) -> None:
        # Tests a case when the input list is None and makes sure it raises a ValueError
        intlist = None
        with self.assertRaises(ValueError):
            reverse_list_mutate(intlist)

        # Test case for empty string not applicable for this function because there
        # is nothing for the empty string to be changed to


if __name__ == "__main__":
    unittest.main()
