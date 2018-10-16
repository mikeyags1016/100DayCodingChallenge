import random
import time

# Driver code for non-tests
list = []
for i in range(10000):
    list.append(random.randrange(1, 101))
start_time = time.time()


def bubble_sort(list):
    n = len(list)

    # Loop through entire list
    for i in range(n):
        # For each element, loop through rest of elements
        for j in range(0, n-i-1):
            # If j is bigger than the next element, swap
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list


def selection_sort(list):
    n = len(list)

    # Loop through entire list
    for i in range(n):
        # Set current element to i
        smallest = i
        # Loop through rest of list
        for j in range(i+1, n):
            # If current element is smaller than the current smallest,
            # set current to smalelst
            if list[j] < list[smallest]:
                smallest = j
        # When you have gone through the entire list,
        # swap the old smallest (i) with the current smallest
        # if they aren't equal
        if smallest != i:
            list[i], list[smallest] = list[smallest], list[i]

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


print(insertion_sort(list))
print("---- %s seconds ----" % (time.time() - start_time))