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

    def __init__(self, height, width, imgPath):
        self.height = height
        self.width = width
        self.imgPath = imgPath

    def readImage(self):

        currentImage = cv2.imread("images/car.jpg")
        currentImage = cv2.cvtColor(currentImage, cv2.COLOR_BGR2RGB)
        height, width, colorChannelNumber = currentImage.shape

        for x in range(0, self.height):
            for y in range(0, self.width):

                currentVertex = Vertex(Key(x, y), 0)
                currentVertex.value = currentImage[x][y]

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
        self.AddInVerticesList(previousVertex)
        previousVertex = self.vertices.__getitem__(self.vertices.index(previousVertex))
        previousVertex.value = image[previousVertex_Index_X][previousVertex_Index_X]
        vertex.listPreviousVertices.__add__(previousVertex)

    def addInVerticesList(self, vertex):
        if not self.vertices.__contains__(vertex):
            self.vertices.__add__(vertex)
