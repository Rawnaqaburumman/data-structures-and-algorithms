class Node:

    def __init__(self, value=None):
        self.next=None
        self.value=value


class EmptyStack(Exception):
    pass


class Stack:
    """
    a class that implements the Stack Data structure
    """
    count2=0
    def __init__(self):
        self.top=None
    @classmethod
    def countering(cls):
        """
        method to count the number of values added
        """
        return cls.count2

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
        Stack.count2+=1
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

#======================================================================================

def multi_bracket_validation(input):



    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = Stack()
    count=0
    print([stack.countering()-1])
    for c in input:
        print(stack.countering())
        if c.isalpha() or c not in ["{","}","(",")","[","]"]:
            count=count+1



            continue
        elif c in "{[(":
            stack.push(c)


        elif stack and c == pairs[c]:


            stack.pop()

        else:
            return False

    if count==len(input):
            return False
    return stack.countering()-1 == 0






print(multi_bracket_validation("[]aa"))


