import numpy as np
import graphviz


def plain_search(graph):
    """
    Iterator over the given graph vertices in the order they were inserted.
    :param graph: graph to iterate over
    :return: vertex iterator
    """
    return iter(graph.vertices)


def bfs(graph):
    """
    Iterator over the given graph via Breath-First-Search
    :param graph: graph to iterate over
    :return: vertex iterator
    """
    return __traversal(graph, 'bfs')


def dfs(graph):
    """
    Iterator over the given graph via Depth-First-Search
    :param graph: graph to iterate over
    :return: vertex iterator
    """
    return __traversal(graph, 'dfs')


def __traversal(graph, algorithm):
    aux = []
    visited = {k: False for k in graph.vertices}
    first = next(iter(graph.vertices))
    aux.append(first)
    while len(aux) > 0:
        if algorithm == 'bfs':
            current = aux.pop(0)
        elif algorithm == 'dfs':
            current = aux.pop()
        if not visited[current]:
            visited[current] = True
            aux.extend(graph.get_adjacency_list(current))
            yield current

    for vertex, was_visited in visited.items():
        if not was_visited:
            yield vertex


def number_of_sinks(graph):
    """
    Get the number of sink vertices in the given graph.
    :param graph: graph to count sinks on
    :return: number of sink vertices in the graph
    """
    is_sink_dict = {k: True for k in graph.vertices}
    for edge in graph.edges:
        is_sink_dict[edge.from_vertex] = False

    return sum(map(lambda is_sink: is_sink, is_sink_dict.values()))


def number_of_sources(graph):
    """
    Get the number of source vertices in the given graph.
    :param graph: graph to count sources on.
    :return: number of source vertices in the graph
    """
    is_source_dict = {k: True for k in graph.vertices}
    for edge in graph.edges:
        is_source_dict[edge.to_vertex] = False

    return sum(map(lambda is_sink: is_sink, is_source_dict.values()))


def is_weakly_connected(graph):
    """
    Given a graph, return whether it is weakly connected or not.
    :param graph: graph to check
    :return: True if the graph is weakly connected, False if it is not.
    """
    def get_non_directed_adjacency_list(vertex):
        result = []
        for x in graph.edges:
            if x.to_vertex is vertex:
                result.append(x.from_vertex)
            elif x.from_vertex is vertex:
                result.append(x.to_vertex)

        return result

    aux = []
    visited = {k: False for k in graph.vertices}
    first = next(iter(graph.vertices))
    aux.append(first)
    while len(aux) > 0:
        current = aux.pop()
        if not visited[current]:
            visited[current] = True
            aux.extend(get_non_directed_adjacency_list(current))

    return next((i for i in visited.values() if not i), True)


def path_exists(graph, a, b, length=0, transitive_closure=None):
    """
    Given a graph and two vertices returns whether a path between them exists.
    :param graph: graph to search on
    :param a: source vertex
    :param b: destination vertex
    :param length: max path length, 0 = unlimited
    :param transitive_closure: transitive closure of the graph, significantly reduces execution time
    :return: True if a path exists, False if it does not.
    """
    if transitive_closure is not None:
        if a == -1 or b == -1:
            return False
        try:
            return transitive_closure[a, b]
        except IndexError:
            return False

    visited = []

    def helper_path_exists(from_vertex, current_len=1):
        a_adjacency_list = graph.get_adjacency_list(from_vertex)
        visited.append(from_vertex)
        path_of_len_exists = b in a_adjacency_list
        if path_of_len_exists:
            return True
        elif current_len == length:
            return False
        else:
            for x in a_adjacency_list:
                if x not in visited:
                    if helper_path_exists(x, current_len + 1):
                        return True
            return False

    return helper_path_exists(a)


def warshall(graph):
    """
    Given a graph, calculates and returns its transitive closure
    :param graph: graph to calculate the closure to
    :return: the given graph's transitive closure
    """
    order = graph.order
    matrix = np.full((order, order), False)

    for i in range(order):
        for j in range(order):
            matrix[i, j] = path_exists(graph, i, j, 1)

    for k in range(order):
        for i in range(order):
            for j in range(order):
                matrix[i, j] |= matrix[i, k] and matrix[k, j]

    return matrix


def save(graph, name, view=False, s_format='pdf'):
    """
    Render and save the given graph with Graphviz.
    :param graph: graph to save
    :param name: name of the saved file
    :param view: True to show the result, False to not show it.
    :param s_format: format to save the graph on (png, pdf, and more).
    """
    dot = graphviz.Digraph(name=name, format=s_format)
    for vertex, data in graph.vertices.items():
        dot.node(str(vertex), str(data))

    for edge in graph.edges:
        dot.edge(str(edge.from_vertex), str(edge.to_vertex))

    dot.render(view=view)
