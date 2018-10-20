import random
import time


# Driver code for non-tests
arr = []
for i in range(10000):
    arr.append(random.randrange(1, 101))


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr):
    n = len(arr)

    # Loop through entire arr
    for i in range(n):
        # For each element, loop through rest of elements
        for j in range(0, n - i - 1):
            # If j is bigger than the next element, swap
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)

    return arr


def selection_sort(arr):
    n = len(arr)

    # Loop through entire arr
    for i in range(n):
        # Set current element to i
        smallest = i
        # Loop through rest of arr
        for j in range(i + 1, n):
            # If current element is smaller than the current smallest,
            # set current to smallest
            if arr[j] < arr[smallest]:
                smallest = j
        # When you have gone through the entire arr,
        # swap the old smallest (i) with the current smallest
        # if they aren't equal
        if smallest != i:
            swap(arr, i, smallest)

    return arr


def insertion_sort(arr):
    n = len(arr)

    # Loop through the unsorted arr
    for i in range(1, n):
        key = arr[i]

        # Loop through sorted arr and locate
        # the spot where the current element
        # is supposed to go
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


start_time = time.time()


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0

    # While we are not at the end of either half,
    # insert the new elements into the new arr
    # and add remaining elements
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def merge_sort(arr):
    # If the arr is only one element long, return the arr
    if len(arr) < 2:
        return arr

    # Create two halves of arrs and merge theme
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def partition(arr, left, right):

    pivot = right

    # Place pivot at beginning of the list and border
    i = left - 1

    # If j is less than pivot, move border up and swap i and j
    for j in range(left, right):
        if arr[j] <= arr[pivot]:
            i += 1
            swap(arr, i, j)

    # Place pivot back in it spot
    swap(arr, i + 1, right)
    return i + 1


def quick_sort_helper(arr, left, right):
    # If there is more than one element in the list
    if left < right and len(arr) <= 20:
        insertion_sort(arr)
    elif left < right:
        # Return pivot after partitioning for two halves
        p = partition(arr, left, right)

        quick_sort_helper(arr, left, p - 1)
        quick_sort_helper(arr, p + 1, right)


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)
    return arr


print(quick_sort(arr))
print("---- %s seconds ----" % (time.time() - start_time))