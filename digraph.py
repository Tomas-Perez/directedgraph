from collections import namedtuple
Edge = namedtuple("Edge", "from_vertex to_vertex")


class Digraph:
    def __init__(self, max_order=-1):
        self.edges = []
        self.vertices = dict()
        self.max_order = max_order
        self.key_gen = 0

    def add_vertex(self, data):
        if self.order == self.max_order:
            return
        self.vertices[self.key_gen] = data
        self.key_gen += 1

    def remove_vertex(self, key):
        for x in self.edges:
            if x.from_vertex is key or x.to_vertex is key:
                self.edges.remove(x)
        return self.vertices.pop(key)

    @property
    def order(self):
        return len(self.vertices)

    @property
    def number_of_edges(self):
        return len(self.edges)

    def index_of(self, data):
        for key, vertex in self.vertices.items():
            if vertex is data:
                return key

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            raise ValueError('No such vertices')
        self.edges.append(Edge(from_vertex, to_vertex))

    def remove_edge(self, from_vertex, to_vertex):
        try:
            return self.edges.remove(Edge(from_vertex, to_vertex))
        except ValueError:
            raise ValueError("Edge does not exist") from None

    def get_vertex(self, index):
        return self.vertices[index]

    def get_adjacency_list(self, vertex):
        return [x.to_vertex for x in self.edges if x.from_vertex is vertex]