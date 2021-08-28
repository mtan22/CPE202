# Project 1 - rec_list_tests.py: Michelle Tan
# Instructor: Prof. Parkinson

import unittest
from rec_list import *


# Starter test cases - write more!

class TestRecList(unittest.TestCase):

    def test_first1(self) -> None:
        # Tests a case with a lowercase first character string, an uppercase first character string,
        # and a non-alpha first character string
        # Makes sure that the non-alpha string gets returned because it is "less than" the other strings
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(first_string(strlist), "49ers")

    def test_first2(self) -> None:
        # Tests a case with two lowercase first character strings and an uppercase first character string
        # Makes sure that the uppercase string gets returned because it is "less than" the other strings
        strlist = Node("Jqu", Node("michelle", Node("amplitude", None)))
        self.assertEqual(first_string(strlist), "Jqu")

    def test_first3(self) -> None:
        # Tests a case with all lowercase first character strings
        # Makes sure that the lowercase character string that is first in the alphabet is returned
        # because it is "less than" the other strings
        strlist = Node("bobby", Node("david", Node("jack", None)))
        self.assertEqual(first_string(strlist), "bobby")

    def test_first4(self) -> None:
        # Tests a case with the input list as None
        # Makes sure that None is returned
        strlist = None
        self.assertEqual(first_string(strlist), None)

    def test_split1(self) -> None:
        # Tests a case with a lowercase first character string, uppercase first character string,
        # a non-alpha first character string, and None
        # Makes sure a tuple with all three strlists are returned with the corresponding categories
        strlist = Node("xyz", Node("Abc", Node("49ers", None)))
        self.assertEqual(split_list(strlist), (Node('Abc', None), Node('xyz', None), Node('49ers', None)))

    def test_split2(self) -> None:
        # Tests a case with various lowercase first character strings, uppercase first character,
        # strings, non-alpha first character strings, and None
        # Makes sure a tuple with all three strlists are returned with the corresponding categories
        strlist = Node("Yellow", Node("abc", Node("$7.25", Node("lime", Node("42", Node("Ethan", None))))))
        self.assertEqual(split_list(strlist), (
            Node('abc', Node("Ethan", None)), Node('Yellow', Node("lime", None)), Node('$7.25', Node("42", None))))

    def test_split3(self) -> None:
        # Tests a case with various lowercase first character strings, uppercase first character,
        # strings, non-alpha first character strings (including mathematical operators), and None
        # Makes sure a tuple with all three strlists are returned with the corresponding categories
        strlist = Node("$248393", Node("Monster", Node("carrot", Node("chocolate", Node("-46364", Node("Abby",
                                                                                                       Node("<3253>",
                                                                                                            None)))))))
        self.assertEqual(split_list(strlist), (
            Node('Abby', None), Node('Monster', Node('carrot', Node('chocolate', None))),
            Node('$248393', Node('-46364', Node('<3253>', None)))))

    def test_split4(self) -> None:
        # Tests a case with the input list as None
        # Makes sure that None is returned in tuple form
        strlist = None
        self.assertEqual(split_list(strlist), (None, None, None))


if __name__ == "__main__":
    unittest.main()
