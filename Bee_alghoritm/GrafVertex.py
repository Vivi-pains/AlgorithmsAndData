import random
import copy

class Graph:
    def __init__(self) -> None:
        self.vertexes = []
        self.listOfColors = list(range(31))
        self.listOfUsedColors = []
        self.numOfNodes = 200
        self.GenereteGraph()
        self.maxDegree = self.CountMax()
        

    def add(self):
        a = GraphVertex('a', 1)
        b = GraphVertex('b', 2, [a])
        c = GraphVertex('c', 2, [a])
        d = GraphVertex('d', 1, [b])
        e = GraphVertex('e', 2, [d])
        f = GraphVertex('f', 3, [c, d, e])
        g = GraphVertex('g', 1, [e, f])
        h = GraphVertex('h', 2, [g])
        i = GraphVertex('i', 3, [e, g, h])
        j = GraphVertex('j', 4, [a, b, c, e, i])
        [self.vertexes.append(x) for x in [a, b, c, d, e, f , g, h, i, j]]

    def CountMax(self):
        return max([x.degree for x in self.vertexes])

    def Print(self):
        for el in self.vertexes:
            print('  '.join([str(el.name), str(el.color), str(el.degree), ]), end='   ')
            print([x.name for x in el.connections])

    def GenereteGraph(self):
        print('Creating graph...')
        tableGraph = [[ 0 for x in range(0, self.numOfNodes)] for x in range(0, self.numOfNodes)]
        self.vertexes = [copy.deepcopy(GraphVertex(x)) for x in range(0, self.numOfNodes)]
        for i in range(0, self.numOfNodes):
            for j in range(i + 1, self.numOfNodes):
                if self.vertexes[i].degree < 45:
                    vay = random.randint(0, 2)
                    if vay == 1:
                        tableGraph[i][j] = vay
                        tableGraph[j][i] = vay
                        self.vertexes[i].connections.append(self.vertexes[j])
                        self.vertexes[i].degree += 1
                        self.vertexes[j].connections.append(self.vertexes[i])
                        self.vertexes[j].degree += 1
        print('Graph created')
        #for i in tableGraph:
        #    print(i)

    def PaintGraph(self):
        # Consider nodes in descending degree 
        for node in self.vertexes:
            
            for color in self.listOfColors:
                if not [x.color for x in node.connections].__contains__(color):
                    node.color = color
                    break
            #print(node.color)




class GraphVertex:
    def __init__(self, name, color = 0, connections = []) -> None:
        self.name = name
        self.color = color
        self.connections = connections
        self.degree = len(self.connections)
        self.Connect()
        self.nectarAmount = None
        self.iter = 0

    def Connect(self):
        for el in self.connections:
            el.connections.append(self)
            el.degree += 1

    def AddConnection(self, node):
        self.connections.append(node)
        self.degree += 1
        node.connections.append(self)
        node.degree += 1

    def PaintNode(self, color):
        self.color = color

    def CalculateNectar(self, sumNectar):
        self.nectarAmount = self.degree / sumNectar


#random_graf = Graph()
#random_graf.Print()
#random_graf.PaintGraph()
#random_graf.Print()
