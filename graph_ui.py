import tkinter as tk
import requests

BASE_URL = "http://localhost:8000"

MAX_ROWS = 10
MAX_COLUMNS = 10
MIN_ROWS = 2
MIN_COLUMNS = 2

def get_graph():
    graph = []
    for row in graph_entries:
        row_values = [int(entry.get()) for entry in row]
        graph.append(row_values)
    return graph

def add_row():
    global graph_entries
    if len(graph_entries) < MAX_ROWS:
        row = [tk.Entry(entries_frame, width=3) for _ in range(len(graph_entries[0]))]
        for i, entry in enumerate(row):
            entry.grid(row=len(graph_entries), column=i)
        graph_entries.append(row)

def add_column():
    global graph_entries
    if len(graph_entries[0]) < MAX_COLUMNS:
        for row in graph_entries:
            entry = tk.Entry(entries_frame, width=3)
            entry.grid(row=row[0].grid_info()['row'], column=len(row))
            row.append(entry)

def remove_row():
    global graph_entries
    if len(graph_entries) > MIN_ROWS:
        row_to_remove = graph_entries.pop()
        for entry in row_to_remove:
            entry.grid_forget()

def remove_column():
    global graph_entries
    if len(graph_entries[0]) > MIN_COLUMNS:
        for row in graph_entries:
            row[-1].grid_forget()
            row.pop()

def submit_graph():
    global graph
    graph = get_graph()
    response = requests.post(f"{BASE_URL}/shortest_paths", json=graph)
    result = response.json()
    display_result(result)

def display_result(result):
    result_window = tk.Toplevel(root)
    result_window.title("Shortest Paths")

    for i in range(len(result)):
        for j in range(len(result[i])):
            if i != j:
                path_label = tk.Label(result_window, text=f"Shortest path from {i+1} to {j+1}: {result[i][j]}")
                path_label.pack()

root = tk.Tk()
root.title("Graph UI")
root.resizable(False, False)

# Create frames
button_frame = tk.Frame(root)
button_frame.grid(row=0, column=0, columnspan=5)

entries_frame = tk.Frame(root)
entries_frame.grid(row=1, column=0, columnspan=2)

# Create initial 2x2 matrix
graph_entries = [[tk.Entry(entries_frame, width=3) for _ in range(2)] for _ in range(2)]
for i, row in enumerate(graph_entries):
    for j, entry in enumerate(row):
        entry.grid(row=i, column=j)

add_row_button = tk.Button(button_frame, text="Add Row", command=add_row)
add_row_button.grid(row=0, column=0)

add_col_button = tk.Button(button_frame, text="Add Column", command=add_column)
add_col_button.grid(row=0, column=1)

remove_row_button = tk.Button(button_frame, text="Remove Row", command=remove_row)
remove_row_button.grid(row=0, column=2)

remove_col_button = tk.Button(button_frame, text="Remove Column", command=remove_column)
remove_col_button.grid(row=0, column=3)

submit_button = tk.Button(button_frame, text="Submit Graph", command=submit_graph)
submit_button.grid(row=0, column=4)

root.mainloop()
