from stack_and_queue.node import Node
from stack_and_queue.queue import Queue
from stack_and_queue.stack import Stack


def test_push_stack():
  a=Stack()
  a.push(1)
  a.push(2)
  a.push(3)
  actual=print(a)
  excepted = "top -> {3} -> {2} -> {1} -> Null"
  assert actual == excepted


