import copy
import random
from math import pow


class Ant:
    def __init__(self, ant_id, matrix_pheromones, matrix_vay, constants, l_min, fist_vertex=0, last_vertex=200):
        self.id = ant_id
        self.tabu_list = []
        self.fist_vertex = fist_vertex
        self.last_vertex = last_vertex
        self.alfa = constants[0]
        self.beta = constants[1]
        self.p = constants[2]
        self.l_min = l_min
        self.matrix_pheromones = matrix_pheromones
        self.matrix_vay = matrix_vay

    def search_vay(self):

        vertex = self.fist_vertex

        matrix_num = len(self.matrix_vay)

        while len(self.tabu_list) < matrix_num:

            self.tabu_list.append(vertex)

            probabilities = self.probability(vertex)

            if sum(probabilities) == 0:
                return

            sum_probabilities = sum(probabilities)

            probabilities = [x/sum_probabilities for x in probabilities]

            vertex = random.choices(range(0, matrix_num), weights=probabilities)[0]

            if vertex == self.last_vertex:
                self.tabu_list.append(vertex)
                self.update_matrix_pheromones()
                # print(self.tabu_list)
                return self.l_min
        return self.l_min

    def probability(self, current_vertex):

        next_vertexes = self.matrix_vay[current_vertex]
        probabilities = []

        for el in self.tabu_list:
            next_vertexes[el] = 0

        for el in range(0, len(next_vertexes)):
            p = pow(self.matrix_pheromones[current_vertex][el], self.alfa)
            p = p * pow(self.matrix_vay[current_vertex][el], self.beta)
            probabilities.append(p)

        return probabilities

    def update_matrix_pheromones(self):
        l_vay = 0

        for i in range(0, len(self.tabu_list)-1):
            l_vay += self.matrix_vay[self.tabu_list[i]][self.tabu_list[i+1]]

        if l_vay < self.l_min:
            self.l_min = l_vay

        for i in range(0, len(self.tabu_list)-1):
            tau = self.matrix_pheromones[self.tabu_list[i]][self.tabu_list[i+1]]
            self.matrix_pheromones[self.tabu_list[i]][self.tabu_list[i + 1]] = tau * (1 - self.p) + l_vay / self.l_min


class Algorithm:
    def __init__(self, graph, ant_num):
        self.matrix_vay = graph
        self.matrix_pheromones = self.calculate_matrix_pheromones()
        self.ant_num = ant_num
        self.l_min = 0

    def calculate_matrix_pheromones(self):
        matrix_pheromones = copy.deepcopy(self.matrix_vay)

        for line in range(len(matrix_pheromones)):
            for el in range(len(matrix_pheromones[line])):
                if matrix_pheromones[line][el] != 0:
                    matrix_pheromones[line][el] = 0.1

        # [print(line) for line in matrix_pheromones]

        return matrix_pheromones

    def send_ants(self, constants, l_min):
        self.l_min = l_min
        for ant in [Ant(i, self.matrix_pheromones, self.matrix_vay, constants, self.l_min) for i in range(0, self.ant_num)]:
            self.l_min = ant.search_vay()

        print('Vay =', end=' ')
        print(self.l_min)

        return self.l_min
