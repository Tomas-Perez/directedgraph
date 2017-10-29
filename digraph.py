from collections import namedtuple
from random import randint

Edge = namedtuple("Edge", "from_vertex to_vertex")


class Digraph:
    """
    Represent a Directed Graph 
    """
    def __init__(self, max_order=-1):
        """
        Default constructor
        :param max_order: maximum order limit, if -1, digraph capacity is unlimited.
        """
        self.edges = []
        self.vertices = dict()
        self.max_order = max_order
        self.key_gen = 0

    @property
    def order(self):
        return len(self.vertices)

    @property
    def number_of_edges(self):
        return len(self.edges)

    def add_vertex(self, data):
        """
        Add a vertex to the graph
        :param data: data to store in the vertex
        """
        if self.order == self.max_order:
            return
        self.vertices[self.key_gen] = data
        self.key_gen += 1

    def remove_vertex(self, key):
        """
        Remove a vertex and all its connected edges from the graph
        :param key: key referencing the vertex
        :return: removed vertex data
        """
        for x in self.edges:
            if x.from_vertex is key or x.to_vertex is key:
                self.edges.remove(x)
        return self.vertices.pop(key)

    def key_of(self, data):
        """
        Get the key of the given data stored in the graph
        :param data: data stored in the graph
        :return: key of given data stored in the graph, or -1 if it is not in the graph
        """
        for key, vertex in self.vertices.items():
            if vertex is data:
                return key
        return -1

    def add_edge(self, from_vertex, to_vertex):
        """
        Add an edge connecting two vertices
        :param from_vertex: source vertex key
        :param to_vertex: destination vertex key
        :raises ValueError if the vertices do not exist
        """
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            raise ValueError('No such vertices')
        self.edges.append(Edge(from_vertex, to_vertex))

    def remove_edge(self, from_vertex, to_vertex):
        """
        Remove an edge from the graph
        :param from_vertex: source vertex in the edge
        :param to_vertex: destination vertex in the edge
        :raises ValueError if the edge does not exist
        """
        try:
            return self.edges.remove(Edge(from_vertex, to_vertex))
        except ValueError:
            raise ValueError("Edge does not exist") from None

    def get_vertex(self, key):
        """
        Given a key returns the data referenced with that key in the graph
        :param key: key referencing the desired vertex
        :return: data stored in the desired vertex
        """
        return self.vertices[key]

    def get_adjacency_list(self, key):
        """
        Given a vertex returns a list of all vertices adjacent to it.
        :param key: key of the desired vertex
        :return: adjacency list of the desired vertex
        """
        return [x.to_vertex for x in self.edges if x.from_vertex is key]

    def edge_exists(self, from_vertex, to_vertex):
        """
        Returns whether an edge between the given vertices exists.
        :param from_vertex: source vertex in the graph
        :param to_vertex: destination vertex in the graph
        :return: True if the edge exists, False if it does not.
        """
        return from_vertex in self.vertices and \
            to_vertex in self.vertices and \
            Edge(from_vertex, to_vertex) in self.edges

    @classmethod
    def random(cls, vertex_amt, edge_amt):
        """
        Secondary constructor for a random digraph
        :param vertex_amt: amount of vertices
        :param edge_amt: amount of edges
        :return: random digraph with the given amount of vertices and edges
        """
        def random_vertices():
            def random_vertex():
                return result.key_of(randint(0, vertex_amt - 1))

            return random_vertex(), random_vertex()

        result = cls()

        for i in range(vertex_amt):
            result.add_vertex(i)

        for i in range(edge_amt):
            result.add_edge(*random_vertices())

        return result
