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
    def zipLists(ll1,ll2):

        current1 = ll1.head
        current2 = ll2.head

        if current1 == None or current2 == None:
            if current1:
                return ll1
            elif current2:
                return ll2
            else:
             return "Both of the linked list is empty"




        li = []
        while current1 or current2:
            if(current1):
                li+=[current1.value]
                current1 = current1.next
            if(current2):
                li+=[current2.value]
                current2 = current2.next
            print(li)
        nodee='head -> '
        for i in li:
         nodee+="{%s} -> "%(i)
        nodee+='None'

        return nodee








if __name__ == "__main__":
    ll1 =LinkedList()
  
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    print(ll1)
    print(ll2)
    print(LinkedList.zipLists(ll1,ll2))

