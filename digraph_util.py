import numpy as np


def plain_search(graph):
    return iter(graph.vertices)


def bfs(graph):
    return __traversal(graph, 'bfs')


def dfs(graph):
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
    is_sink_dict = {k: True for k in graph.vertices}
    for edge in graph.edges:
        is_sink_dict[edge.from_vertex] = False

    return sum(map(lambda is_sink: is_sink, is_sink_dict.values()))


def number_of_sources(graph):
    is_source_dict = {k: True for k in graph.vertices}
    for edge in graph.edges:
        is_source_dict[edge.to_vertex] = False

    return sum(map(lambda is_sink: is_sink, is_source_dict.values()))


def is_weakly_connected(graph):
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
    if transitive_closure is not None:
        if a == -1 or b == -1:
            return False
        try:
            return transitive_closure[a, b]
        except IndexError:
            return False

    def helper_path_exists(from_vertex, current_len=1):
        a_adjacency_list = graph.get_adjacency_list(from_vertex)
        path_of_len_exists = b in a_adjacency_list
        if path_of_len_exists:
            return True
        elif current_len == length:
            return False
        else:
            for x in a_adjacency_list:
                if helper_path_exists(x, current_len + 1):
                    return True
            return False

    return helper_path_exists(a)


def warshall(graph):
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
