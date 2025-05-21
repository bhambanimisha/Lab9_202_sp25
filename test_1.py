import unittest
from lab9_p1 import graph_1, graph_2

class TestGraphs(unittest.TestCase):

    # ----- Graph 1 (Undirected) -----
    def test_graph_1_has_keys(self):
        self.assertIn(1, graph_1)
        self.assertIn(2, graph_1)
        self.assertIn(3, graph_1)
        self.assertIn(4, graph_1)
        self.assertIn(5, graph_1)
        self.assertIn(6, graph_1)

    def test_graph_1_value_types(self):
        self.assertIsInstance(graph_1[1], list)
        self.assertIsInstance(graph_1[2], list)
        self.assertIsInstance(graph_1[3], list)
        self.assertIsInstance(graph_1[4], list)
        self.assertIsInstance(graph_1[5], list)
        self.assertIsInstance(graph_1[6], list)

    def test_graph_1_spot_adjacency(self):
        self.assertIn(4, graph_1[5])
        self.assertIn(5, graph_1[4])
        self.assertIn(3, graph_1[2])
        self.assertIn(2, graph_1[1])

    # ----- Graph 2 (Directed) -----
    def test_graph_2_has_keys(self):
        self.assertIn(1, graph_2)
        self.assertIn(2, graph_2)
        self.assertIn(3, graph_2)
        self.assertIn(4, graph_2)
        self.assertIn(5, graph_2)
        self.assertIn(6, graph_2)

    def test_graph_2_value_types(self):
        self.assertIsInstance(graph_2[1], list)
        self.assertIsInstance(graph_2[2], list)
        self.assertIsInstance(graph_2[3], list)
        self.assertIsInstance(graph_2[4], list)
        self.assertIsInstance(graph_2[5], list)
        self.assertIsInstance(graph_2[6], list)

    def test_graph_2_spot_adjacency(self):
        self.assertIn(2, graph_2[1])
        self.assertEqual(graph_2[3], [])
        self.assertIn(5, graph_2[4])
        self.assertIn(4, graph_2[6])

if __name__ == '__main__':
    unittest.main()
