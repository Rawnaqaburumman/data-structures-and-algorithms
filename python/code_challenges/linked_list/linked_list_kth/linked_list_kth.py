


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
#============================kthFromEnd(k)=================================================
    def kthFromEnd(self,k):
        """
        kth from end
        argument: a number, k, as a parameter.
        Return the node’s value that is k places from the tail of the linked list.
        You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
        """

        if k<0:
            return f"{k} value was rejected --> negative value"


        count=0
        current = self.head
        if current.next == None:
          return " the linked list size is 1 "
        while current.next != None:
         current=current.next
         count+=1
         diff=count-k

        if count+1 ==k:
            return f"{k} value was rejected --> k= length of linked list/out the range "
        elif diff<0:
            return f"{k} value was rejected --> out the range"

        else:
         current = self.head.next
         while k < diff:
            current=current.next

         return current.value



if __name__=="__main__":

    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print(ll.kthFromEnd(2))



