from code_challenges.quick_sort.quick_sort import *



def test_random_sorted():
    arr=[8,4,23,42,16,15]
    quicksort(arr,0,len(arr)-1)
    assert arr[0]==4
    assert arr[1]==8
    assert arr[-1]==42

def test_Reverse_sorted():
    arr=[20,18,12,8,5,-2]
    quicksort(arr,0,len(arr)-1)
    assert arr[0]==-2
    assert arr[1]==5
    assert arr[-1]==20

def test_Few_uniques():
    arr=[5,12,7,5,5,7]
    quicksort(arr,0,len(arr)-1)
    assert arr[0]==5
    assert arr[1]==5
    assert arr[-1]==12

def test_Few_uniques():
    arr=[5,12,7,5,5,7]
    quicksort(arr,0,len(arr)-1)
    assert arr[0]==5
    assert arr[1]==5
    assert arr[-1]==12

def test_Nearly_sorted():
    arr=[2,3,5,7,13,11]
    quicksort(arr,0,len(arr)-1)
    assert arr[0]==2
    assert arr[1]==3
    assert arr[-1]==13
