from code_challenges.trees.tree_breadth_first import *
import pytest
from pytest import raises
def test_breadth_first():

    node1 = Node(1)
    node1.left = Node(2)
    node1.right = Node(3)
    node1.left.left = Node(4)
    node1.left.right = Node(5)
    binary_tree = BinaryTree(node1)
    expected = [1,2,3,4,5]

    actual = breadth_first(binary_tree)

    assert actual == expected

    
def test_empty_tree():

  binary_treee = BinaryTree()

  excepted="its empty Tree"
  with pytest.raises(Exception):
        assert breadth_first(binary_treee)

