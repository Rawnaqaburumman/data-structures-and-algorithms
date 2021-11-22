
class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


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


    def max_number(self):

        if not self.root:
                return "Tree is Empty"

        self.max=self.root.value
        def tree(node):
            if node.value>self.max:
                self.max=node.value
            if node.left:
                tree(node.left)
            if node.right:
                tree(node.right)
            return self.max

        return tree(self.root)


class  Binary_Search (BinaryTree) :

    def add(self,value) :
        if self.root:
            def traverse(root):
                if value < root.value:
                    if root.left is None :
                        root.left=Node(value)
                        return

                    else:
                        traverse(root.left)

                else :
                    if root.right is None :
                        root.right=Node(value)
                        return
                    else :
                        traverse(root.right)

            return traverse(self.root)
        else:
            self.root=Node(value)





    def contains(self,value):
        if not self.root:
            return False
        def traverse(root):
            if root:
                if root.value == value:
                    return True
                if traverse(root.left):
                    return True
                if traverse(root.right):
                    return True
            return False
        return traverse(self.root)



#========================================================================================
if __name__ == "__main__":
    node1 = Node(1)
    node1.left = Node(2)
    node1.right = Node(3)
    node1.left.left = Node(4)
    node1.left.right = Node(5)
    binarytree = BinaryTree(node1)
    print(binarytree.pre_order())  #1, 2, 4, 5, 3
    print (binarytree.in_order()) #4, 2, 5, 1, 3
    print (binarytree.post_order(node1)) #4, 5, 2, 3, 1
    print(binarytree.max_number())







