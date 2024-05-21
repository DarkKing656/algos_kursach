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

# Пример использования
graph = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

result = floyd_warshall(graph)

print("Матрица кратчайших расстояний:")
for row in result:
    print(row)