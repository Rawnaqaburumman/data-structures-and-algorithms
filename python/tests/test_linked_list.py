from linked_list.linked_list import LinkedList


def test_import():
    assert LinkedList

def test_instantiate():
    """
    Can successfully instantiate an empty linked list
    """
    ll=LinkedList()
    assert ll

def test_insert():
    """
    Can properly insert into the linked list
    """
    ll=LinkedList()
    ll.insert(2)
    actual = ll.head.value
    expected = 2
    assert actual ==expected

def test_head_point():
     """
     The head property will properly point to the first node in the linked list
     """

     ll=LinkedList()
     ll.append(1)
     actual=ll.head.value
     excepted=1
     assert actual==excepted

def test_insert_multiple():

     """
     Can properly insert multiple nodes into the linked list
     """
     ll=LinkedList()
     ll.insert(2)
     ll.insert(3)
     actual = str(ll)
     excepted = "head -> {3} -> {2} -> Null"
     assert actual == excepted

def test_finding_true_value():

    """
    Will return true when finding a value within the linked list that exists
    """
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    actual = ll.include(1)
    excepted = True
    assert actual == excepted


def test_finding_false_value():

    """
    Will return false when searching for a value in the linked list that does not exist
    """
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    actual = ll.include(5)
    excepted = False
    assert actual == excepted


def test_return_all():

    """
    Can properly return a collection of all the values that exist in the linked list
    """
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    actual=str(ll)
    expected = "head -> {1} -> {2} -> {3} -> {4} -> Null"
    assert actual == expected
