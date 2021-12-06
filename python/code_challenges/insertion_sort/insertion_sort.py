def InsertionSort(array):

    for i in range(1, len(array)):
        previous = i - 1
        current = array[i]
        while previous >= 0 and current < array[previous]:
            array[previous + 1] = array[previous]
            previous -= 1
            array[previous + 1] = current
    return array


print(InsertionSort([8,4,23,42,16,15]))
