# Daily Coding Problem: Problem #331 [Medium]
# 
# You are given a string consisting of the letters x and y, such as xyxxxyxyy. 
# In addition, you have an operation called flip,
# which changes a single x to y or vice versa.

# Determine how many times you would need to apply this operation
#  to ensure that all x's come before all y's. 
# In the preceding example, it suffices to flip 
# the second and sixth characters, so you should return 2.

def flipxy2(arr):
    flip_count = 0
    last_y = len(arr)-1
    for i in range(len(arr)):
        if arr[i] == 'y':
            arr[i] = 'x'
            while arr[last_y] == 'y':
                last_y = last_y -1
            arr[last_y] =  'y'
            flip_count = flip_count + 1
            if last_y <= i:
                break

    print (arr)
    return flip_count

# what excepected as a result without flip action
def flipxy(arr):   
    last_y = len(arr)-1
    while arr[last_y] == 'y':
        last_y = last_y - 1

    flip_count = 0
    for i in range (last_y) :
        if arr[i] == 'y':
            flip_count = flip_count + 1

    
    return flip_count


txt = "xyxxxyxyxxxxxy"
count = flipxy2([ char for char in txt ])
print(count)
count = flipxy([ char for char in txt ])

txt = 'xyxxxyxyy' # == 2
count = flipxy([ char for char in txt ])
print(count)
