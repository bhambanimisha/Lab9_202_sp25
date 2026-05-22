import unittest
from lab9_p3 import dijkstra

class Testdijkstra(unittest.TestCase):

    def test_dijkstra(self):
        graph_3 = {
            1: {2: 2, 3: 4},
            2: {3: 1, 4: 7},
            3: {5: 3},
            4: {5: 1},
            5: {}
        }
        start_node = 1
        expected_distances = {
            1: 0,
            2: 2,
            3: 3,
            4: 9,
            5: 6
        }
        result = dijkstra(graph_3, start_node)
        self.assertEqual(result, expected_distances)

    def test_dijkstra_with_unreachable_node(self):
        graph_3 = {
            1: {2: 2, 3: 4},
            2: {3: 1, 4: 7},
            3: {5: 3},
            4: {5: 1},
            5: {},
            6: {}
        }
        start_node = 1
        expected_distances = {
            1: 0,
            2: 2,
            3: 3,
            4: 9,
            5: 6,
            6: float('inf')
        }
        result = dijkstra(graph_3, start_node)
        self.assertEqual(result, expected_distances)

    def test_dijkstra_with_negative_weights(self):
        graph_3 = {
            1: {2: 2, 3: -4},  # Negative weight
            2: {3: 1, 4: 7},
            3: {5: 3},
            4: {5: 1},
            5: {}
        }
        start_node = 1
        self.assertRaises(ValueError)



if __name__ == '__main__':
    unittest.main()
