

def toArray(array_text):
    arr = arr_text.rstrip().split(' ')
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr

# Selection sort 
# best O(n)
# avg/worst O(n^2)
def selectionSort(arr):
    ln = len(arr)
    
    for i in range(0, ln): # start from 1 to sort before the index
        l =  i # min value 
        for j in range(i+1, ln):
            if arr[l] > arr[j]:
                l = j
            
        arr[i], arr[l] = arr[l], arr[i] 
    return arr

while True:    
    try:
        arr_text = input('Enter your numbers comma seprated (e.g.: 13 3 5 7 8 6 22 5 7)\n')
        
        if len(arr_text) == 0: 
            break

        arr = toArray(arr_text)
        print('Input',arr)
        sorted = selectionSort(arr)
        print('Final',sorted)
    except Exception as identifier:
        print('Invalid input \nExiting!', identifier)    
        break
