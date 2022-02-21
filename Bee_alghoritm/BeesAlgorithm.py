from Bee import *
from GrafVertex import *
import random
import copy

class Bees:
    def __init__(self) -> None:
        self.employedBees = []
        self.foragers = []
        self.listOfSeenVertex = []
        self.numOfEmployedBees = 2
        self.numOfForagers = 38

    def CreateEmployedBees(self, num):
        for i in range(0, num):
            self.employedBees.append(EmployedBee())

    def SendEmployedBees(self, graph, iteration):

        graph.listOfUsedColors = []

        self.CreateEmployedBees(self.numOfEmployedBees)
        
        for bee in self.employedBees:
            vertex = random.choice(graph.vertexes)
            bee.stack.append(vertex)

        while(True):
            for bee in self.employedBees:
                if bee.stack:
                    bee.SendEmployedBee(graph, iteration)
                else:
                    self.employedBees.remove(bee)
            if not self.employedBees:
                break
        graph.vertexes.sort(key=lambda x: x.nectarAmount)
        graph.vertexes.reverse()
        #print(graph.vertexes)
        #print([str(i.name) + ' ' + str(i.nectarAmount) for i in graph.vertexes])

        graph.listOfUsedColors.sort()
        #print(graph.listOfUsedColors)

    def SendForagers(self, graph):
        bees = self.numOfForagers
        koef = 2
        for el in graph.vertexes:
            neighborhood = copy.copy(el.connections)
            n_bees = round(el.degree * (1 - koef / 10))
            koef -= 1

            if bees - n_bees < 0:
                n_bees = bees
            #print(n_bees)

            for i in range(0, n_bees):
                vertex = random.choice(neighborhood)
                el = Forager(el).SendForager(vertex, graph.listOfUsedColors)
                neighborhood.remove(vertex)

            bees = bees - n_bees
            if bees <= 0:
                break
