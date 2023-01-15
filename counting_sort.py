#Counting sorting

def counting_sort(arr):
    max_element = max(arr)
    counting_arr = [0] * (max_element + 1)

    for element in arr:
        counting_arr[element] += 1

    sorted_arr = []

    for i in range(len(counting_arr)):
        for j in range(counting_arr[i]):
            sorted_arr.append(i)

    return sorted_arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", counting_sort(arr))
