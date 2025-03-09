def find_max_min(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] > arr[1] else (arr[1], arr[0])
    
    mid = len(arr) // 2
    left_max, left_min = find_max_min(arr[:mid])
    right_max, right_min = find_max_min(arr[mid:])
    
    return max(left_max, right_max), min(left_min, right_min)

n = int(input("Enter the number of elements: "))
arr = list(map(int, input(f"Enter {n} elements separated by spaces: ").split()))

if len(arr) != n:
    print("Error: Number of elements entered does not match the expected count.")
else:
    max_num, min_num = find_max_min(arr)
    print("Maximum number:", max_num)
    print("Minimum number:", min_num)
