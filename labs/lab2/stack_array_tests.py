# Lab 2: Michelle Tan
# Instructor: Prof. Parkinson

import unittest
from stack_array import Stack


class TestLab2(unittest.TestCase):

    def test_init(self) -> None:
        stack = Stack(5)
        self.assertEqual(stack.items, [None] * 5)
        self.assertEqual(stack.capacity, 5)

        stack = Stack(5, [1, 2])
        self.assertEqual(stack.items[0:2], [1, 2])
        self.assertEqual(stack.capacity, 5)

        with self.assertRaises(IndexError):
            Stack(5, [1, 2, 3, 4, 5, 6])

    def test_eq(self) -> None:
        stack1 = Stack(5)
        stack2 = Stack(5)
        stack3 = Stack(10)
        stack4 = Stack(5, [1, 2])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_repr(self) -> None:
        stack = Stack(5, [1, 2])
        self.assertEqual(stack.__repr__(), "Stack(5, [1, 2])")

    # WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.
    def test_is_empty_01(self) -> None:
        stack = Stack(0, [])
        self.assertEqual(stack.is_empty(), True)

    def test_is_empty_02(self) -> None:
        stack = Stack(5, [3, 6, None])
        self.assertEqual(stack.is_empty(), False)

    def test_is_full_01(self) -> None:
        stack = Stack(3, [1, 3, None])
        self.assertEqual(stack.is_full(), True)

    def test_is_full_02(self) -> None:
        stack = Stack(3, [1, 3])
        self.assertEqual(stack.is_full(), False)

    def test_is_full_03(self) -> None:
        stack = Stack(9, [])
        self.assertEqual(stack.is_full(), False)

    def test_push_01(self) -> None:
        stack = Stack(5, [2, 3, 4, 5])
        stack.push(7)
        self.assertEqual(stack.items, [2, 3, 4, 5, 7])

    def test_push_02(self) -> None:
        stack = Stack(0, [])
        with self.assertRaises(IndexError):
            stack.push(7)

    def test_push_03(self) -> None:
        stack = Stack(3, [0, None])
        stack.push(9)
        self.assertEqual(stack.items, [0, None, 9])

    def test_pop_01(self) -> None:
        stack = Stack(5, [2, 3, 4, 5])
        self.assertEqual(stack.pop(), 5)

    def test_pop_02(self) -> None:
        stack = Stack(0, [])
        with self.assertRaises(IndexError):
            stack.pop()

    def test_pop_03(self) -> None:
        stack = Stack(4, [2, 3])
        self.assertEqual(stack.pop(), 3)

    def test_peek_01(self) -> None:
        stack = Stack(4, [2, 7, 3])
        self.assertEqual(stack.peek(), 3)

    def test_peek_02(self) -> None:
        stack = Stack(0, [])
        with self.assertRaises(IndexError):
            stack.peek()

    def test_peek_03(self) -> None:
        stack = Stack(7, [None, 3, 5])
        self.assertEqual(stack.peek(), 5)

    def test_size_01(self) -> None:
        stack = Stack(3, [2, 5, 3])
        self.assertEqual(stack.size(), 3)

    def test_size_02(self) -> None:
        stack = Stack(0, [])
        self.assertEqual(stack.size(), 0)

    def test_size_03(self) -> None:
        stack = Stack(7, [8, None])
        self.assertEqual(stack.size(), 2)


if __name__ == '__main__':
    unittest.main()
