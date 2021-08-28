# Project 1 - perm_lex_tests.py: Michelle Tan
# Instructor: Prof. Parkinson

import unittest
import perm_lex
from typing import List


# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex_01(self) -> None:
        # Tested a case with two characters in the input string
        self.assertEqual(perm_lex.perm_gen_lex('ab'), ['ab', 'ba'])

    def test_perm_gen_lex_02(self) -> None:
        # Tested a case with three characters in the input string
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_perm_gen_lex_03(self) -> None:
        # Tested a case with four characters in the input string
        # The characters in the input string are not alphabetized
        # Makes sure that the list returned is in lexicographic order
        self.assertEqual(perm_lex.perm_gen_lex('geek'),
                         ['eegk', 'eekg', 'egek', 'egke', 'ekeg', 'ekge', 'geek', 'geke', 'gkee', 'keeg', 'kege',
                          'kgee'])

    def test_perm_gen_lex_04(self) -> None:
        # Tested a case with one character in the input string
        # Makes sure that the list returned is the one character
        self.assertEqual(perm_lex.perm_gen_lex('a'), ['a'])

    def test_perm_gen_lex_05(self) -> None:
        # Tested a case with an empty input string
        # Makes sure that the list returned is an empty list
        self.assertEqual(perm_lex.perm_gen_lex(''), [])


if __name__ == "__main__":
    unittest.main()
