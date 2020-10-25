# Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.


def dijkstra(start, my_graph):
    len_graph = len(my_graph)
    visited_list = [False] * len_graph
    cost_list = [float('inf')] * len_graph
    parent = [-1] * len_graph

    cost_list[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        visited_list[start] = True
        for i, vertex in enumerate(my_graph[start]):
            if vertex != 0 and not visited_list[i]:
                if cost_list[i] > vertex + cost_list[start]:
                    cost_list[i] = vertex + cost_list[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(len_graph):
            if min_cost > cost_list[i] and not visited_list[i]:
                min_cost = cost_list[i]
                start = i

    return cost_list


ex_graph = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

ex_vertex = int(input('Введите номер необходимой вершины: '))
print(dijkstra(ex_vertex, ex_graph))