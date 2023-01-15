#Heap sorting

def heafy(arr, n, i):
    largest = i 
    l = 2 * i + 1
    r = 2 * i + 2 
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
 
        heafy(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heafy(arr, n, i)
 
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heafy(arr, i, 0)
 
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", heap_sort(arr))
