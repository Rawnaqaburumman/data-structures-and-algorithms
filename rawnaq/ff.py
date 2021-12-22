class Node:

    """
    Function to initialise the node Class
    """
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    """
    Creating Nodes in linked List way
    """
    counter=0
    def __init__(self):
        self.head = None

    def __str__(self):
        """
        method to print and display the   values added
        """
        output = "head -> "
        if self.head is None:
            output += None
        else:
            current = self.head
            while(current):

                output += ("["+str(current.value)+"]"+" -> ")
                current = current.next
            output += "None"
            return output


    def append(self, valueAdded):
        """
        Method to add values to the end of nodes
        """
        LinkedList.counter += 1


        node = Node(valueAdded)

        if self.head == None:
            self.head = node

        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = node
            return "value added"




    def insert(self, valueAdded):
        """
        Method to add values at the beginning  nodes
        """
        node = Node(valueAdded)

        if self.head==None:
            self.head=node

        else:

            node.next=self.head

            self.head=node


        return "value added"

    def insert_before(self, val, valueAdded):
        node = Node(valueAdded)
        if self.head==None:
            self.head=node
        elif self.head.value == val:
            node.next = self.head
            self.head = node
        else:
            current = self.head

            while current.next !=None:

                if current.next.value == val:
                    node.next = current.next
                    current.next = node
                    break
                current = current.next


    def insert_after(self, val, valueAdded):

        """
        Method to add values after a specifc node
        """
        node = Node(valueAdded)

        if self.head==None:
            self.head=node

        elif self.head.value == val:
            node.next = self.head.next
            self.head.next = node
        else:
            current=self.head

            while current.next != None:

                if current.next.value == val:
                    current = current.next

                    node.next = current.next
                    current.next = node
                    break
                current = current.next




    def deleteNode(self, key):
        current = self.head

        if self.head==None:
           return "empty list"
        elif self.head.value == key:

            self.head =self.head.next
            current=None
            return
        while current.next!=None:
            if current.next.value == key:
                 current=current
                 print(current.value)
                 current = current.next
                 current.next=current.next
                 current=None
            if current:
                 current = current.next

    def deleteNodepos(self, position):

        if self.head == None:
            return

        current = self.head

        if position == 0:
            self.head = current.next
            current = None
            return

        for i in range(position -1 ):
            current = current.next
            if current is None:
                break

        if current is None:
            return
        if current.next is None:
            return
        current = current.next.next

        current.next = None

        current.next = current




    def includes(self, valueSearched):
        """
        method to search for a specifc value
        """
        current = self.head
        if self.head!=None:
            while current.next != None:
                if current.value == valueSearched:
                    print ("true")
                    return True

                current = current.next
            print ("false")
            return False
        else:
            print ("Empty")
            return ("Empty")
    def reorderlost(self,head) :
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second =slow.next
        prev=slow.next  =None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp

        first,second=head,prev
        while second:
            tmp1,tmp2=first.next,second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1,tmp2
    def remove_middle(self):
      current=self.head
      if current==None:
        return
      while current.next != None:
        count=0
        current=current.next
        count=count+1

      while current.next !=None:
        mid=count//2
        for i in range (mid):
          current=current.next
        node=current





    def removeDuplicates(self):
        current = self.head
        if current == None:
            return
        while current.next:
            if current.value == current.next.value:
                temp=current.next
                new = temp.next
                current.next = new
                temp=None

            else:
                current = current.next






            # ptr2 = current

            # while (ptr2.next != None):

            #     if (current.value == ptr2.next.value):

            #         ptr2.next = ptr2.next.next
            #     else:
            #         ptr2 = ptr2.next

            # current = current.next




    @classmethod
    def countering(cls):
        """
        method to count the number of values added
        """
        return cls.counter



    def kthFromEnd(self, k):
        """
        This method is to return the value of a given index start counting the index from tail
        """
        current = self.head
        length = 0
        while current != None:
            current = current.next
            length += 1

        if k <0:
            print ("Please input positive numbers")
            return ("Please input positive numbers")

        if k > length:

            print('k is greater than the length of the linked list')
            return ('k is greater than the length of the linked list')
        current = self.head

        for i in range(length - k -1):
            current = current.next
        # print(current.value)
        return(current.value)

    def reverse_list(self):
         prev,current=None,self.head
         while current:
             next=current.next
             current.next=prev
             prev=current
             current=next
         self.head=prev

    def palindrom(self):
        fast=self.head
        current=self.head

        while fast and fast.next:
            fast=fast.next.next
            current=current.next
        prev=None
        while current:
             following=current.next
             current.next=prev
             prev=current
             current=following

        left,right=self.head,prev
        while right:
            if left.value!=right.value:
                return False

            left=left.next
            right=right.next
        return True




def mergeLists(head1, head2):

    current = None

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.value <= head2.value:

        current = head1

        current.next = mergeLists(head1.next, head2)

    else:
        current = head2

        current.next = mergeLists(head1, head2.next)

    return current


def zipLists(list1,list2):
        current1 = list1.head
        current2 = list2.head
        if not current1 and not current2:
            print("The two lists are empty")
            return 'The two lists are empty'
        elif  not current1 :
            print("The first list is empty")

            return (list2)
        elif not current2:
            print("The second list is empty")

            return (list1)
        while current1!=None and current2!=None:

            if current2:
                current = current1.next
                current1.next = current2
                current1 = current
            if current1:
                current = current2.next
                current2.next = current1
                current2 = current


if __name__ == '__main__':

    ll1 = LinkedList()


    ll1.append(1)
    ll1.append(1)
    ll1.append(1)
    ll1.append(5)
    ll1.append(5)
    print(ll1.deleteNode(1))








    # ll1.removeDuplicates()







    # print(ll1)
    # ll1.mergTwoList(ll1,ll2)
    # ll1.deleteNodepos(3)
    # ll1.reorderlost(ll1.head)
    # print(ll1.palindrom())
    # ll2.append(5)
    # print(ll1.kthFromEnd(0))
    # print(zipLists(ll1,ll2))
    print(ll1)





