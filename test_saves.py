from digraph_util import *
from digraph import *


def save_test():
    graph = Digraph()
    graph.add_vertex("a")
    graph.add_vertex("b")
    graph.add_vertex("c")
    graph.add_vertex("d")
    graph.add_vertex("e")
    graph.add_edge(graph.key_of('a'), graph.key_of('c'))
    graph.add_edge(graph.key_of('a'), graph.key_of('b'))
    graph.add_edge(graph.key_of('b'), graph.key_of('d'))
    graph.add_edge(graph.key_of('c'), graph.key_of('d'))
    graph.add_edge(graph.key_of('d'), graph.key_of('e'))

    save(graph, 'lmao', view=True, format='png')


def random_test():
    graph = Digraph.random(20, 35)
    save(graph, 'random', view=True)

if __name__ == '__main__':
    random_test()