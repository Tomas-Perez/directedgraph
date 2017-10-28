import numpy as np


def plain_search(graph):
    return graph.vertices.__iter__()


def bfs(graph):
    return __traversal(graph, 'bfs')


def dfs(graph):
    return __traversal(graph, 'dfs')


def __traversal(graph, algorithm):
    aux = []
    visited = [False for _ in graph.vertices]
    aux.append(0)
    visited[0] = True
    while len(aux) > 0:
        if algorithm == 'bfs':
            current = aux.pop()
        elif algorithm == 'dfs':
            current = aux.pop(0)
        if not visited[current]:
            visited[current] = True
            aux.extend(graph.get_adjacency_list(current))
            yield current

    unvisited_indexes = map(lambda y: y[0], filter(lambda x: not x[1], enumerate(visited)))

    for index in unvisited_indexes:
        yield graph.vertices[index]

        # if len(aux) == 0:
        #     for index, visited_state in enumerate(visited):
        #         if not visited_state:
        #             yield graph.vertices[index]


def number_of_sinks(graph):
    is_sink_list = [True for _ in graph.vertices]
    for edge in graph.edges:
        is_sink_list[edge.from_index] = False
    return len(list(filter(lambda x: x, is_sink_list)))


def number_of_sources(graph):
    is_source_list = [True for _ in graph.vertices]
    for edge in graph.edges:
        is_source_list[edge.to_index] = False
    return len(list(filter(lambda x: x, is_source_list)))


def is_weakly_connected(graph):
    def get_non_directed_adjacency_list(vertex):
        result = []
        for x in graph.edges:
            if x.to_vertex is vertex:
                result.append(vertex)
            elif x.from_vertex is vertex:
                result.append(vertex)

        return result

    aux = []
    visited = [False for _ in graph.vertices]
    aux.append(0)
    visited[0] = True
    while len(aux) > 0:
        current = aux.pop()
        if not visited[current]:
            visited[current] = True
            aux.extend(get_non_directed_adjacency_list(current))

    return next((i for i in visited if not i), True)


def path_exists(graph, a, b, length=0):
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