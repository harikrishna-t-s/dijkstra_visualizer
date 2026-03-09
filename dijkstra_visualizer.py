import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import heapq
import time

# -----------------------------
# Graph Data
# -----------------------------
G = nx.Graph()
positions = {}

# -----------------------------
# Dijkstra Algorithm
# -----------------------------
def dijkstra(graph, start, update_callback):

    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0

    pq = [(0, start)]
    visited = set()

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        update_callback(current_node, visited)

        for neighbor in graph.neighbors(current_node):

            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

        time.sleep(1)

    return distances


# -----------------------------
# Draw Graph
# -----------------------------
def draw_graph(highlight=None):

    ax.clear()

    colors = []

    for node in G.nodes():
        if highlight and node in highlight:
            colors.append("gray")
        else:
            colors.append("white")

    nx.draw(
        G,
        positions,
        with_labels=True,
        node_color=colors,
        edge_color="black",
        node_size=1500,
        font_color="black",
        ax=ax
    )

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, positions, edge_labels=labels)

    canvas.draw()


# -----------------------------
# Add Edge
# -----------------------------
def add_edge():

    u = node1_entry.get()
    v = node2_entry.get()
    w = weight_entry.get()

    if not u or not v or not w:
        messagebox.showerror("Error", "Enter node1, node2 and weight")
        return

    w = int(w)

    G.add_edge(u, v, weight=w)

    global positions
    positions = nx.spring_layout(G)

    draw_graph()

    node1_entry.delete(0, tk.END)
    node2_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)


# -----------------------------
# Run Algorithm
# -----------------------------
def run_dijkstra():

    start = start_entry.get()

    if start not in G.nodes():
        messagebox.showerror("Error", "Start node not found")
        return

    def update(node, visited):

        draw_graph(visited)
        root.update()

    distances = dijkstra(G, start, update)

    result = "\n".join([f"{node} : {dist}" for node, dist in distances.items()])

    messagebox.showinfo("Shortest Paths", result)


# -----------------------------
# UI
# -----------------------------
root = tk.Tk()
root.title("Dijkstra Graph Visualizer")
root.configure(bg="white")

# Controls Frame
controls = tk.Frame(root, bg="white")
controls.pack(pady=10)

tk.Label(controls, text="Node 1", bg="white").grid(row=0, column=0)
node1_entry = tk.Entry(controls)
node1_entry.grid(row=0, column=1)

tk.Label(controls, text="Node 2", bg="white").grid(row=1, column=0)
node2_entry = tk.Entry(controls)
node2_entry.grid(row=1, column=1)

tk.Label(controls, text="Weight", bg="white").grid(row=2, column=0)
weight_entry = tk.Entry(controls)
weight_entry.grid(row=2, column=1)

add_button = tk.Button(
    controls,
    text="Add Edge",
    command=add_edge,
    bg="black",
    fg="white"
)
add_button.grid(row=3, columnspan=2, pady=5)

tk.Label(controls, text="Start Node", bg="white").grid(row=4, column=0)
start_entry = tk.Entry(controls)
start_entry.grid(row=4, column=1)

run_button = tk.Button(
    controls,
    text="Execute Dijkstra",
    command=run_dijkstra,
    bg="black",
    fg="white"
)
run_button.grid(row=5, columnspan=2, pady=10)

# Graph Display
fig, ax = plt.subplots(figsize=(5,5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
