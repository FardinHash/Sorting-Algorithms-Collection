#Quick sorting

def partition(arr, low, high):
    i = ( low - 1 )         
    pivot = arr[high]
 
    for j in range(low, high):
        if   arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i + 1]

    return(i + 1)

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
 
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi + 1, high)

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

print("Sorted array is:", quick_sort(arr,0,n-1))
