
class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right




class Queue:
  def __init__(self, datalist=[]):
    self.data = datalist

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)


#=======================================================================================
class BinaryTree (Node) :
    def __init__(self,root=None):
        self.root=root

    def pre_order(self):
        output= []
        if self.root is None :
            raise Exception("its empty Tree")
        def traverse(root)  :
            output.append(root.value)

            if root.left :
                traverse(root.left )
            if root.right :
                traverse(root.right)

        traverse(self.root)
        return  (output )


    def in_order(self):
        output=[]
        if self.root is None :
            raise Exception("its empty Tree")
        def traverse(root):
            if root.left:
                traverse(root.left)
            output.append (root.value)

            if root.right:
                traverse(root.right)

        traverse (self.root)
        return (output )


    def post_order(self, root):
        output=[]
        if self.root is None :
            raise Exception("its empty Tree")
        def traverse(root):
            if root.left:
                traverse(root.left)


            if root.right:
                traverse(root.right)
            output.append (root.value)
        traverse (self.root)
        return (output )
#===============================================================================
def breadth_first(tree):
        print(tree.root)
        test_Queue=Queue()
        if tree.root is None :
         raise Exception("its empty Tree")
        test_Queue.enqueue(tree.root)
        list=[]
        while test_Queue.peek():
            front=test_Queue.dequeue()

            list.append(front.data)

            if front.left:
                  test_Queue.enqueue(front.left)

            if front.right:
                  test_Queue.enqueue(front.right)

        return list


if __name__=="__main__":
    node1 = Node(1)
    node1.left = Node(2)
    node1.right = Node(3)
    node1.left.left = Node(4)
    node1.left.right = Node(5)
    binarytree = BinaryTree(node1)

    print(breadth_first(binarytree))








