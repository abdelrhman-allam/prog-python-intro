def mergeSort(array):
  ln = len(array)
  if ln < 2:
    return array
  mid = ln // 2
  l = array[:mid]
  r = array[mid:]
  l = mergeSort(l)
  r = mergeSort(r)
  a = merge(l, r)
 
  return a

def merge(l, r):
  a = [ i for i in range(len(l) + len(r))]
  k = 0
  i = 0
  j = 0 # to pointers to index of each array
  while(i < len(l) and j < len(r)):
    if l[i] < r[j]:
      a[k] = l[i]
      i = i + 1
    else:
      a[k] = r[j]
      j = j + 1
    k=k+1
  
  while i < len(l):
    a[k] = l[i]
    i = i + 1
    k = k + 1
  
  while j < len(r):
    a[k] = r[j]
    j = j + 1
    k = k + 1
  
  return a

o = mergeSort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92])
print(o)
