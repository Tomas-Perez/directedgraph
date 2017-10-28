import unittest
from digraph import *


class TestDigraph(unittest.TestCase):
    def test_vertex(self):
        graph = Digraph()
        graph.add_vertex("43")
        graph.add_vertex("0")
        graph.add_vertex("12")
        self.assertEqual(graph.order, 3)
        self.assertEqual(graph.get_vertex(graph.index_of('43')), '43')
        self.assertEqual(graph.get_vertex(graph.index_of('0')), '0')
        self.assertEqual(graph.get_vertex(graph.index_of('12')), '12')
        self.assertRaises(KeyError, graph.get_vertex, 5)
        graph.remove_vertex(graph.index_of('43'))
        self.assertEqual(graph.order, 2)
        graph.remove_vertex(graph.index_of('12'))
        self.assertEqual(graph.order, 1)
        graph.remove_vertex(graph.index_of('0'))
        self.assertEqual(graph.order, 0)
        self.assertRaises(KeyError, graph.remove_vertex, 5)
        self.assertRaises(KeyError, graph.remove_vertex, 0)

    def test_edges(self):
        graph = Digraph()
        graph.add_vertex("43")
        graph.add_vertex("0")
        graph.add_vertex("12")
        graph.add_edge(graph.index_of('43'), graph.index_of('0'))
        graph.add_edge(graph.index_of('0'), graph.index_of('0'))
        graph.add_edge(graph.index_of('12'), graph.index_of('43'))
        self.assertEqual(graph.number_of_edges, 3)
        graph.remove_edge(graph.index_of('43'), graph.index_of('0'))
        self.assertEqual(graph.number_of_edges, 2)
        graph.remove_edge(graph.index_of('0'), graph.index_of('0'))
        self.assertEqual(graph.number_of_edges, 1)
        graph.remove_edge(graph.index_of('12'), graph.index_of('43'))
        self.assertEqual(graph.number_of_edges, 0)
        self.assertEqual(graph.order, 3)
        self.assertRaises(ValueError, graph.remove_edge, 0, 2)

    def test_vertex_and_edges(self):
        graph = Digraph()
        graph.add_vertex("43")
        graph.add_vertex("0")
        graph.add_vertex("12")
        graph.add_edge(graph.index_of('43'), graph.index_of('0'))
        graph.add_edge(graph.index_of('0'), graph.index_of('0'))
        graph.add_edge(graph.index_of('12'), graph.index_of('43'))
        self.assertEqual(graph.order, 3)
        self.assertEqual(graph.number_of_edges, 3)

        graph.remove_vertex(graph.index_of('43'))
        self.assertEqual(graph.order, 2)
        self.assertEqual(graph.number_of_edges, 1)
        graph.remove_vertex(graph.index_of('0'))
        self.assertEqual(graph.order, 1)
        self.assertEqual(graph.number_of_edges, 0)

    def test_adjacency_list(self):
        graph = Digraph()
        graph.add_vertex("43")
        graph.add_vertex("0")
        graph.add_vertex("12")
        graph.add_edge(graph.index_of('43'), graph.index_of('0'))
        graph.add_edge(graph.index_of('0'), graph.index_of('0'))
        graph.add_edge(graph.index_of('12'), graph.index_of('43'))

        expected = [graph.index_of('0')]
        self.assertEqual(graph.get_adjacency_list(graph.index_of('43')), expected)
        self.assertEqual(graph.get_adjacency_list(graph.index_of('0')), expected)
        self.assertNotEqual(graph.get_adjacency_list(graph.index_of('12')), expected)
        expected_2 = [graph.index_of('43')]
        self.assertEqual(graph.get_adjacency_list(graph.index_of('12')), expected_2)

    def test_edge_exists(self):
        graph = Digraph()
        graph.add_vertex("43")
        graph.add_vertex("0")
        graph.add_vertex("12")
        graph.add_edge(graph.index_of('43'), graph.index_of('0'))
        graph.add_edge(graph.index_of('0'), graph.index_of('0'))
        graph.add_edge(graph.index_of('12'), graph.index_of('43'))

        self.assertTrue(graph.edge_exists(graph.index_of('43'), graph.index_of('0')))
        self.assertTrue(graph.edge_exists(graph.index_of('0'), graph.index_of('0')))
        self.assertTrue(graph.edge_exists(graph.index_of('12'), graph.index_of('43')))

        self.assertFalse(graph.edge_exists(graph.index_of('0'), graph.index_of('12')))
        self.assertFalse(graph.edge_exists(graph.index_of('0'), graph.index_of('43')))

if __name__ == '__main__':
    unittest.main()