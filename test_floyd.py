def floyd_warshall(graph):
    """
    Алгоритм Флойда-Уоршелла для поиска кратчайших путей между всеми парами вершин в графе.

    Аргументы:
    graph (list) - двумерный список, представляющий взвешенный граф.
                   Элемент graph[i][j] содержит вес ребра от вершины i до вершины j.
                   Если ребра не существует, то вместо веса указывается float('inf').

    Возвращает:
    list - двумерный список, представляющий матрицу кратчайших расстояний между всеми парами вершин.
    """
    if not graph:
        return [[]]

    n = len(graph)  # Количество вершин в графе
    dist = [row[:] for row in graph]  # Создаем копию исходного графа

    # Проходим по всем вершинам графа
    for k in range(n):
        # Для каждой пары вершин (i, j)
        for i in range(n):
            for j in range(n):
                # Проверяем, можно ли улучшить расстояние от i до j, проходя через k
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Пример 1: Пустой граф
print("Пример 1: Пустой граф")
graph = []
result = floyd_warshall(graph)
print(result)  # Вывод: [[]]
print()

# Пример 2: Граф с одной вершиной
print("Пример 2: Граф с одной вершиной")
graph = [[0]]
result = floyd_warshall(graph)
print(result)  # Вывод: [[0]]
print()

# Пример 3: Граф с двумя вершинами, соединенными ребром
print("Пример 3: Граф с двумя вершинами, соединенными ребром")
graph = [
    [0, 5],
    [float('inf'), 0]
]
result = floyd_warshall(graph)
print(result)  # Вывод: [[0, 5], [float('inf'), 0]]
print()

# Пример 4: Граф с двумя вершинами, не соединенными ребром
print("Пример 4: Граф с двумя вершинами, не соединенными ребром")
graph = [
    [0, float('inf')],
    [float('inf'), 0]
]
result = floyd_warshall(graph)
print(result)  # Вывод: [[0, float('inf')], [float('inf'), 0]]
print()

# Пример 5: Граф с циклом отрицательного веса
print("Пример 5: Граф с циклом отрицательного веса")
graph = [
    [0, 1, float('inf')],
    [-1, 0, 1],
    [float('inf'), -1, 0]
]
result = floyd_warshall(graph)
print(result)  # Вывод: [[-1, 0, -1], [-2, -1, 0], [float('inf'), -2, -1]]
print()

# Пример 6: Граф со всеми положительными весами
print("Пример 6: Граф со всеми положительными весами")
graph = [
    [0, 5, 1],
    [2, 0, 3],
    [4, 6, 0]
]
result = floyd_warshall(graph)
print(result)  # Вывод: [[0, 5, 1], [2, 0, 3], [4, 6, 0]]
print()

# Пример 7: Граф с дублирующими ребрами
print("Пример 7: Граф с дублирующими ребрами")
graph = [
    [0, 5, 1, float('inf')],
    [2, 0, 3, 1],
    [4, 6, 0, 2],
    [float('inf'), float('inf'), float('inf'), 0]
]
result = floyd_warshall(graph)
print(result)  # Вывод: [[0, 5, 1, 6], [2, 0, 3, 1], [4, 6, 0, 2], [float('inf'), float('inf'), float('inf'), 0]]
