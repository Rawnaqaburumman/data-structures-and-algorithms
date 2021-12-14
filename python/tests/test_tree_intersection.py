
from code_challenges.tree_intersection.tree_intersection import tree_intersection
from code_challenges.tree_intersection.trees import BinaryTree,Node
import pytest





def test_tree_intersection(tree_i):
    actual = tree_i
    expected=['1', '2']
    assert actual == expected

def test_tree_intersection_empty_tree():
    tree1=BinaryTree()
    tree2=BinaryTree()
    actual = tree_intersection(tree1,tree2)
    expected ="One or two of the trees are empty"
    assert actual == expected


@pytest.fixture()
def tree_i():
    tree1=BinaryTree()
    tree1.root=Node("1")
    tree1.root.left=Node("2")
    tree1.root.right=Node("3")
    tree1.root.left.left=Node("4")
    tree1.root.left.right=Node("5")
    tree1.root.right.left=Node("6")

    tree2=BinaryTree()
    tree2.root=Node("1")
    tree2.root.left=Node("2")
    tree2.root.right=Node("7")
    tree2.root.left.left=Node("8")
    tree2.root.left.right=Node("9")
    tree2.root.right.left=Node("44")

    return tree_intersection(tree1,tree2)
