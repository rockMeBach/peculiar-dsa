# divide the array into 2 halves
# then sort each sub-array
# recurse

def mergeSort(start, end, arr):
    if start >= end:
        return [arr[end]]

    mid = (start + end) // 2

    arr1 = mergeSort(start, mid, arr)
    arr2 = mergeSort(mid + 1, end, arr)

    new_arr = []

    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        new_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        new_arr.append(arr2[j])
        j += 1

    return new_arr

arr = [5, 4, 2, 9, 3, 1]
arr = mergeSort(0, len(arr) - 1, arr)
print(arr)
