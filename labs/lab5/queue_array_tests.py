import unittest
from queue_array import Queue


class TestLab1(unittest.TestCase):

    def test_array(self) -> None:
        q = Queue(5)
        with self.assertRaises(IndexError):
            q.dequeue()
        self.assertEqual(q.is_empty(), True)
        self.assertEqual(q.items, [None, None, None, None, None])
        self.assertEqual(q.get_items(), [])
        q.enqueue(1)
        self.assertEqual(q.is_empty(), False)
        self.assertEqual(q.items, [1, None, None, None, None])
        q.enqueue(2)
        self.assertEqual(q.items, [1, 2, None, None, None])
        self.assertEqual(q.is_full(), False)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(3)
        self.assertEqual(q.is_full(), True)

    def test_init_eq(self) -> None:
        with self.assertRaises(IndexError):
            q = Queue(5, [1, 2, 3, 4, 5, 6])
        q1 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1.get_items(), [1, 2, 3, 4])
        q2 = Queue(5, [1, 2, 3, 4])
        self.assertEqual(q1, q2)

    def test_init_eq2(self) -> None:
        q1 = Queue(5, [1, 2, 3, 4, 5])
        q2 = Queue(5, [1, 2, 3, 4, 5])
        self.assertFalse(q1.__eq__(None))
        self.assertEqual(q1, q2)

    def test_repr(self) -> None:
        q1 = Queue(5, [])
        self.assertEqual(q1.__repr__(), "Queue(5, [])")

    def test_queue_simple(self) -> None:
        q = Queue(5)
        self.assertEqual(q.is_full(), False)
        self.assertEqual(q.is_empty(), True)
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.is_full(), True)
        with self.assertRaises(IndexError):
            q.enqueue(9)
        self.assertEqual(q.size(), 5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), 5)


if __name__ == '__main__':
    unittest.main()
