import random

def kth_smallest(arr, k):
    n = len(arr)
    temp = arr[:k]
    random.shuffle(temp)

    for i in range(k, n):
        for j in range(k):
            if arr[i] < temp[j]:
                temp[j] = arr[i]
                break

    return max(temp)

n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))
k = int(input("Enter the value of k: "))

print(f"{k}th smallest element is", kth_smallest(arr, k))
