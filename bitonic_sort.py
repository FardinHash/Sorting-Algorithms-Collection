#Bitonic sort

def bitonic_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", bitonic_sort(arr))
