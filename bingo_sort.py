#Bingo sort

import random

def bingo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)

    return arr

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False

    return True

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", bingo_sort(arr))
