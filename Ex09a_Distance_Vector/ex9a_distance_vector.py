INF = 999
# cost matrix: graph[i][j] = link cost (INF = no link)
graph = [
    [0,   2,   INF, 1],
    [2,   0,   3,   7],
    [INF, 3,   0,   1],
    [1,   7,   1,   0],
]
n = len(graph)

# every router starts with its own neighbour costs
dist = [row[:] for row in graph]
hop = [[j if graph[i][j] != INF else -1 for j in range(n)] for i in range(n)]

# routers keep exchanging tables until nothing changes
changed = True
while changed:
    changed = False
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    hop[i][j] = hop[i][k]
                    changed = True

for i in range(n):
    print("\nRouting table of router", chr(65 + i))
    print("Dest  Cost  NextHop")
    for j in range(n):
        print(f"  {chr(65 + j)}   {dist[i][j]:4}   {chr(65 + hop[i][j])}")
