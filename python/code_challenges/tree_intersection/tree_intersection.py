from code_challenges.tree_intersection.trees import BinaryTree,Node
from code_challenges.tree_intersection.hashtable import HashTable

def tree_intersection(tree1 , tree2):
    tree1 = tree1.pre_order()
    tree2 = tree2.pre_order()

    if len(tree1)==0 or len(tree2)==0 :
        return "One or two of the trees are empty"

    h_table = HashTable()
    output = []

    for node in tree1:

        h_table.add(node,node)


    for node in tree2:

        if h_table.contains(node):
            output.append(node)
        h_table.add(node,node)


    return output


if __name__ == "__main__":
    tree1=BinaryTree()
    tree1.root=Node("A")
    tree1.root.left=Node("B")
    tree1.root.right=Node("C")
    tree1.root.left.left=Node("D")
    tree1.root.left.right=Node("E")
    tree1.root.right.left=Node("F")

    tree2=BinaryTree()
    tree2.root=Node("A")
    tree2.root.left=Node("B")
    tree2.root.right=Node("k")
    tree2.root.left.left=Node("r")
    tree2.root.left.right=Node("x")
    tree2.root.right.left=Node("m")

    print(tree_intersection(tree1,tree2))
