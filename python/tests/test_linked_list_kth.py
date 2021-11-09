from linked_list.linked_list_kth.linked_list_kth import LinkedList
import pytest


#=====================test 1 =================================================
def test_import():
    assert LinkedList
#=====================test 2 =================================================
def test_instantiate():
    """
    Can successfully instantiate an empty linked list
    """
    ll=LinkedList()
    assert ll
#======================test 3 Out the range =====================================================
def test_k_out_the_range():
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    actual=ll.kthFromEnd(5)
    k=5
    expected= f"{k} value was rejected --> out the range"
    assert actual == expected

#======================== test 4 k=the length of linked list===========================================
def test_k_equal_legth():
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    # ll.append(3)
    ll.append(4)
    k=3
    actual=ll.kthFromEnd(k)

    expected= f"{k} value was rejected --> k= length of linked list/out the range "
    assert actual == expected

#==============================test5 k is not possitive integer=================================
def test_k_negative_num():
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    k=-2
    actual=ll.kthFromEnd(k)

    expected= f"{k} value was rejected --> negative value"
    assert actual == expected


#=====================================test6Happy path============================================
def test_happy_bath():
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    k=2
    actual=ll.kthFromEnd(k)

    expected= 2
    assert actual == expected
#================================test7 k linked in is size =1 .=======================================
def test_size_one():
    ll=LinkedList()
    ll.append(1)
    k=2
    actual=ll.kthFromEnd(k)

    expected= " the linked list size is 1 "
    assert actual == expected
