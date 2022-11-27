import numpy as np
import cv2
from matplotlib import pyplot as plt
from graph.Key import Key
from graph.Vertex import Vertex

class Graph:
    def __init__(self, img_path, superpixel_quantity):
        self.vertices = []
        self.width = None
        self.height = None
        self.image = None
        self.img_path = img_path
        self.readImage(img_path)
        self.showImage()
        self.distanceParameter = 119.63
        for i in range(0, superpixel_quantity):
            self.mergeVertices()

    def readImage(self, img_path):
        self.image = cv2.imread(img_path)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.height, self.width, colorChannelNumber = self.image.shape

        for x in range(0, self.height):
            for y in range(0, self.width):

                current_vertex = Vertex(Key(x, y))
                current_vertex.value = self.image[x][y]
                self.addVertex(current_vertex)

                if (x - 1) >= 0:
                    self.addPrevious(self.vertices.__getitem__(self.vertices.index(current_vertex)), x - 1, y)

                if self.height - 1 >= (x + 1):
                    self.addPrevious(self.vertices.__getitem__(self.vertices.index(current_vertex)), x + 1, y)

                if self.width - 1 >= (y + 1):
                    self.addPrevious(self.vertices.__getitem__(self.vertices.index(current_vertex)), x, y + 1)

                if (y - 1) >= 0:
                    self.addPrevious(self.vertices.__getitem__(self.vertices.index(current_vertex)), x, y - 1)



    def addPrevious(self, vertex, previous_vertex_index_x, previous_vertex_index_y):
        previous_vertex = Vertex(Key(previous_vertex_index_x, previous_vertex_index_y))
        self.addVertex(previous_vertex)
        previous_vertex = self.vertices.__getitem__(self.vertices.index(previous_vertex))
        previous_vertex.value = self.image[previous_vertex_index_x][previous_vertex_index_y]
        vertex.listPreviousVertices.append(previous_vertex)

    def addVertex(self, vertex):
        if not self.vertices.__contains__(vertex):
            self.vertices.append(vertex)

    def mergeVertices(self):
        nearest_neighbor_quantity = 1
        neighbor_relationship_values = []
        neighbor_relationship = []

        for vertex in self.vertices:
            neighbor_relationship_values.append(vertex.value)
            merged_neighbor_array_result = np.array(vertex.value)
            for neighbor in vertex.listPreviousVertices:
                if np.linalg.norm(vertex.value - neighbor.value) <= self.distanceParameter:
                    neighbor_relationship.append(neighbor)
                    neighbor_relationship_values.append(neighbor.value)
                    merged_neighbor_array_result = [int(merged_neighbor_array_result[0]) + int(neighbor.value[0]),int(merged_neighbor_array_result[1]) + int(neighbor.value[1]), int(merged_neighbor_array_result[2] + neighbor.value[2])]
                    nearest_neighbor_quantity = nearest_neighbor_quantity + 1

            merged_neighbor_array_result = np.array(merged_neighbor_array_result) / nearest_neighbor_quantity

            vertex.value = merged_neighbor_array_result

            for neighbor in neighbor_relationship:
                neighbor.value = merged_neighbor_array_result

            nearest_neighbor_quantity = 1
            neighbor_relationship_values.clear()
            neighbor_relationship.clear()

    def showImageWithSuperpixels(self):
        for vertex in self.vertices:
            self.image[vertex.key.height, vertex.key.width] = vertex.value

        plt.imshow(self.image)
        plt.show()

    def showImage(self):
        plt.imshow(self.image)
        plt.show()
