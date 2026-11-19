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

# find the pivot
# any elem x that is x <= pivot goes on the left
# x >= pivot goes on the right
# do the same on both the sides of the pivot

def quickSort(arr):
    if not arr:
        return []

    n = len(arr)
    mid = n // 2

    pivot = arr[mid]
    l_arr, r_arr = [], []
    i = 0

    while i < n:
        if i == mid:
            i += 1
            continue

        if arr[i] <= pivot:
            l_arr.append(arr[i])
        else:
            r_arr.append(arr[i])

        i += 1

    arr1 = quickSort(l_arr)
    arr2 = quickSort(r_arr)

    return arr1 + [pivot] + arr2

arr = [7,3,4,8,3,6,9,9,3,4,6,0,2,5,6,3,82,53,9,4,7]
arr = quickSort(arr)
print(arr)