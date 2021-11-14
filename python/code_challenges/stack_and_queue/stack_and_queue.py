class Node:

    def __init__(self, value=None):
        self.next=None
        self.value=value

#===============================================Queue=====================================================



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
          return temp.value

    def peek(self):

     if self.front:
      return self.front.value
     else:
            raise Emptyqueue("This queue is empty")

    def is_empty(self):
        return self.front == None
#========================================STACK============================================================






class Stack:
    """
    a class that implements the Stack Data structure
    """
    def __init__(self):
        self.top=None



    def __str__(self):
        output = "top -> "
        if self.top is None:
            output += "None"
        else:
            current = self.top
            while(current):
                output += "{%s} -> "%(current.value)
                current = current.next
            output += "Null"
            return output

    def push(self, value):
        node = Node(value)
        if self.top:
            node.next=self.top

        self.top=node


    def pop(self):

        if self.top == None:
            raise EmptyStack("This stack is empty")
        else:
         temp =self.top
         self.top=self.top.next
         temp.next=None
        return temp.value




    def peek(self):
     if self.top:
      return self.top.value
     else:
            raise EmptyStack("This stack is empty")

    def is_empty(self):
        return self.top == None





if __name__=="__main__":
    # a=Stack()



    # print(a.peek())
    # print(a.is_empty())
    a=Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    print(a.dequeue())
    print(a)
    print(a.peek())
    print(a.is_empty())
