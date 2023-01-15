#Comb sort

def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)

        if gap > 1:
            sorted = False

        else:
            gap = 1
            sorted = True

        i = 0

        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False

            i += 1

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", comb_sort(arr))
