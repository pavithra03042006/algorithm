INF = float('inf')
V = int(input("Enter the number of vertices: "))
print(f"Enter the adjacency matrix ({V}x{V}) row by row:")
graph = []
for i in range(V):
    row = list(map(int, input().split()))
    graph.append([INF if x == 0 and i != j else x for j, x in enumerate(row)])
dist = [row[:] for row in graph]
for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][k] != INF and dist[k][j] != INF:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
print("\nShortest distances between every pair of vertices:")
for row in dist:
    for val in row:
        print("INF" if val == INF else val, end="\t")
    print()
