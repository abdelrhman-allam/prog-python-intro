import random


def swap(a, q, p):
    tmp = a[q]
    a[q] = a[p]
    a[p] = tmp


def bubble_sort(a):
    sorted = False

    while sorted == False:
        sorted = True
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                swap(a, i, i+1)
                sorted = False

    return a


# print(bubble_sort([5, 4,  7, 6,  2, 3, 8, 1]))


def selection_sort(q):
    for i in range(0, len(q)):

        min = i
        for j in range(i+1, len(q)):

            if(q[j] < q[min]):
                min = j

        swap(q, min, i)
    return q


print(selection_sort([5, 4,  7, 6,  2, 3, 8, 1]))


def quick_sort(a):

    quick_sort_helper(a, 0, len(a)-1)


def quick_sort_helper(a, start, end):
    if start < end:
        p = partation(a, start, end)
        quick_sort_helper(a, start, p - 1)
        quick_sort_helper(a, p + 1, end)


def partation(a, first, last):
    pivot_value = a[first]
    left_pointer = first + 1
    right_pointer = last

    done = False

    while not done:

        while left_pointer <= right_pointer and a[left_pointer] <= pivot_value:
            left_pointer = left_pointer + 1
        while a[right_pointer] >= pivot_value and right_pointer >= left_pointer:
            right_pointer = right_pointer - 1

        if right_pointer < left_pointer:
            done = True
        else:
            temp = a[left_pointer]
            a[left_pointer] = a[right_pointer]
            a[right_pointer] = temp
    temp = a[first]
    a[first] = a[right_pointer]
    a[right_pointer] = temp

    return right_pointer


unsorted = [random.randrange(0, 10*(i+1)) for i in range(10)]
print(unsorted)
quick_sort(unsorted)
print(unsorted)
