def insertShiftArray(arr,value):

    newArray = [ 0 for i in range(len(arr)+1)]

    if len(arr) % 2 == 0:
        j = len(arr)/2
    else:
       j=len(arr)/2 + 0.5

    for i in range(len(newArray)):
        if i == j:
          newArray[i] = value
        elif i < j:
           newArray[i] = arr[i]
        else:
           newArray[i] = arr[i-1]

    return newArray

print(insertShiftArray([1,2,3,2],7))



