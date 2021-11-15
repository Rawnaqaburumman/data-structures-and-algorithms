

from attr import asdict
import pytest
from code_challenges.stack_and_queue.stack_and_queue import Stack,Node,Queue
from pytest import raises

def test_push_stack():
    """
    push  multiple values
    """
    a=Stack()
    a.push(1)
    a.push(2)
    a.push(3)
    actual=str(a)
    excepted = "top -> {3} -> {2} -> {1} -> Null"
    assert actual == excepted
#===========================================================================
def test_push_stack2():
    """
    push one value
    """
    a=Stack()
    a.push(1)

    actual=str(a)
    excepted = "top -> {1} -> Null"
    assert actual == excepted
#============================================================================
def test_empty_after_pop_from_stack():
    """
     pop off the stack
    """
    a=Stack()
    a.push(1)
    a.push(2)
    a.push(3)
    a.pop()
    actual=str(a)
    excepted="top -> {2} -> {1} -> Null"
    assert actual == excepted


#=============================================================================

def test_pop_function():
    a=Stack()
    a.push(1)
    a.push(2)
    actual= a.pop()
    excepted= 2
    assert actual == excepted


#===========================================================================
def test_empty_stck_after_many_pops():
    """
    empty a stack after multiple pops
    """
    a=Stack()
    a.push(1)
    a.push(2)
    a.push(3)
    a.pop()
    a.pop()
    a.pop()
    with pytest.raises(Exception):
        assert a.pop()

#=================================================================================
def test_peak_next_item():
    """
  peek the next item on the stack
  """

    a=Stack()
    a.push(1)
    a.push(2)
    a.push(3)
    a.pop()
    actual = a.peek()
    excepted= 2
    assert actual == excepted
#==================================================================================
def test_initantiate_empty_stack():
    """
    instantiate an empty stack
     """

    a=Stack()
    with pytest.raises(Exception):
        assert a.peek()

#===================================================================================
def test_exception_with_empty():
    """
    Calling pop or peek on empty stack raises exception
    """
    a=Stack()
    with pytest.raises(Exception):
        assert a.peek()
        assert a.pop
#=======================================================================================


def test_enqueue():

    """
    enqueue multiple values into a queue
    """
    a=Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    actual=str(a)
    excepted= "front -> {1} -> {2} -> {3} -> Null"
    assert actual==excepted
#===================================================================================
def test_peek_into_queue():
     """
     peek into a queue, seeing the expected value
     """
     a=Queue()
     a.enqueue(1)
     a.enqueue(2)
     a.enqueue(3)
     actual=a.peek()
     excepted=1
     assert excepted ==actual


def test_dqueue():
     """
      dequeue out of a queue the expected value
      """

     a=Queue()
     a.enqueue(1)
     a.enqueue(2)
     a.enqueue(3)
     actual=a.dequeue()
     excepted=1
     assert excepted ==actual

def test_Multiple_deque():
     """"
    multiple dequeues +empty a queue after multiple dequeues
    """
     a=Queue()
     a.enqueue(1)
     a.enqueue(2)
     a.enqueue(3)
     a.enqueue(4)
     a.dequeue()
     a.dequeue()
     actual= str(a)
     excepted= "front -> {3} -> {4} -> Null"
     assert actual==excepted
     a.dequeue()
     a.dequeue()
     with pytest.raises(Exception):
      assert a.dequeue()


def test_peek_in_queue():
    """
    peek into a queue, seeing the expected value
    """
    a=Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    actual=a.peek()
    excepted=1
    assert actual == excepted


def test_instantiate_an_empty_queue():
      """
      Calling dequeue or peek on empty queue raises exception
      """
      a=Queue()
      with pytest.raises(Exception):
       assert a.dequeue()
       assert a.peek()





