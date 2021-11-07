class Node:

    """
    Node class
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):

      return f" {self.value} and the next {self.next}"

class LinkedList:

    """
     Linked In class
    """
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        append methode used to add values at the end of linked list
        """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node

    def insert(self,value):

     """
     insert methode used to add nodes at the begining of linked list
     """
     node = Node(value)
     if self.head:
      current = self.head
      self.head=node
      self.head.next=current
     else:
         self.head=node


    def include(self,value):

        """
        include methode to search if the linked list include the values
        """
        current = self.head
        while current.next != None:
                if current.value==value:

                 return True
                current=current.next
        return False

    def __str__(self):
        output = "head -> "
        if self.head is None:
            output += None
        else:
            current = self.head
            while(current):
                output += "{%s} -> "%(current.value)
                current = current.next
            output += "Null"
            return output

    def insert_after(self,value,new):
       current = self.head
       node = Node(new)
       oldnode=Node(value)
       print(node)
       while current.next != None:
                if current.value==value:
                   current.next= node
                   oldnode.next= node.next
                   break


                else:
                      current=current.next




    def insert_before(self,val,new):
        """
        Method to add values before a specifc node
        """
        node=Node(new)
        if self.head == None:
            self.head = node
        else:
            current=self.head
        while current.next != None:

            if current.next.value == val:
                node.next = current.next
                current.next = node
                break
            else:
                current = current.next


if __name__=="__main__":
 ll = LinkedList()

 ll.append(1)
 ll.append(2)
 ll.append(3)
 ll.append(4)
 print(ll)
#  ll.insert_after(2,9)
 ll.insert_before(3,7)
 print(ll)
# "head -> 1 -> 2 -> 3 -> 4 -> None"


