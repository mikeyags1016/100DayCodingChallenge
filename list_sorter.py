import random
import time

# Driver code for non-tests
list = []
for i in range(10000):
    list.append(random.randrange(1, 101))


def swap(list, i, j):
    list[i], list[j] = list[j], list[i]


def bubble_sort(list):
    n = len(list)

    # Loop through entire list
    for i in range(n):
        # For each element, loop through rest of elements
        for j in range(0, n - i - 1):
            # If j is bigger than the next element, swap
            if list[j] > list[j + 1]:
                swap(list, j, j + 1)

    return list


def selection_sort(list):
    n = len(list)

    # Loop through entire list
    for i in range(n):
        # Set current element to i
        smallest = i
        # Loop through rest of list
        for j in range(i + 1, n):
            # If current element is smaller than the current smallest,
            # set current to smallest
            if list[j] < list[smallest]:
                smallest = j
        # When you have gone through the entire list,
        # swap the old smallest (i) with the current smallest
        # if they aren't equal
        if smallest != i:
            swap(list, i, smallest)

    return list


def insertion_sort(list):
    n = len(list)

    # Loop through the unsorted list
    for i in range(1, n):
        key = list[i]

        # Loop through sorted list and locate
        # the spot where the current element
        # is supposed to go
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key

    return list

start_time = time.time()

def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0

    # While we are not at the end of either half,
    # insert the new elements into the new list
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


def merge_sort(list):
    # If the list is only one element long, return the list
    if len(list) < 2:
        return list

    # Create two halves of lists and merge theme
    middle = len(list) // 2
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])

    return merge(left, right)


print(merge_sort(list))
print("---- %s seconds ----" % (time.time() - start_time))
