import numpy as np
import math
import random

def opt_solution(dist_matrix, num_cities):
    visited = [False] * num_cities
    current_city = 0
    total_cost = 0

    visited[current_city] = True

    for _ in range(num_cities - 1):
        min_cost = math.inf
        next_city = -1

        for j in range(num_cities):
            if not visited[j] and dist_matrix[current_city][j] < min_cost:
                min_cost = dist_matrix[current_city][j]
                next_city = j

        total_cost += min_cost
        visited[next_city] = True
        current_city = next_city

    total_cost += dist_matrix[current_city][0]  
    return total_cost

def approx_algorithm(dist_matrix, num_cities):
    cities = list(range(num_cities))
    random.shuffle(cities)

    total_cost = 0
    for i in range(num_cities - 1):
        total_cost += dist_matrix[cities[i]][cities[i + 1]]

    total_cost += dist_matrix[cities[-1]][cities[0]] 
    return total_cost

num_cities = int(input("Enter the number of cities: "))
dist_matrix = []

print("Enter the distance matrix row by row:")
for _ in range(num_cities):
    row = list(map(int, input().split()))
    dist_matrix.append(row)

dist_matrix = np.array(dist_matrix)

opt_sol = opt_solution(dist_matrix, num_cities)
approx_sol = approx_algorithm(dist_matrix, num_cities)

print("Optimal Solution: ", opt_sol)
print("Approximated Solution: ", approx_sol)
print("Error: ", abs(opt_sol - approx_sol))
