V = int(input("Enter the number of vertices: "))
print(f"Enter the adjacency matrix ({V}x{V}) row by row (use 0 for no direct edge):")

graph = []
for i in range(V):
    row = list(map(int, input().split()))
    graph.append([99999 if x == 0 and i != j else x for j, x in enumerate(row)])

selected = [False] * V
selected[0] = True  
edges = 0
total_cost = 0  

print("\nMinimum Spanning Tree Edges (u - v : weight):")
while edges < V - 1:
    min_weight = 99999
    u, v = -1, -1

    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and graph[i][j] < min_weight:
                    min_weight = graph[i][j]
                    u, v = i, j

    print(f"{u} - {v} : {min_weight}")
    selected[v] = True
    total_cost += min_weight
    edges += 1

print("\nTotal Minimum Cost of MST:", total_cost)
