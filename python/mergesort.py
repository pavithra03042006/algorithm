import time
import matplotlib.pyplot as plt
import statistics
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            arr[k] = left[i] if left[i] <= right[j] else right[j]
            i, j = (i + 1, j) if left[i] <= right[j] else (i, j + 1)
            k += 1        
        arr[k:], arr[k + len(left) - i:] = left[i:], right[j:]
num_experiments = int(input("Enter the number of experiments: "))
sizes, times = [], []
num_trials = 5  
for exp in range(num_experiments):
    arr = list(map(int, input(f"\nExperiment {exp + 1} (space-separated numbers): ").split()))
    sizes.append(len(arr))
    trial_times = [time.perf_counter() - time.perf_counter() for _ in range(num_trials)] 
    for t in range(num_trials):
        arr_copy = arr[:]  
        start = time.perf_counter()
        merge_sort(arr_copy)
        trial_times[t] = time.perf_counter() - start  
    avg_time = statistics.mean(trial_times)
    times.append(avg_time)
    print(f"Sorted array: {arr_copy}")
    print(f"Time: {avg_time:.6f} sec (avg over {num_trials} runs)")
plt.plot(sizes, times, marker='o', linestyle='-', color='b', label="Merge Sort Time")
plt.xlabel("Elements (n)");plt.ylabel("Time (sec)")
plt.title("Merge Sort Performance");plt.grid(True);plt.legend()
plt.show()
