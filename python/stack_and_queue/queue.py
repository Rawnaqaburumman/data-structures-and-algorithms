from node import Node


class Queue:
    """
    a class that implements the Queue Data structure
    """
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, value):
        node=Node(value)

        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node



    def __str__(self):
        output = "front -> "
        if self.front is None:
            output += None
        else:
            current = self.front
            while(current):
                output += "{%s} -> "%(current.value)
                current = current.next
            output += "Null"
            return output

    def dequeue(self):
        if self.front == None:
              raise EmptyQueue("This stack is empty")
        else:

          temp=self.front
          self.front=self.front.next
          temp.next=None
          return temp

    def peek(self):

     if self.front:
      return self.front.value
     else:
            raise Emptyqueue("This queue is empty")

    def is_empty(self):
        return self.front == None


if __name__=="__main__":
    a=Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.dequeue()
    print(a)
    # print(a.peek())
    # print(a.is_empty())
