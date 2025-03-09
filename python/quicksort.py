import time
import matplotlib.pyplot as plt
import statistics
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
num_experiments = int(input("Enter the number of experiments: "))
sizes, times = [], []
num_trials = 5  
for exp in range(num_experiments):
    arr = list(map(int, input(f"\nExperiment {exp + 1} (space-separated numbers): ").split()))
    sizes.append(len(arr))
    trial_times = [0] * num_trials  
    for t in range(num_trials):
        arr_copy = arr[:]  
        start = time.perf_counter()
        sorted_arr = quick_sort(arr_copy)
        trial_times[t] = time.perf_counter() - start  
    avg_time = statistics.mean(trial_times)
    times.append(avg_time)
    print(f"Sorted array: {sorted_arr[:10]}... (showing first 10 elements)")
    print(f"Quick Sort took {avg_time:.6f} sec (avg over {num_trials} runs)")
plt.plot(sizes, times, marker='o', linestyle='-', color='r', label="Quick Sort Time")
plt.xlabel("Elements (n)")
plt.ylabel("Time (sec)")
plt.title("Quick Sort Performance")
plt.grid(True)
plt.legend()
plt.show()
