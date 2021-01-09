# Написать программу, которая обходит не взвешенный ориентированный
# граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания: a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import collections

vertex_num = int(input('Введите количество вершин графа: '))
visited_list = []


def generation_graph(vertex_num):
    ex_graph = collections.defaultdict(list)
    for i in range(vertex_num):
        for j in range(vertex_num):
            if j != i:
                ex_graph[i].append(j)
    return ex_graph


def depth_first_search(graph, node):
    if node not in visited_list:
        visited_list.append(node)
        for n in graph[node]:
            depth_first_search(graph, n)


ex_graph = generation_graph(vertex_num)
print('Граф: {0}'.format(ex_graph))
depth_first_search(ex_graph, 2)
print(visited_list)