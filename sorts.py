# recurse:
# divide the array into 2 halves
# then sort both the halves
# combine

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    def combine(left, right):
        results = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                results.append(left[i])
                i += 1
            else:
                results.append(right[j])
                j += 1

        while i < len(left):
            results.append(left[i])
            i += 1

        while j < len(right):
            results.append(right[j])
            j += 1

        return results

    mid = len(arr) // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return combine(left, right)

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
        while j > l and arr[j] > arr[l]:
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


arr = [1,2]
arr = mergeSort(arr)
print(arr[:1], arr[1:])
