
def rotateArray(arr, k):
    n = len(arr)
    reverseArray(arr, 0, k - 1)
    reverseArray(arr, k, n - 1)
    reverseArray(arr, 0, n - 1)


def reverseArray(arr, start, end):
    i = start
    j = end
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    print arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rotateArray(arr, 8)
