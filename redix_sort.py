#Redix sort

def radix_sort(arr):
    max_element = max(arr)
    exp = 1

    while max_element // exp > 0:
        arr = [x for x in arr if x // exp % 10] + [x for x in arr if x // exp % 10 == 0]
        exp *= 10

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", radix_sort(arr))
