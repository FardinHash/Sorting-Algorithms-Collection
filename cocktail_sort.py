#Cocktail sort

def cocktail_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while left < right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        right -= 1

        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
  
        left += 1

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", cocktail_sort(arr))
