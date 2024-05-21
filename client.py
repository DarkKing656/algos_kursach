import requests
from typing import List
from graph_ui import get_graph

def get_shortest_paths(graph: List[List[float]]) -> List[List[float]]:
    """
    Отправляет матрицу графа на сервер и возвращает
    матрицу кратчайших расстояний между всеми парами вершин.
    """
    url = "http://localhost:8000/shortest_paths"
    response = requests.post("/shortest_paths", json=graph)
    return response.json()

# Пример использования
graph = get_graph()
shortest_paths = get_shortest_paths(graph)



result = get_shortest_paths(graph)
print("Матрица кратчайших расстояний:")
for row in result:
    print(row)
