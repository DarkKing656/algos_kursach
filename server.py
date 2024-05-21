from fastapi import FastAPI
from typing import List

app = FastAPI()

# Функция алгоритма Флойда
def floyd_warshall(graph: List[List[float]]) -> List[List[float]]:
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Эндпоинт для поиска кратчайших путей
@app.post("/shortest_paths")
def get_shortest_paths(graph: List[List[int]]):
    # Ваша логика для вычисления кратчайших путей
    

    """
    Принимает матрицу графа в виде списка списков и возвращает
    матрицу кратчайших расстояний между всеми парами вершин.
    """
    return floyd_warshall(graph)
