import unittest
from tsort import *

class TestTsort(unittest.TestCase):
        
    def test_01(self) -> None:
        input = ['101', '102', '102', '103', '103', '315', '225', '315', '103', '357', '315', '357', '141', '102', '102', '225']
        expect = "141\n101\n102\n225\n103\n315\n357"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_02(self) -> None:
        input = ['blue', 'black', 'red', 'blue', 'red', 'green', 'green', 'blue', 'green', 'purple', 'purple', 'blue']
        expect = "red\ngreen\npurple\nblue\nblack"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_04(self) -> None:
        input = ['3', '8', '3', '10', '5', '11', '7', '8', '7', '11', '8', '9', '11', '2', '11', '9', '11', '10']
        expect = "7\n5\n11\n2\n3\n10\n8\n9"
        actual = tsort(input)
        self.assertEqual(actual.strip(), expect)

    def test_07(self) -> None:
        input = 'v1 v2 v3 v4 v5 v6 v7 v8 v9 v10'
        input = input.split() #type: ignore
        expect = 'v9 v10 v7 v8 v5 v6 v3 v4 v1 v2'
        expect = '\n'.join(expect.split())
        actual = tsort(input) #type: ignore
        self.assertEqual(actual.strip(), expect)

    def test_10(self) -> None:
        input = [] #type: ignore
        try:
            actual = tsort(input)
            self.fail() # pragma: no cover
        except ValueError as e:
            self.assertEqual(str(e), "input contains no edges")

    def test_13(self) -> None:
        input = 'a b b a'
        input = input.split() #type: ignore
        try:
            actual = tsort(input) #type: ignore
            self.fail() # pragma: no cover
        except ValueError as e:
            self.assertEqual(str(e), "input contains a cycle")

    def test_14(self) -> None:
        input = 'a b b a b'
        input = input.split() #type: ignore
        try:
            actual = tsort(input) #type: ignore
            self.fail() # pragma: no cover
        except ValueError as e:
            self.assertEqual(str(e), "input contains an odd number of tokens")

if __name__ == "__main__":
    unittest.main()
