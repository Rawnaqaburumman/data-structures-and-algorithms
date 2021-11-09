# from  linked_list.singly_linked_list.linked_list import ( Node, LinkedList)

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

#==============================Ziplist=========================================
def zipLists(self,ll1, ll2):
    current1 = ll1.head
    current2 = ll2.head


    while current1 != None and  current2 != None and self.head != None :
        current1=current1.next
        current2=current2.next

        current1.next=current2
        current2.next=current1


        current1=current1.next
        current2=current2.next
        ll2.head=ll1.head


    while self.head != None:
            yield self.head.data
            self.head = self.head.next






if __name__ == "__main__":
    ll1 =LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    print(ll1)
    print(ll2)
    print(zipLists(ll1, ll2))
