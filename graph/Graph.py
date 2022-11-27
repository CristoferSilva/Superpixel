import numpy as np
import cv2
from matplotlib import pyplot as plt
from graph.Key import Key
from graph.Vertex import Vertex

class Graph:
    height = 0
    width = 0
    vertices = []
    imgPath = ""
    image = []
    distanceParameter = 119.63

    def __init__(self, height, width, imgPath, superPixelQuantity):
        self.height = height
        self.width = width
        self.imgPath = imgPath
        self.readImage(imgPath)

        while(superPixelQuantity):
            self.mergeVertices()

    def readImage(self, imgPath):

        currentImage = cv2.imread(imgPath)
        currentImage = cv2.cvtColor(currentImage, cv2.COLOR_BGR2RGB)
        self.image = currentImage
        height, width, colorChannelNumber = currentImage.shape

        for x in range(0, self.height):
            for y in range(0, self.width):

                currentVertex = Vertex(Key(x, y), 0)
                currentVertex.value = currentImage[x][y]
                self.addVertex(currentVertex)

                if x - 1 >= 0:
                    self.addPrevious(currentVertex, x - 1, y, currentImage)

                if x + 1 >= 0:
                    self.addPrevious(currentVertex, x + 1, y, currentImage)

                if y + 1 >= 0:
                    self.addPrevious(currentVertex, y + 1, y, currentImage)

                if y - 1 >= 0:
                    self.addPrevious(currentVertex, y - 1, y, currentImage)

    def addPrevious(self, vertex, previousVertex_Index_X, previousVertex_Index_Y, image):
        previousVertex = Vertex(Key(previousVertex_Index_X, previousVertex_Index_Y), 0)
        self.addVertex(previousVertex)
        previousVertex = self.vertices.__getitem__(self.vertices.index(previousVertex))
        previousVertex.value = image[previousVertex_Index_X][previousVertex_Index_X]
        vertex.listPreviousVertices.__add__(previousVertex)

    def addVertex(self, vertex):
        if not self.vertices.__contains__(vertex):
            self.vertices.__add__(vertex)

    def mergeVertices(self):
        nearestNeighborQuantity = 1;
        neighborRelationShipValues = [];
        neighborRelationShip = [];

        for vertex in self.vertices:
            neighborRelationShipValues.__add__(vertex.value)
            arrayMergeNeighborResult = vertex.value;
            for neighbor in vertex.listPreviousVertices:
               if np.linalg.norm(vertex - neighbor) < self.distanceParameter:
                   neighborRelationShip.__add__(neighbor)
                   neighborRelationShipValues.__add__(neighbor.value)
                   arrayMergeNeighborResult = arrayMergeNeighborResult + neighbor.value
                   nearestNeighborQuantity = nearestNeighborQuantity + 1;

            arrayMergeNeighborResult = arrayMergeNeighborResult/nearestNeighborQuantity

            vertex.value = arrayMergeNeighborResult

            for neighbor in neighborRelationShip:
                neighbor.value = arrayMergeNeighborResult

            nearestNeighborQuantity = 1;
            neighborRelationShipValues = [];
            neighborRelationShip = [];

    def showImageWithSuperpixels(self):
        for vertex in self.vertices:
            self.image[vertex.key.height, vertex.key.width] = vertex.value

        plt.imshow(self.image)
        plt.show()








