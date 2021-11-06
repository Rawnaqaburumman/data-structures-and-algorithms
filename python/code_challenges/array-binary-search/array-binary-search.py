def BinarySearch(array,key):

  j=len(array)-1
  i=0
  m=0
  while i<=j :
      m=(i+j)//2
      print(m)
      if array[m]<key:
       i=m+1
      elif array[m] > key:
        j=m-1
      else:
        return m
  return -1
print(BinarySearch([1,2,3,45,4],22))
