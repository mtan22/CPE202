# Project 2: Michelle Tan
# Instructor: Prof. Parkinson
# Date: 2/3/2021

# Start of unittest - add to completely test functions in exp_eval!

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):

    def test_postfix_eval_01a(self) -> None:
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_01b(self) -> None:
        self.assertAlmostEqual(postfix_eval("8 1 >>"), 4)
        self.assertAlmostEqual(postfix_eval("8 1 <<"), 16)

    def test_postfix_eval_01c(self) -> None:
        self.assertAlmostEqual(postfix_eval("8 2 **"), 64)

    def test_postfix_eval_01d(self) -> None:
        self.assertAlmostEqual(postfix_eval("18.5 -2 *"), -37)
        self.assertAlmostEqual(postfix_eval("-18.52 -0.78 +"), -19.3)
        self.assertAlmostEqual(postfix_eval("-33.5 -22 -"), -11.5)
        self.assertAlmostEqual(postfix_eval("9 2 /"), 4.5)

    def test_postfix_eval_02(self) -> None:
        try:
            postfix_eval("blah")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03a(self) -> None:
        try:
            postfix_eval("4 +")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_03b(self) -> None:
        try:
            postfix_eval("")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self) -> None:
        try:
            postfix_eval("1 2 3 +")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self) -> None:
        try:
            postfix_eval("6 0 /")
            self.fail()  # pragma: no cover
        except ValueError as e:
            self.assertEqual(str(e), "0 not divisible")

    def test_postfix_eval_06(self) -> None:
        try:
            postfix_eval("6.8 9 <<")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_07(self) -> None:
        try:
            postfix_eval("6 9.9 >>")
            self.fail()     # pragma: no cover
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_infix_to_postfix_01a(self) -> None:
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("32 >> 2 >> 1"), "32 2 >> 1 >>")

    def test_infix_to_postfix_01b(self) -> None:
        self.assertEqual(infix_to_postfix("32 >> 2 << 1"), "32 2 >> 1 <<")

    def test_infix_to_postfix_01c(self) -> None:
        self.assertEqual(infix_to_postfix("3 ** 2 ** 2"), "3 2 2 ** **")

    def test_infix_to_postfix_02(self) -> None:
        self.assertEqual(infix_to_postfix("( 5 - 3 ) * 4"), "5 3 - 4 *")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")

    def test_infix_to_postfix_03(self) -> None:
        self.assertEqual(infix_to_postfix("70 - -3 * 10"), "70 -3 10 * -")

    def test_infix_to_postfix_04(self) -> None:
        self.assertEqual(infix_to_postfix("70.52 - 3.5 * 10.05"), "70.52 3.5 10.05 * -")

    def test_infix_to_postfix_05(self) -> None:
        self.assertEqual(infix_to_postfix("-70.52 - 3.5 * 10.05"), "-70.52 3.5 10.05 * -")

    def test_infix_to_postfix_06(self) -> None:
        self.assertEqual(infix_to_postfix("46 + 6 / 2 * (64 - 3) >> 3"), "46 6 2 / * + 3 >> -")

    def test_infix_to_postfix_07(self) -> None:
        self.assertEqual(infix_to_postfix("6 ** 3 / 4"), "6 3 ** 4 /")

    def test_infix_to_postfix_08(self) -> None:
        self.assertEqual(infix_to_postfix(""), "")

    def test_prefix_to_postfix_01(self) -> None:
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix_02(self) -> None:
        self.assertEqual(prefix_to_postfix("+ * / 5 7 4 6"), "5 7 / 4 * 6 +")

    def test_prefix_to_postfix_03(self) -> None:
        self.assertEqual(infix_to_postfix(" - << 5 >> 7 >> -5"), "5 << 7 >> -5 >> -")

    def test_prefix_to_postfix_04(self) -> None:
        self.assertEqual(infix_to_postfix("** 7 6 4 2"), "7 6 4 2 **")

    def test_prefix_to_postfix_05(self) -> None:
        self.assertEqual(infix_to_postfix('3 >> 5 ** 8 >> 4'), '3 5 >> 8 4 >> **')

    def test_prefix_to_postfix_06(self) -> None:
        with self.assertRaises(IndexError):
            prefix_to_postfix('e')

    def test_prefix_to_postfix_07(self) -> None:
        self.assertEqual(prefix_to_postfix(""), "")

if __name__ == "__main__":
    unittest.main()
