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

# quicksort implementation

def quickSort(l, r, arr):
    if l >= r:
        return

    # l is the pivot
    i, j = l, r

    while i < j:
        # loop until you find a value greater than the pivot
        while i <= r and arr[i] <= arr[l]:
            i += 1

        # loop until you find a value lesser than the pivot
        while j >= l and arr[j] > arr[l]:
            j -= 1

        # put lesser values on the left
        # greater on the right
        # only if i and j haven't overlapped
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # the correct position of the pivot in the sorted array is at j
    arr[l], arr[j] = arr[j], arr[l]

    # recurse for the left and right part of the pivot
    quickSort(l, j - 1, arr)
    quickSort(j + 1, r, arr)


arr = [2,5,3,4,0,1]
print("input", arr)
quickSort(0, len(arr) - 1, arr)
print("output", arr)
