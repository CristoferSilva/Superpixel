import Key as Key
import numpy as np

def Vertex():
    return Vertex();

class Vertex:
     Key = Key();
     distance = 0;
     color =  np.array([0,0,0]); # 0 = WHITE; 1 = BLACK ; 2 = GRAY
     listPreviousVertices = [Vertex()];

     def __init__(self, key, color):
        self.key = key
        self.color = color

     def getPreviousVerticeWithShortestDistance(self):
         if(self.listPreviousVertices.count() == 0):
            return None;
         verticeKeyWithShortestDistance = self.listPreviousVertices[0].distance;
         currentdistance = 0;
         verticeWithShortestDistance = self;

         for currentVertex in self.listPreviousVertices:

             currentdistance = currentVertex.distance;

             if(currentdistance < verticeKeyWithShortestDistance):
                 verticeKeyWithShortestDistance = currentdistance;
                 verticeWithShortestDistance = currentdistance

         return verticeWithShortestDistance;

     def __str__(self):
         return f"{self.key}<-)"

     def __eq__(self, other):
         if isinstance(other,self):
             return other.key == self.key