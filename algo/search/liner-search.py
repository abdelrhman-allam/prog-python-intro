def toArray(array_text):
    arr = arr_text.rstrip().split(' ')
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    return arr

# O(n)

def search(arr, val):
    for i in range(len(arr)):
        if val == arr[i]:
            return i # found
    
    return -1 # not found

while True:    
    try:
        arr_text = input('Enter your numbers comma seprated (e.g.: 13 3 5 7 8 6 22 5 7)\n')
        val = input('Enter value to find (e.g. 8)\n')
        if len(arr_text) == 0 or len(val) == 0: 
            break

        arr = toArray(arr_text)
        val = int(val)
        found = search(arr, val)
        print('Final',found)
    except Exception as identifier:
        print('Invalid input \nExiting!', identifier)    
        break