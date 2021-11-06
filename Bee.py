#from typing import Deque
from GrafVertex import *
import random
from collections import deque

listOfVertex = []
listOfSeenVertex = []

class EmployedBee:
    def __init__(self) -> None:
        self.stack = deque()

    def SendEmployedBee(self, graph, iteration):
        vertex = self.stack.pop()

        if vertex.iter < iteration:
            vertex.nectarAmount = vertex.color + vertex.degree / graph.maxDegree

            if not graph.listOfUsedColors.__contains__(vertex.color):
                graph.listOfUsedColors.append(vertex.color)

            #print('  '.join([str(vertex.name), str(vertex.color), str(vertex.degree), str(vertex.nectarAmount)]))
            for x in vertex.connections:
                self.stack.append(x)

            vertex.iter = iteration

class Forager():
    def __init__(self, vertex) -> None:
        self.vertex = vertex

    def SendForager(self, neighbor, usedColors):

        colorsNeighbor = list([x.color for x in neighbor.connections])
        colorsNeighbor.remove(self.vertex.color)
        colorsNeighbor = list(set(list(colorsNeighbor)))

        colorsVertex = [x.color for x in self.vertex.connections]
        colorsVertex.remove(neighbor.color)
        colorsVertex = list(set(colorsVertex))

        ChangeColor1 = colorsNeighbor.__contains__(self.vertex.color)
        ChangeColor2 = colorsVertex.__contains__(neighbor.color)

        if not ChangeColor1 and not ChangeColor2:
            for i in usedColors:
                bool1 = not colorsNeighbor.__contains__(i)
                
                if i != self.vertex.color and i != neighbor.color and bool1:
                    print("Change {0} from {1} to {2}".format(self.vertex.name, self.vertex.color, neighbor.color))
                    print("Change {0} from {1} to {2}".format(neighbor.name, neighbor.color, i))
                    self.vertex.color = neighbor.color
                    neighbor.color = i
                    break
        return self.vertex


    def SendScouts(self):
        pass
