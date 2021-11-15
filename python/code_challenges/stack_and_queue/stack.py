from node import Node


class EmptyStack(Exception):
    pass


class Stack:
    """
    a class that implements the Stack Data structure
    """
    def __init__(self):
        self.top=None



    def __str__(self):
        output = "top -> "
        if self.top is None:
            output += None
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
    a=Stack()
    a.push(1)
    a.push(2)
    a.push(3)
    print(a)
    print(a.peek())
    print(a.is_empty())

