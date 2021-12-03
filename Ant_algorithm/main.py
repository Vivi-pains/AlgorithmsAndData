from Generate_graph import *
from antAlgorithm import *
from test_graph import *

L_min = 5000
list_answers = []

alg = Algorithm(graph, 150)
l = alg.send_ants([1.6, 0.1, 0.82], 1593)



"""
for a in range(1, 40, 3):
    for b in range(1, 40, 3):
        for p in range(1, 100, 3):
            l_min = []
            for i in range(0, 3):
                alg = Algorithm(graph, 200)
                L_min = alg.send_ants([a/10, b/10, p/100], 5000)
                if L_min == None: L_min = 5000
                l_min.append(L_min)
                L_min = 5000

            if min(l_min) <= 1000:
                list_answers.append([[a/10, b/10, p/100, l_min[0], l_min[1], l_min[2]]])
            print([[a/10, b/10, p/100, l_min[0], l_min[1], l_min[2]]])

list_answers.sort(key=lambda x: (x[0] + x[1] + x[2]) / 3)
[print(x) for x in list_answers]


[[0.7, 0.1, 0.76, 516, 302, 636]]
[[0.7, 0.7, 0.28, 337, 689, 538]]
[[1.0, 0.1, 0.07, 911, 384, 271]]
[[1.0, 0.1, 0.52, 596, 360, 752]]
[[1.0, 0.4, 0.73, 756, 384, 554]]
[[1.6, 0.1, 0.82, 425, 323, 370]]
[[2.2, 0.1, 0.4, 302, 323, 271]]
[[2.5, 0.4, 0.85, 304, 384, 299]]
[[3.4, 0.1, 0.01, 360, 370, 485]]
[[3.7, 0.1, 0.37, 384, 309, 261]]
[[1.9, 1.0, 0.79, 261, 271, 536]]
[[2.2, 0.1, 0.7, 535, 261, 269]]
[[2.8, 0.7, 0.67, 261, 261, 438]]
[[3.1, 0.4, 0.94, 370, 299, 269]]
"""


