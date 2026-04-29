"""
<lab11.py>

Author(s): Lorenzo .S and Jerod Abraham
Created: 04-29-2026
Last Updated: Created: 04-29-2026
"""

class Graph_ES:
    """Graph ADT implementation using an edge set."""

    def __init__(self, vertices=None, edges=None):
        """
        Docstring for Graph_ES.__init__()
            - Description: Initialize graph with optional set of vertices and edges.
        """
        self._vertices = set()
        self._edges = set()

        if vertices is not None:
            for vertex in vertices:
                self.add_vertex(vertex)

        if edges is not None:
            for edge in edges:
                self.add_edge(edge)

    def __len__(self):
        """
        Docstring for Graph_ES.__len__()
            - Description: Returns the number of vertices in the graph.
        """
        return len(self._vertices)

    def __iter__(self):
        """
        Docstring for Graph_ES.__iter__()
            - Description: Iterates over all vertices in the graph.
        """
        return iter(self._vertices)

    def add_vertex(self, vertex):
        """
        Docstring for Graph_ES.add_vertex()
            - Description: Adds vertex to the graph.
        """
        self._vertices.add(vertex)

    def remove_vertex(self, vertex):
        """
        Docstring for Graph_ES.remove_vertex()
            - Description: Removes vertex from the graph and removes all connected edges.
        """
        if vertex not in self._vertices:
            raise KeyError(vertex)

        self._vertices.remove(vertex)

        self._edges = {}

        for edge in self._edges:
            if edge[0] != vertex and edge[1] != vertex:
                self._edges.add(edge)


        # edge for edge in self._edges if edge[0] != vertex and edge[1] != vertex

    def add_edge(self, edge):
        """
        Docstring for Graph_ES.add_edge()
            - Description: Adds edge to the graph.
        """
        start_vertex, end_vertex = edge

        self.add_vertex(start_vertex)
        self.add_vertex(end_vertex)

        self._edges.add(edge)

    def remove_edge(self, edge):
        """
        Docstring for Graph_ES.remove_edge()
            - Description: Removes edge from the graph.
        """
        if edge not in self._edges:
            raise KeyError(edge)

        self._edges.remove(edge)

    def _neighbors(self, vertex):
        """
        Docstring for Graph_ES._neighbors()
            - Description: Returns an iterable collection of neighbors of vertex.
        """
        for start_vertex, end_vertex in self._edges:
            if start_vertex == vertex:
                yield end_vertex


class Graph_AS:
    """Graph ADT implementation using adjacency sets."""

    def __init__(self, vertices=None, edges=None):
        """
        Docstring for Graph_AS.__init__()
            - Description: Initialize graph with optional set of vertices and edges.
        """
        self._adjacency_sets = dict()

        if vertices is not None:
            for vertex in vertices:
                self.add_vertex(vertex)

        if edges is not None:
            for edge in edges:
                self.add_edge(edge)

    def __len__(self):
        """
        Docstring for Graph_AS.__len__()
            - Description: Returns the number of vertices in the graph.
        """
        return len(self._adjacency_sets)

    def __iter__(self):
        """
        Docstring for Graph_AS.__iter__()
            - Description: Iterates over all vertices in the graph.
        """
        return iter(self._adjacency_sets)

    def add_vertex(self, vertex):
        """
        Docstring for Graph_AS.add_vertex()
            - Description: Adds vertex to the graph.
        """
        if vertex not in self._adjacency_sets:
            self._adjacency_sets[vertex] = set()

    def remove_vertex(self, vertex):
        """
        Docstring for Graph_AS.remove_vertex()
            - Description: Removes vertex from the graph and removes all connected edges.
        """
        if vertex not in self._adjacency_sets:
            raise KeyError(vertex)

        del self._adjacency_sets[vertex]

        for neighbor_set in self._adjacency_sets.values():
            neighbor_set.discard(vertex)

    def add_edge(self, edge):
        """
        Docstring for Graph_AS.add_edge()
            - Description: Adds edge to the graph.
        """
        start_vertex, end_vertex = edge

        self.add_vertex(start_vertex)
        self.add_vertex(end_vertex)

        self._adjacency_sets[start_vertex].add(end_vertex)

    def remove_edge(self, edge):
        """
        Docstring for Graph_AS.remove_edge()
            - Description: Removes edge from the graph.
        """
        start_vertex, end_vertex = edge

        if start_vertex not in self._adjacency_sets or end_vertex not in self._adjacency_sets[start_vertex]:
            raise KeyError(edge)

        self._adjacency_sets[start_vertex].remove(end_vertex)

    def _neighbors(self, vertex):
        """
        Docstring for Graph_AS._neighbors()
            - Description: Returns an iterable collection of neighbors of vertex.
        """
        if vertex not in self._adjacency_sets:
            raise KeyError(vertex)

        return iter(self._adjacency_sets[vertex])