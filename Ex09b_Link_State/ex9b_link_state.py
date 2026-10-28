INF = 999
graph = [
    [0,   2,   INF, 1],
    [2,   0,   3,   7],
    [INF, 3,   0,   1],
    [1,   7,   1,   0],
]
n = len(graph)
src = 0     # source router A

# Dijkstra's shortest path algorithm
dist = [INF] * n
prev = [-1] * n
visited = [False] * n
dist[src] = 0

for _ in range(n):
    # pick unvisited node with smallest distance
    u = -1
    for i in range(n):
        if not visited[i] and (u == -1 or dist[i] < dist[u]):
            u = i
    visited[u] = True
    for v in range(n):
        if graph[u][v] != INF and dist[u] + graph[u][v] < dist[v]:
            dist[v] = dist[u] + graph[u][v]
            prev[v] = u

print("Shortest paths from router A")
print("Dest  Cost  Path")
for v in range(n):
    path = []
    x = v
    while x != -1:
        path.insert(0, chr(65 + x))
        x = prev[x]
    print(f"  {chr(65 + v)}   {dist[v]:4}  " + " -> ".join(path))
