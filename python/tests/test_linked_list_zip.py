from  linked_list.linked_ist_zip.linked_list_zip import LinkedList, Node
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
#======================test 3 happy path =====================================================
def test_zip():
    ll1=LinkedList()
    ll2=LinkedList()

    ll1.append(1)
    ll1.append(3)
    ll1.append(5)

    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    actual = LinkedList.zipLists(ll1,ll2)
    excepted = "head -> {1} -> {2} -> {3} -> {4} -> {5} -> {6} -> None"
    assert actual == excepted

#=======================================================================================
def test_none_linked():
    ll1=LinkedList()
    ll2=LinkedList()

  

    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    actual = LinkedList.zipLists(ll1,ll2)
    excepted = "head -> {1} -> {2} -> {3} -> {4} -> {5} -> {6} -> None"
    assert actual == excepted
