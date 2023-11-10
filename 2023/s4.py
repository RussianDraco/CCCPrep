from collections import defaultdict
import tkinter as tk
import math

class Graph:
    def __init__(self):
        self.edges = [] #src, dst, length, cost

graph = Graph()

dimensions = input().split(" ")
for x in range(int(dimensions[1])):
    inp = input().split(" ")
    graph.edges.append([int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])])

interNum = int(dimensions[0])

newEdgeList = []
visited = [False] * interNum

currentNode = 0
visited[0] = True
dist = 0
path = []

sortedEdges = sorted(graph.edges, key=lambda x: x[3])

while False in visited:
    if not visited[sortedEdges[0][0] - 1] or not visited[sortedEdges[0][1] - 1]:
        if visited[sortedEdges[0][0] - 1]:
            currentNode = sortedEdges[0][1]
        else:
            currentNode = sortedEdges[0][0]
        visited[currentNode - 1] = True
        dist += sortedEdges[0][2]
        path.append(sortedEdges[0][3])
        newEdgeList.append(sortedEdges.pop(0))





def display_graph(newEdgeList, visited):
    # Create a window for the GUI
    window = tk.Tk()
    window.title("Graph")

    # Create a canvas to draw the nodes and edges
    canvas = tk.Canvas(window, width=500, height=500)
    canvas.pack()

    canvas.create_text(250, 25, text="ALL NODES ARE 1 LESS ON GRAPH THAN IN INPUT")

    # Get a set of all nodes in the graph
    nodes = set()
    for edge in newEdgeList:
        nodes.add(edge[0])
        nodes.add(edge[1])

    # Calculate the number of nodes and the radius of the circle that will contain them
    num_nodes = len(nodes)
    radius = min(200, (500 / 2) * 0.8)

    # Calculate the coordinates of each node on the circle
    node_coords = []
    for i in range(num_nodes):
        angle = i * (2 * math.pi / num_nodes)
        x = 250 + radius * math.cos(angle)
        y = 250 + radius * math.sin(angle)
        node_coords.append((x, y))

    # Draw the nodes and their labels
    node_dict = {}
    for i, node in enumerate(nodes):
        x, y = node_coords[i]
        node_dict[node] = canvas.create_oval(x-10, y-10, x+10, y+10, fill="white", outline="black")
        canvas.create_text(x, y, text=str(node))

    # Draw the edges between the nodes
    for edge in newEdgeList:
        if visited[edge[0]-1] and visited[edge[1]-1]:
            x1, y1 = node_coords[edge[0]-1]
            x2, y2 = node_coords[edge[1]-1]
            canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST)
            canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(edge[3]))

    # Display the GUI window
    window.mainloop()


display_graph(newEdgeList, visited)
