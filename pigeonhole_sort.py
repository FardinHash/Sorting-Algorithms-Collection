#Pigeonhole sort

def pigeonhole_sort(arr):
    min_val = min(arr)
    max_val = max(arr)

    pigeonholes = [0] * (max_val - min_val + 1)

    for x in arr:
        pigeonholes[x - min_val] += 1

    i = 0

    for count in range(len(pigeonholes)):
        while pigeonholes[count] > 0:
            pigeonholes[count] -= 1
            arr[i] = count + min_val
            i += 1

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", pigeonhole_sort(arr))
