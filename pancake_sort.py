#Pancake sort

def pancake_sort(arr):
    n = len(arr)

    for curr_size in range(n, 1, -1):
        max_idx = arr.index(max(arr[0:curr_size]))

        if max_idx != curr_size-1:
            if max_idx != 0:
                arr[:max_idx+1] = reversed(arr[:max_idx+1])

            arr[:curr_size] = reversed(arr[:curr_size])

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", pancake_sort(arr))
