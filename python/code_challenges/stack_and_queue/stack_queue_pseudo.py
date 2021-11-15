from stack import Stack
from  node import Node
# from stack_and_queue.queue import Queue

class PseudoQueue:
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()
        self.front = None
        self.rear = None


    def enqueue(self,value):
        self.stack1.push(value)
    def dequeue(self):
        while self.stack1.top:
            stack1_item = self.stack1.pop()
            self.stack2.push(stack1_item)
        item=self.stack2.pop()
        while self.stack2.top:
            stack2_item=self.stack2.pop()
            self.stack1.push(stack2_item)

        return item



    # def __str__(self):
    #     current=self.stack1.top
    #     x=''
    #     while current:
    #         if not current.next:
    #             x=x+f'( {current.value} )'
    #             current=current.next
    #         else:
    #             x=x+f'( {current.value} ) -> '
    #             current=current.next
        return x

if __name__=="__main__":
  stack2=Stack()
  stack1=Stack()
  stack1.push(1)
  stack1.push(2)
  stack1.push(3)
  qsueue=PseudoQueue()
  qsueue.enqueue(4)
  qsueue.enqueue(5)
  qsueue.enqueue(6)
  qsueue.dequeue()
  print(qsueue.dequeue())







