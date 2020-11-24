
def intersetion(ar1, ar2):
    m = len(ar1)
    n = len(ar2)
    p = []
    i = 0
    j = 0

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            p.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            p.append(arr2[j])
            j += 1
        else:
            p.append(arr2[j])
            i += 1
            j += 1

    while i < m:
        p.append(arr1[i])
        i += 1

    while j < n:
        p.append(arr2[j])
        j += 1

    return p


arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]

print intersetion(arr1, arr2)
