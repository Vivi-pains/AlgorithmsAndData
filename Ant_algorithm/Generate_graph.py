import random


class GraphVay:
    def __init__(self) -> None:
        self.num_of_nodes = 300
        self.max_degree = 10
        self.graph_matrix = self.empty_graph()
        self.degrees = [0 for _ in range(0, self.num_of_nodes)]

        self.create_table()

    def create_table(self):
        print('Creating graph...')
        # self.vertexes = [copy.deepcopy(GraphVertex(x)) for x in range(0, self.numOfNodes)]]

        for i in range(0, self.num_of_nodes):

            for j in range(i + 1, self.num_of_nodes):
                deg = self.degrees[i]
                if deg < self.max_degree:
                    print(self.degrees[i])
                    vay = random.randint(0, 20)
                    if vay == 1:
                        ran = random.randint(5, 150)
                        self.graph_matrix[i][j] = ran
                        self.graph_matrix[j][i] = ran
                        self.degrees[i] += 1
                        self.degrees[j] += 1

        print('Graph created')

        for i in range(0, len(self.graph_matrix)):
            print(self.graph_matrix[i], end=', ')
            # print(self.degrees[i])

    def empty_graph(self):
        table_graph = [[0 for _ in range(0, self.num_of_nodes)] for _ in range(0, self.num_of_nodes)]

        return table_graph


