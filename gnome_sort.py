#Gnome sort

def gnome_sort(arr):
    n = len(arr)
    index = 0

    while index < n:
        if index == 0:
            index += 1

        if arr[index] >= arr[index - 1]:
            index += 1

        else:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index -= 1

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", gnome_sort(arr))
