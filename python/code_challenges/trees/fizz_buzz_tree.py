class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.center=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def pre_order(self, root,output=[]):
        output.append(root.value)
        if root.left is not None:
            self.pre_order(root.left,output)
        if root.right is not None:
            self.pre_order(root.right,output)
        return output
    def in_order(self,root,output=[]):
        if root.left is not None:
            self.in_order(root.left,output)
        output.append(root.value)
        if root.right is not None:
            self.in_order(root.right,output)
        return output
    def post_order(self, root,output=[]):
        if root.left is not None:
            self.in_order(root.left,output)
        if root.right is not None:
            self.in_order(root.right,output)
        output.append(root.value)
        return output
class Node1:
    def __init__(self,value):
       self.value=value
       self.next=None
class Queue():
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self, value):
        node=Node1(value)
        if not self.rear:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
    def dequeue(self):
        if not self.front:
          raise Exception ('This Queue is Empty')
        if self.rear==self.front:
            temp = self.front
            self.rear =  None
            self.front = None
            return temp.value
        temp=self.front
        self.front=self.front.next
        temp.next=None
        return temp.value
    def peek(self):
        if self.isEmpty():
            return ('This Queue is Empty')
        else:
            return self.front.value
    def isEmpty(self):
        return self.front == None
def breadth_first(tree):
    output=[]
    queue=Queue()
    if tree.root is None:
        return 'this tree is empty'
    queue.enqueue(tree.root)

    while not queue.isEmpty():
        start=queue.dequeue()
        output.append(start.value)
        if start.left:
            queue.enqueue(start.left)
        if start.center:
            queue.enqueue(start.center)
        if start.right:
            queue.enqueue(start.right)
    return output
def fizz_buzz_tree(node):
    new=[]
    for i in node:

        if int(i) % 3 == 0 and int(i) % 5 == 0:
           new.append('FizzBuzz')

        elif int(i) %3 == 0:
            new.append('Fizz')

        elif int(i) % 5 == 0:
            new.append('Buzz')

        else:
            new.append(str(int(i)))

    return new
# if __name__=='__main__':
#        k_tree=BinaryTree()
#        k_tree.root=Node(17)
#        k_tree.root.left=Node(5)
#        k_tree.root.center=Node(6)
#        k_tree.root.right=Node(10)
#        k_tree.root.left.left=Node(12)
#        k_tree.root.left.right=Node(15)
#        k_tree.root.right.left=Node(30)
#        print (fizzBuzz(breadth_first(k_tree)))

