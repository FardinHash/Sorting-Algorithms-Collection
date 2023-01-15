#Bucket sort

def bucket_sort(arr):
    max_element = max(arr)
    buckets = [[] for x in range(len(arr))]

    for element in arr:
        buckets[int(element/max_element * (len(buckets) - 1))].append(element)

    for bucket in buckets:
        bucket.sort()
  
    sorted_arr = []

    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array is:", bucket_sort(arr))
