'''Defines graph structures.'''
from random import random


def search_transitive_closure(v, visited):
    '''
        Searchs for a transitive closure.

        v (Vertex): Reference vertex.
        visited (set): Already visited vertices.
    '''
    visited.add(v)
    for v_ in v.neighbours:
        if not v_ in visited:
            search_transitive_closure(v_, visited)

    return visited


class Vertex:
    '''
        A graph's vertex.
    '''
    def __init__(self, key):
        self.key = key
        self.neighbours = set()

    def degree(self):
        '''
            Returns the vertex's degree.
        '''
        return len(self.neighbours)

class Graph:
    '''
        The graph itself.
    '''
    def __init__(self):
        self.vertices = {}

    # Basic operations

    def add(self, v):
        '''
            Adds a vertex to the graph.

            v (obj): Vertex to be add.
        '''
        self.vertices[v] = Vertex(v)

    def remove(self, v):
        '''
            Removes a vertex from the graph.

            v (obj): Vertex to be removed.
        '''
        del self.vertices[v]

    def link(self, v1, v2):
        '''
            Links two vertices by a bidirectional edge.

            v1 (obj): First vertex.
            v2 (obj): Second vertex.
        '''
        self.vertices[v1].neighbours.add(self.vertices[v2])
        self.vertices[v2].neighbours.add(self.vertices[v1])

    def unlink(self, v1, v2):
        '''
            Unlinks two vertices.

            v1 (obj): First vertex.
            v2 (obj): Second vertex.
        '''
        self.vertices[v1].neighbours.discard(self.vertices[v2])
        self.vertices[v2].neighbours.discard(self.vertices[v1])

    def order(self):
        '''
            Graph's order.
        '''
        return len(self.vertices)

    def random_vertex(self):
        '''
            Gets a random vertex from the graph.
        '''
        return random.choice(list(self.vertices.values()))

    def neighbours(self, key):
        '''
            Gets a set with a vertex's neighbours.

            key (obj): The vertex.
        '''
        return self.vertices[key].neightbours

    def degree(self, key):
        '''
            Gets a vertex's degree.

            key (obj): The vertex.
        '''
        return self.vertices[key].degree()

    # Derived actions

    def regular(self):
        '''
            Checks if the graph is regular.
        '''
        # pegamos um vértice aleatório e calculamos o seu grau
        same_degree = len(self.random_vertex().neighbours)

        for v in self.vertices.values():
            if v.degree() != same_degree:
                return False

        return True

    def complete(self):
        '''
            Checks if the graph is complete.
        '''
        for _, v in self.vertices.items():
            for _, v_ in self.vertices.items():
                # verificamos se um vértice i está ligado com todo os outros
                # vértices j
                if not v_ in v.neighbours and v != v_:
                    return False

        return True

    def transitive_closure(self, key):
        '''
            Gets the transitive closure starting from the given key.

            key (obj): Reference vertex.
        '''
        if isinstance(key, Vertex):
            v = key
        else:
            v = self.vertices[key]
        visited = set()
        return search_transitive_closure(v, visited)

    def connected(self):
        '''
            Checks if the graph is connected.
        '''
        trans = self.transitive_closure(self.random_vertex())
        values = set(self.vertices.values())
        return len(trans ^ values) == 0

    def tree(self):
        '''
            Checks if the graph is a tree.
        '''
        return self.connected() and not self.has_cycle()

    def has_cycle(self, v=None, prev=None, visited=None):
        '''
            Check if the graph has a cycle.

            v (Vertex): Vertex to be checked against visited set.
                        If None, begins searching recursively for a cycle.
            prev (Vertex): Reference vertex.
            visited (set): Set of already visited vertices.
        '''
        if v is None:
            v = self.random_vertex()
            return self.has_cycle(v, v, set())
        if v in visited:
            return True

        visited.add(v)
        for v_ in v.neighbours:
            if v_ != prev:
                return self.has_cycle(v_, v, visited)
        visited.remove(v)
        return False

    # Extra

    def __getitem__(self, key):
        '''
            Overrides operator [] to get a vertex by a given key.

            key (obj): The vertex's key.
        '''
        return self.vertices[key]
