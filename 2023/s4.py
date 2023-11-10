from collections import defaultdict
import tkinter as tk

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
            break

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

    # Iterate through the newAdjList and draw a circle for each node
    nodes = {}
    for node in newAdjList:
        x = 50 + node * 50
        y = 50 + node * 50
        nodes[node] = canvas.create_oval(x-10, y-10, x+10, y+10, fill="white", outline="black")
        canvas.create_text(x, y, text=str(node))

    # Iterate through the newAdjList again and draw a line between each node and its adjacent nodes
    for node, edges in newAdjList.items():
        for edge in edges:
            if visited[node] and visited[edge[0]]:
                canvas.create_line(
                    50 + node * 50, 50 + node * 50,
                    50 + edge[0] * 50, 50 + edge[0] * 50,
                    arrow=tk.LAST
                )
                canvas.create_text(
                    (50 + node * 50 + 50 + edge[0] * 50) / 2,
                    (50 + node * 50 + 50 + edge[0] * 50) / 2,
                    text=str(edge[2]) #shows edge cost on arrow
                )

    # Display the GUI window
    window.mainloop()

display_graph(newAdjList, visited)
