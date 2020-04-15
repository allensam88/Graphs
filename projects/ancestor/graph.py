"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()
        queue.enqueue([starting_vertex])
        ancestor_path = [starting_vertex]

        while queue.size() > 0:
            path = queue.dequeue()
            node = path[-1]
            if node not in visited:
                if len(path) > len(ancestor_path):
                    ancestor_path = path
                elif len(path) == len(ancestor_path):
                    if path[-1] < ancestor_path[-1]:
                        ancestor_path = path
                visited.add(node)
                neighbors = self.get_neighbors(node)
                for next_node in neighbors:
                    new_path = list(path)
                    new_path.append(next_node)
                    queue.enqueue(new_path)

        return ancestor_path

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        stack.push([starting_vertex])
        ancestor_path = [starting_vertex]

        while stack.size() > 0:
            path = stack.pop()
            node = path[-1]
            if node not in visited:
                if len(path) > len(ancestor_path):
                    ancestor_path = path
                elif len(path) == len(ancestor_path):
                    if path[-1] < ancestor_path[-1]:
                        ancestor_path = path
                visited.add(node)
                neighbors = self.get_neighbors(node)
                for next_node in neighbors:
                    new_path = list(path)
                    new_path.append(next_node)
                    stack.push(new_path)

        return ancestor_path
