import tkinter as tk
import requests

def get_graph():
    graph = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(int(entries[i][j].get()))
        graph.append(row)
    return graph

BASE_URL = "http://localhost:8000"  

def submit_graph():
    global graph
    graph = get_graph()
    response = requests.post(f"{BASE_URL}/shortest_paths", json=graph)
    result = response.json()
    display_result(result)


def display_result(result):
    # Создайте новое окно или виджет для вывода результата
    result_window = tk.Toplevel(root)
    result_window.title("Shortest Paths")

    # Выведите результат в новом окне
    for i in range(len(result)):
        for j in range(len(result[i])):
            if i != j:
                path_label = tk.Label(result_window, text=f"Shortest path from {i+1} to {j+1}: {result[i][j]}")
                path_label.pack()



root = tk.Tk()
root.title("Graph Input")

# Создаем сетку для ввода графа
entries = []
for i in range(4):
    row = []
    for j in range(4):
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=j)
        row.append(entry)
    entries.append(row)

# Заполняем изначальный граф
for i in range(4):
    for j in range(4):
        if i == j:
            entries[i][j].insert(0, "0")
        else:
            entries[i][j].insert(0, "1000000")

# Добавляем кнопку для отправки графа
submit_button = tk.Button(root, text="Submit Graph", command=submit_graph)
submit_button.grid(row=4, column=0, columnspan=4)

root.mainloop()
