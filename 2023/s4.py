from collections import defaultdict
import tkinter as tk
import math

class Graph:
    def __init__(self):
        self.adjs = defaultdict(list) #src : dst, length, cost

graph = Graph()

dimensions = input().split(" ")
for x in range(int(dimensions[1])):
    inp = input().split(" ")
    graph.adjs[int(inp[0]) - 1].append([int(inp[1]) - 1, int(inp[2]), int(inp[3])])
    graph.adjs[int(inp[1]) - 1].append([int(inp[0]) - 1, int(inp[2]), int(inp[3])])

interNum = int(dimensions[0])

newAdjList = defaultdict(list)
visited = [False] * interNum

currentNode = 0
visited[0] = True
dist = 0
path = []
while False in visited:
    print(str(visited))
    bestEdge = [None, None, float("inf")]
    for adj in graph.adjs[currentNode]:
        if visited[adj[0]]:
            continue
        if adj[2] < bestEdge[2]:
            bestEdge = adj
    if bestEdge == [None, None, float("inf")]:
        try:
            currentNode = path.pop()
        except IndexError:
            if not False in visited:
                break
            else:
                continue

        dist -= newAdjList[currentNode].pop()[-1]
        continue
    newAdjList[currentNode].append(bestEdge)
    dist += bestEdge[1]
    newAdjList[bestEdge[0]].append([currentNode, bestEdge[1], bestEdge[2]])
    visited[bestEdge[0]] = True
    path.append(bestEdge[0])
    currentNode = bestEdge[0]




def display_graph(newAdjList, visited):
    # Create a window for the GUI
    window = tk.Tk()
    window.title("Graph")

    # Create a canvas to draw the nodes and edges
    canvas = tk.Canvas(window, width=500, height=500)
    canvas.pack()

    canvas.create_text(250, 25, text="ALL NODES ARE 1 LESS ON GRAPH THAN IN INPUT")

    # Calculate the number of nodes and the radius of the circle that will contain them
    num_nodes = len(newAdjList)
    radius = min(200, (500 / 2) * 0.8)

    # Calculate the coordinates of each node on the circle
    node_coords = []
    for i in range(num_nodes):
        angle = i * (2 * math.pi / num_nodes)
        x = 250 + radius * math.cos(angle)
        y = 250 + radius * math.sin(angle)
        node_coords.append((x, y))

    # Draw the nodes and their labels
    nodes = {}
    for i, node in enumerate(newAdjList):
        x, y = node_coords[i]
        nodes[node] = canvas.create_oval(x-10, y-10, x+10, y+10, fill="white", outline="black")
        canvas.create_text(x, y, text=str(node))

    # Draw the edges between the nodes
    for node, edges in newAdjList.items():
        for edge in edges:
            if visited[node] and visited[edge[0]]:
                x1, y1 = node_coords[node]
                x2, y2 = node_coords[edge[0]]
                canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
                canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(edge[2]))

    # Display the GUI window
    window.mainloop()


display_graph(newAdjList, visited)
