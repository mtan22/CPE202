import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self) -> None:
        g = Graph('test1.txt')
        self.assertEqual([['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']], g.conn_components())
        self.assertTrue(g.is_bipartite()) #pragma: no cover
        
    def test_02(self) -> None:
        g = Graph('test2.txt')
        self.assertEqual([['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']], g.conn_components())
        self.assertFalse(g.is_bipartite()) #pragma: no cover

    def test_03(self) -> None:
        with self.assertRaises(FileNotFoundError):
            Graph('test4.txt')

    def test_04(self) -> None:
        g = Graph('test2.txt')
        self.assertEqual(None, g.get_vertex(None))

    def test_05(self) -> None:
        g = Graph('test2.txt')
        self.assertEqual(['v1', 'v2', 'v3', 'v4', 'v6', 'v7', 'v8'], g.get_vertices())

if __name__ == '__main__':
   unittest.main()
