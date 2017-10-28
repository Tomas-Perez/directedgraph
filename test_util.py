import unittest
from digraph import *
from digraph_util import *


class TestDigraphUtil(unittest.TestCase):
    def test_plain_search(self):
        graph = Digraph()
        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")

        for x, y in zip(plain_search(graph), graph.vertices):
            self.assertEqual(x, y)

    def test_dfs(self):
        graph = Digraph()
        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")
        graph.add_edge(graph.index_of('a'), graph.index_of('c'))
        graph.add_edge(graph.index_of('a'), graph.index_of('b'))
        graph.add_edge(graph.index_of('b'), graph.index_of('d'))
        graph.add_edge(graph.index_of('c'), graph.index_of('d'))
        graph.add_edge(graph.index_of('d'), graph.index_of('e'))

        expected = map(lambda vertex: graph.index_of(vertex), ['a', 'b', 'd', 'e', 'c'])

        for x, y in zip(dfs(graph), expected):
            self.assertEqual(x, y)

    def test_bfs(self):
        graph = Digraph()
        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")
        graph.add_edge(graph.index_of('a'), graph.index_of('c'))
        graph.add_edge(graph.index_of('a'), graph.index_of('b'))
        graph.add_edge(graph.index_of('b'), graph.index_of('d'))
        graph.add_edge(graph.index_of('c'), graph.index_of('d'))
        graph.add_edge(graph.index_of('d'), graph.index_of('e'))

        expected = map(lambda vertex: graph.index_of(vertex), ['a', 'c', 'b', 'd', 'e'])

        for x, y in zip(bfs(graph), expected):
            self.assertEqual(x, y)

    def test_sinks(self):
        graph = Digraph()
        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")
        graph.add_edge(graph.index_of('a'), graph.index_of('c'))
        graph.add_edge(graph.index_of('a'), graph.index_of('b'))
        graph.add_edge(graph.index_of('b'), graph.index_of('d'))
        graph.add_edge(graph.index_of('c'), graph.index_of('d'))
        graph.add_edge(graph.index_of('d'), graph.index_of('e'))

        self.assertEqual(1, number_of_sinks(graph))

        graph.add_vertex('f')

        self.assertEqual(2, number_of_sinks(graph))

        graph.add_edge(graph.index_of('e'), graph.index_of('f'))

        self.assertEqual(1, number_of_sinks(graph))

        graph.add_vertex('x')

        self.assertEqual(2, number_of_sinks(graph))

        graph.add_edge(graph.index_of('b'), graph.index_of('x'))
        graph.add_edge(graph.index_of('c'), graph.index_of('x'))
        graph.add_edge(graph.index_of('e'), graph.index_of('x'))

        self.assertEqual(2, number_of_sinks(graph))
        graph.add_edge(graph.index_of('f'), graph.index_of('x'))

        self.assertEqual(1, number_of_sinks(graph))

    def test_sources(self):
        graph = Digraph()
        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")
        graph.add_edge(graph.index_of('a'), graph.index_of('c'))
        graph.add_edge(graph.index_of('a'), graph.index_of('b'))
        graph.add_edge(graph.index_of('b'), graph.index_of('d'))
        graph.add_edge(graph.index_of('c'), graph.index_of('d'))
        graph.add_edge(graph.index_of('d'), graph.index_of('e'))

        self.assertEqual(1, number_of_sources(graph))

        graph.add_vertex('f')

        self.assertEqual(2, number_of_sources(graph))

        graph.add_edge(graph.index_of('f'), graph.index_of('a'))

        self.assertEqual(1, number_of_sources(graph))

        graph.add_vertex('x')
        self.assertEqual(2, number_of_sources(graph))

        graph.add_edge(graph.index_of('x'), graph.index_of('b'))
        graph.add_edge(graph.index_of('x'), graph.index_of('c'))
        graph.add_edge(graph.index_of('x'), graph.index_of('e'))
        self.assertEqual(2, number_of_sources(graph))

        graph.add_edge(graph.index_of('x'), graph.index_of('f'))

        self.assertEqual(1, number_of_sources(graph))

    def test_weakly_connected(self):
        graph = Digraph()
        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")
        graph.add_edge(graph.index_of('a'), graph.index_of('c'))
        graph.add_edge(graph.index_of('a'), graph.index_of('b'))
        graph.add_edge(graph.index_of('b'), graph.index_of('d'))
        graph.add_edge(graph.index_of('c'), graph.index_of('d'))
        graph.add_edge(graph.index_of('d'), graph.index_of('e'))

        self.assertTrue(is_weakly_connected(graph))

        graph.add_vertex('f')

        self.assertFalse(is_weakly_connected(graph))

        graph.add_edge(graph.index_of('d'), graph.index_of('f'))

        self.assertTrue(is_weakly_connected(graph))

    def test_path_exists(self):
        graph = Digraph()
        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")
        graph.add_edge(graph.index_of('a'), graph.index_of('c'))
        graph.add_edge(graph.index_of('a'), graph.index_of('b'))
        graph.add_edge(graph.index_of('b'), graph.index_of('d'))
        graph.add_edge(graph.index_of('c'), graph.index_of('d'))
        graph.add_edge(graph.index_of('d'), graph.index_of('e'))

        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('b')))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('d')))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('e')))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('c')))

        self.assertTrue(path_exists(graph, graph.index_of('b'), graph.index_of('d')))
        self.assertTrue(path_exists(graph, graph.index_of('b'), graph.index_of('e')))

        self.assertTrue(path_exists(graph, graph.index_of('c'), graph.index_of('d')))
        self.assertTrue(path_exists(graph, graph.index_of('c'), graph.index_of('e')))

        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('b'), 1))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('c'), 1))
        self.assertFalse(path_exists(graph, graph.index_of('a'), graph.index_of('d'), 1))
        self.assertFalse(path_exists(graph, graph.index_of('a'), graph.index_of('e'), 1))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('d'), 2))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('e'), 3))

        self.assertFalse(path_exists(graph, graph.index_of('a'), graph.index_of('f'), 3))
        self.assertFalse(path_exists(graph, graph.index_of('a'), graph.index_of('f')))
        self.assertFalse(path_exists(graph, graph.index_of('a'), 18))

        graph.add_vertex('f')
        self.assertFalse(path_exists(graph, graph.index_of('a'), graph.index_of('f')))
        self.assertFalse(path_exists(graph, graph.index_of('f'), graph.index_of('b')))
        self.assertFalse(path_exists(graph, graph.index_of('f'), graph.index_of('f')))

        graph.add_edge(graph.index_of('f'), graph.index_of('f'))
        self.assertTrue(path_exists(graph, graph.index_of('f'), graph.index_of('f')))

    def test_warshall(self):
        graph = Digraph()
        graph.add_vertex("a")
        graph.add_vertex("b")
        graph.add_vertex("c")
        graph.add_vertex("d")
        graph.add_vertex("e")
        graph.add_edge(graph.index_of('a'), graph.index_of('c'))
        graph.add_edge(graph.index_of('a'), graph.index_of('b'))
        graph.add_edge(graph.index_of('b'), graph.index_of('d'))
        graph.add_edge(graph.index_of('c'), graph.index_of('d'))
        graph.add_edge(graph.index_of('d'), graph.index_of('e'))

        matrix = warshall(graph)

        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('b'), transitive_closure=matrix))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('d'), transitive_closure=matrix))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('e'), transitive_closure=matrix))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('c'), transitive_closure=matrix))

        self.assertTrue(path_exists(graph, graph.index_of('b'), graph.index_of('d'), transitive_closure=matrix))
        self.assertTrue(path_exists(graph, graph.index_of('b'), graph.index_of('e'), transitive_closure=matrix))

        self.assertTrue(path_exists(graph, graph.index_of('c'), graph.index_of('d'), transitive_closure=matrix))
        self.assertTrue(path_exists(graph, graph.index_of('c'), graph.index_of('e'), transitive_closure=matrix))

        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('b'), transitive_closure=matrix))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('c'), transitive_closure=matrix))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('d'), transitive_closure=matrix))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('e'), transitive_closure=matrix))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('d'), transitive_closure=matrix))
        self.assertTrue(path_exists(graph, graph.index_of('a'), graph.index_of('e'), transitive_closure=matrix))

        self.assertFalse(path_exists(graph, graph.index_of('a'), graph.index_of('f'), transitive_closure=matrix))
        self.assertFalse(path_exists(graph, graph.index_of('a'), graph.index_of('f'), transitive_closure=matrix))

        self.assertFalse(path_exists(graph, graph.index_of('a'), 18, transitive_closure=matrix))

if __name__ == '__main__':
    unittest.main()
