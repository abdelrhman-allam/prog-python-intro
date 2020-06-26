


def toArray(array_text):
    arr = arr_text.rstrip().split(',')
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr

# Bubble sort 
# best O(n)
# avg/worst O(n^2)
def insertionSort(arr):
    ln = len(arr)

    for i in range(1, ln): # start from 1 to sort before the index
        v = arr[i] # current value
        j = i - 1 # before sorted items

        while j >=0 and v < arr[j]: # test value less then previous item
            arr[j+1] = arr[j] # override with values with pervious
            j = j - 1 # j to previous index 

        arr[j+1] = v # assign to last j + 1

        
    return arr

while True:    
    try:
        arr_text = input('Enter your numbers comma seprated (e.g.: 13,3,5,7,8,6,22,5,7)\n')
        
        if len(arr_text) == 0: 
            break

        arr = toArray(arr_text)
        print('Input',arr)
        sorted = insertionSort(arr)
        print('Final',sorted)
    except Exception as identifier:
        print('Invalid input \nExiting!', identifier)    
        break
