from stack_and_queue.stack import Stack
# from stack_and_queue.node import Node
# from stack_and_queue.queue import Queue

class PseudoQueue:
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()
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


if __name__=="__main__":
 stack1=Stack()
 stack2=Stack()
 stack1.push(1)
 stack1.push(2)
 stack1.push(3)
 queue=PseudoQueue()




