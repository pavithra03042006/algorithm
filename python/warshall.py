n = int(input("Enter the number of vertices: "))

graph = []
print("Enter the adjacency matrix row by row:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):

        for j in range(n):
            graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])

print("Transitive Closure:")
for row in graph:
    print(" ".join(map(str, row)))
