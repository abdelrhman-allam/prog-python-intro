


def toArray(array_text):
    
    arr = arr_text.rstrip().split(',')
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr

# Bubble sort O(n^2)
def bubbleSort(arr):
    ln = len(arr)
    step = 0
    for i in range(ln-1):
        for j in range(ln-i-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
            step = step+1
            
    return arr

while True:    
    try:
        arr_text = input('Enter your numbers comma seprated (e.g.: 13,3,5,7,8,6,22,5,7)\n')
        if len(arr_text) == 0: break
        arr = toArray(arr_text)
        print('Input',arr)
        sorted = bubbleSort(arr)
        print('Final',sorted)
    except Exception as identifier:
        print('Invalid input \nExiting!', identifier)    
        break
