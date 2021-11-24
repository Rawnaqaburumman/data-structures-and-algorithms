from code_challenges.stack_and_queue.stack_queue_pseudo import PseudoQueue
import pytest
from attr import asdict
from pytest import raises



def test_pseudo_dequeue_empty():
 stack1=Stack()
 stack2=Stack()
 stack1.push(1)
 stack1.push(2)
 stack1.push(3)
 queue=PseudoQueue()
 queue.enqueue(4)
 queue.dequeue()
 queue.dequeue()
 queue.dequeue()
 queue.dequeue()

with pytest.raises(Exception):
        assert PseudoQueue.dequeue()


def test_pseudo_queue_enqueue_value(pseudo_queue_1):
 stack1=Stack()
 stack2=Stack()
 stack1.push(1)
 stack1.push(2)
 stack1.push(3)
 queue=PseudoQueue()
 queue.enqueue(4)
 expected = 4
 actual = queue.dequeue()
 assert actual == expected


 def test_pseudo_queue_enqueue_multiple(pseudo_queue):

  stack2=Stack()
  stack1.push(1)
  stack1.push(2)
  stack1.push(3)
  queue=PseudoQueue()
  queue.enqueue(4)
  queue.enqueue(5)
  queue.enqueue(6)
  queue.dequeue()
  
  expected = 5
  actual = queue.dequeue()

  assert actual == expected







