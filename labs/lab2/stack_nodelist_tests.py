# Lab 2: Michelle Tan
# Instructor: Prof. Parkinson

import unittest
from stack_nodelist import *


class TestLab2(unittest.TestCase):

    def test_node_init(self) -> None:
        node1 = Node(1, None)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.rest, None)

        node2 = Node(2, node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.rest, node1)

    def test_node_eq(self) -> None:
        node1a = Node(1, None)
        node1b = Node(1, None)
        node2a = Node(2, node1a)
        node2b = Node(2, node1b)

        self.assertEqual(node1a, node1b)
        self.assertNotEqual(node1a, node2a)
        self.assertEqual(node2a, node2b)
        node1a = Node(3, None)
        self.assertNotEqual(node1a, node1b)

        self.assertFalse(node1a.__eq__(None))

    def test_node_repr(self) -> None:
        node = Node(2, Node(1, None))
        self.assertEqual(node.__repr__(), "Node(2, Node(1, None))")

    def test_stack_init(self) -> None:
        stack = Stack()
        self.assertEqual(stack.top, None)

        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.top, init_stack)

    def test_stack_eq(self) -> None:
        stack1 = Stack()
        stack2 = Stack()
        init_stack = Node(2, Node(1, None))
        stack4 = Stack(init_stack)
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack4)
        self.assertFalse(stack1.__eq__(None))

    def test_stack_repr(self) -> None:
        init_stack = Node(2, Node(1, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.__repr__(), "Stack(Node(2, Node(1, None)))")

    def test_is_empty_01(self) -> None:
        stack = Stack()
        self.assertEqual(stack.is_empty(), True)

    def test_is_empty_02(self) -> None:
        init_stack = Node(5, Node(5, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.is_empty(), False)

    def test_is_empty_03(self) -> None:
        init_stack = Node(2, Node(4, Node(64, None)))
        stack = Stack(init_stack)
        self.assertEqual(stack.is_empty(), False)

    def test_push_01(self) -> None:
        init_stack = Node(5, Node(2, Node(52, None)))
        stack = Stack(init_stack)
        stack.push(3)
        init_stack1 = Node(3, Node(5, Node(2, Node(52, None))))
        self.assertEqual(stack.top, init_stack1)

    def test_push_02(self) -> None:
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.push(4)

    def test_push_03(self) -> None:
        init_stack = Node(9, Node(2, None))
        stack = Stack(init_stack)
        stack.push(9)
        init_stack1 = Node(9, Node(9, Node(2, None)))
        self.assertEqual(stack.top, init_stack1)

    def test_pop_01(self) -> None:
        init_stack = Node(5, Node(2, Node(52, None)))
        stack = Stack(init_stack)
        self.assertEqual(stack.pop(), 5)

    def test_pop_02(self) -> None:
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_pop_03(self) -> None:
        init_stack = Node(24, Node(5, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.pop(), 24)

    def test_peek_01(self) -> None:
        init_stack = Node(5, Node(2, Node(52, None)))
        stack = Stack(init_stack)
        self.assertEqual(stack.peek(), 5)

    def test_peek_02(self) -> None:
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_peek_03(self) -> None:
        init_stack = Node(66, Node(24, Node(52, Node(53, None))))
        stack = Stack(init_stack)
        self.assertEqual(stack.peek(), 66)

    def test_size_01(self) -> None:
        init_stack = Node(5, Node(2, Node(52, None)))
        stack = Stack(init_stack)
        self.assertEqual(stack.size(), 3)

    def test_size_02(self) -> None:
        stack = Stack()
        self.assertEqual(stack.size(), 0)

    def test_size_03(self) -> None:
        init_stack = Node(6, Node(23, None))
        stack = Stack(init_stack)
        self.assertEqual(stack.size(), 2)


# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

if __name__ == '__main__':
    unittest.main()
