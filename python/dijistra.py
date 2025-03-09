V = int(input("Enter the number of vertices: "))  
INF = 9999  
def min_distance(dist, visited):
    min_val = INF
    min_index = -1
    for v in range(V):
        if not visited[v] and dist[v] <= min_val:
            min_val = dist[v]
            min_index = v
    return min_index
def print_solution(dist):
    print("Vertex \t Distance from Source")
    for i in range(V):
        print(f"{i} \t\t {dist[i]}")
def dijkstra(graph, src):
    dist = [INF] * V  
    visited = [False] * V  
    dist[src] = 0  
    for _ in range(V - 1):
        u = min_distance(dist, visited)
        visited[u] = True
        for v in range(V):
            if not visited[v] and graph[u][v] != 0 and dist[u] != INF and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print_solution(dist)
graph = []
print(f"Enter the adjacency matrix ({V}x{V}) row by row:")
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)
src = int(input("Enter the source vertex: "))
dijkstra(graph, src)
