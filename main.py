from Bee import *
from BeesAlgorithm import *
from GrafVertex import *


iterations = 0
graph = Graph()
graph.PaintGraph()
bees = Bees()
print(max(graph.vertexes, key=lambda x: x.color).color)

while(iterations < 100):
    iterations += 1

    bees.SendEmployedBees(graph, iterations)
    bees.SendForagers(graph)
    print(max(graph.vertexes, key=lambda x: x.color).color)
    #input()
