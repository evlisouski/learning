# region МАТРИЦЫ СМЕЖНОСТИ
# Матрица смежности для не ориентированного графа
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
]

print(*graph, sep='\n')
print('*' * 50)

# Матрица смежности для ориентированного графа.
# Отсутствие симемтрии относительно нисходящей диагонали
# из левого верхнего угла говорит о том что матрица смежности
# для ориентированного графа
graph = [
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
]

print(*graph, sep='\n')
print('*' * 50)

# Для взвешенного графа нужно заменить 1 на значения весов соответствующих ребер
graph[0][1:3] = [2, 3]
graph[1][2] = 2
graph[2][1] = 2

print(*graph, sep='\n')
print('*' * 50)
# endregion

# region СПИСКИ СМЕЖНОСТИ
graph = []

graph.append([1, 2])
graph.append([0, 2, 3])
graph.append([0, 1])
graph.append([1])

print(*graph, sep='\n')

# Списки смежности на основе словарей и множеств работают гораздо быстрее чем на основании списков
graph_2 = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1},
    3: {1},
}

print(graph_2)

# Пример проверки возможности перехода из вершины 1 в вершину 3
if 3 in graph_2[1]:
    print(True)
print('*' * 50)

# Список смежности с весовыми коэффициентами
from collections import namedtuple

Vertex = namedtuple("vertex", ['vertex', "edge"])
graph_3 = []

graph_3.append([Vertex(1, 2), Vertex(2, 3)])
graph_3.append([Vertex(0, 2), Vertex(2, 2), Vertex(3, 1)])
graph_3.append([Vertex(0, 3), Vertex(1, 2)])
graph_3.append([Vertex(1, 1)])

print(*graph_3, sep='\n')

for v in graph_3[1]:  # проверка возможности перехода из вершины 1 в вершину 3
    if v.vertex == 3:
        print(True)


class Graph:
    def __init__(self, vertex, edge, spam):
        self.vertex = vertex
        self.edge = edge
        self.spam = spam

# endregion

#region СПИСОК РЕБЕР
graph = [(0, 1), (0, 2), ()]
#endregion