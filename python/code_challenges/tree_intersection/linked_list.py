class Node:

    """
    Node class to create nodes
    """
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):

      return f" {self.value} and the next {self.next}"
#====================================== Class LinkedList and methodes =====================================
class LinkedList:

    """
     Linked In class
    """
    def __init__(self):
        self.head = None
    #==============================append methode==========================================
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
    #=====================================insert methode======================================
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

    #==================================include methode===========================================
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
    #======================================str =========================================
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
    #======================================insert after========================================
    def insert_after(self, value,new):

        """
        insert a new value after any value in the linked_list
        """
        current = self.head
        while current is not None:
            if current.value == value:
                break
            current = current.next

            new_node = Node(new)
            new_node.next = current.next
            current.next = new_node


    #============================insert before======================================

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

#=============================================================================
if __name__=="__main__":

  ll = LinkedList()
  ll.append(2)
  ll.append(5)
  ll.insert(9)
  print(ll)
  ll.insert_after(2,7)
#   ll.insert_after(2,7)
  print(ll)

# "head -> 1 -> 2 -> 3 -> 4 -> None"


