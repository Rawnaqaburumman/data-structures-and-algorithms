# Tracing Quick Sort Code
This article traces a psuedo code for quick sort

## Pseudo Code
    ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

    ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

    ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp

# Trace:

1. Start:
![](part1.PNG)

```
  low = 1

    for 0 to 5

        i = 0:
        temp= 8
        [8,4,23,42,16,15]

        i = 1:
        temp= 8
        [8,4,23,42,16,15]

        i = 2:
        less than pivot

        i = 3:
       less than pivot

        i = 4:
       less than pivot

    Swap(arr,5, 2)

        [8,4,15,42,16,23]

```
![2](part2.PNG)


2.Call Quicksort again: and swap 4 and 8
``` low = -1
    for 0 to 1

    i=0:
    Swap(arr, 1, 0)
        [4,8,15,42,16,23]

```
3.position=low-1 =0 , QuickSort(arr, 1, 5):
```   low = 3
    for 1 to 5

    i= 1: less than pivot
    i= 2: less than pivot
    i= 3: less than pivot
    i= 4: less than pivot
    Swap(arr, 4, 3)
    [4,8,15,16,42,23]

    Swap(arr, 5, 4)
    [4,8,15,16,23,42]
```
![3](part3.PNG)
### Efficency
> Time Complexity : O(n2)
<br>
Space Complexity : O(log(N)) Because quick sort calls itself log(n) times.
