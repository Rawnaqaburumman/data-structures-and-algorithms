from code_challenges.trees.trees import *

import pytest



def test_instance_an_empty_tree():
    tree = BinaryTree()
    assert isinstance(tree, BinaryTree)


def test_single_root_node():
    expected = 5
    value = Binary_Search(5)
    actual = value.root
    assert actual == expected




def test_add_left_and_right_child_to_single_root_node():
    expected = [2, 1, 3]
    node1 = Node(1)
    node1.left = Node(2)
    node1.right = Node(3)
    binary_tree = BinaryTree(node1)
    actual = binary_tree.in_order()
    assert actual == expected



def test_return_a_collection_preorder_traversal():
    node1 = Node(1)
    node1.left = Node(2)
    node1.right = Node(3)
    node1.left.left = Node(4)
    node1.left.right = Node(5)
    binary_tree = BinaryTree(node1)
    expected = [1, 2, 4, 5, 3]

    actual = binary_tree.pre_order()

    assert actual == expected




def test_return_a_collection_In_order_traversal():
    node1 = Node(1)
    node1.left = Node(2)
    node1.right = Node(3)
    node1.left.left = Node(4)
    node1.left.right = Node(5)
    binary_tree = BinaryTree(node1)
    expected = [4, 2, 5, 1, 3]

    actual = binary_tree.in_order()

    assert actual == expected




def test_return_a_collection_from_a_post_order_traversal():

    node1 = Node(1)
    node1.left = Node(2)
    node1.right = Node(3)
    node1.left.left = Node(4)
    node1.left.right = Node(5)
    binary_tree = BinaryTree(node1)
    expected = [4, 5, 2, 3, 1]

    actual = binary_tree.post_order(node1)

    assert actual == expected





def test_max_val():
    b_tree=Binary_Search()
    b_tree.root=Node(2)
    b_tree.root.left=Node(7)
    b_tree.root.left.left=Node(2)
    b_tree.root.left.right=Node(6)
    b_tree.root.left.right.left=Node(5)
    b_tree.root.left.right.left=Node(11)
    b_tree.root.right=Node(5)
    b_tree.root.right.right=Node(9)
    b_tree.root.right.right.left=Node(4)


    actual=b_tree.max_number()
    expected=11
    assert actual==expected


def test_max_empty_val():
    b_tree=Binary_Search()
    actual=b_tree.max_number()
    excepted="Tree is Empty"
    assert actual==excepted

