class Node:
   def __init__(self,value):
       self.value=value
       self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node
    def reverseList(self,list):
                listt=list
                previous = None
                current = list.head
                following = current.next
                while current:
                    current.next = previous
                    previous = current
                    current = following
                    if following:
                        following = following.next
                list.head = previous

                if listt == list:
                   return True
                else:
                       return False


    def __str__(self):
        result = ""
        if self.head is None:
            result += None
        else:
            current = self.head
            while(current):
                result += "{ "+str(current.value)+" } -> "
                current = current.next
            result += "NULL"
            return result



if __name__=="__main__":
    newlist=LinkedList()

    newlist.insert(1)
    newlist.insert(2)
    newlist.insert(3)
    newlist.insert(2)
    newlist.insert(1)
    newlist.reverseList(newlist)
    print(newlist)
print (newlist.reverseList(newlist))
