from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjs = defaultdict(list) #src : dst, length, cost

graph = Graph()

dimensions = input().split(" ")
for x in int(dimensions[1]):
    inp = input().split(" ")
    graph.adjs[int(inp[0])].append((int(inp[1]), int(inp[2], int(inp[3]))))
    graph.adjs[int(inp[1])].append((int(inp[0]), int(inp[2], int(inp[3]))))

interNum = int(dimensions[0])

newAdjList = defaultdict(list)
visited = [False] * interNum

currentNode = 0
visited[0] = True
while False in visited:
    bestEdge = None
    for adj in graph.adjs[currentNode]:
        if visited[adj[0]]:
            continue
        if adj[2] < bestEdge[2]:
            bestEdge = adj
    if bestEdge == None:
        currentNode = visited.index(False)
        continue