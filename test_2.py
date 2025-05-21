import unittest
from lab9_p2 import bfs

class TestBFS(unittest.TestCase):

    def test_linear_graph(self):
        graph = {
            1: [2],
            2: [3],
            3: [4],
            4: []
        }
        self.assertEqual(bfs(graph, 1), [1, 2, 3, 4])

    def test_branching_graph(self):
        graph = {
            1: [2, 3],
            2: [4],
            3: [4],
            4: []
        }
        self.assertEqual(bfs(graph, 1), [1, 2, 3, 4])

    def test_tie_breaking(self):
        graph = {
            1: [3, 2],  # Unordered on purpose
            2: [4],
            3: [4],
            4: []
        }
        # Should visit 2 before 3 due to numerical tie-breaking
        self.assertEqual(bfs(graph, 1), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
