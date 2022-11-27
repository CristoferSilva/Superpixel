from graph.Key import Key
import numpy as np

class Vertex:
    Key = Key(0, 0)
    distance = 0
    value = 0
    color = np.array([0, 0, 0])
    # 0 = WHITE; 1 = BLACK ; 2 = GRAY
    listPreviousVertices = []

    def __init__(self, key, color):
        self.key = key
        self.color = color

    def get_previous_vertex_with_shortest_distance(self):
        if self.listPreviousVertices.count() == 0:
            return None
        vertex_key_with_shortest_distance = self.listPreviousVertices[0].distance
        vertex_with_shortest_distance = self

        for currentVertex in self.listPreviousVertices:

            current_distance = currentVertex.distance

            if current_distance < vertex_key_with_shortest_distance:
                vertex_key_with_shortest_distance = current_distance
                vertex_with_shortest_distance = current_distance

        return vertex_with_shortest_distance

    def __str__(self):
        return f"{self.key}<-)"

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return other.key == self.key
