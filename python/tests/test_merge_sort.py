from code_challenges.merge_sort.merge_sort import *


def test_mergeSort_1():

    arr = [12, 11, 13, 5, 6, 7]

    actual =  mergeSort(arr)

    expected = [5, 6, 7, 11, 12, 13]
    assert actual == expected


def test_mergeSort_2():

    arr = [20, 18, 12, 8, 5, -2]

    actual = mergeSort(arr)

    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_mergeSort_3():

    arr = [5, 12, 7, 5, 5, 7]

    actual = mergeSort(arr)

    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_mergeSort_4():

    arr = [2, 3, 5, 7, 13, 11]

    actual = mergeSort(arr)

    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
