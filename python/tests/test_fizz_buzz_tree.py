from code_challenges.trees.fizz_buzz_tree import *
import pytest

def test_fizz_buzz_expected_output(tree):
    actual = fizz_buzz_tree(breadth_first(tree))
    expected = ['2', '7', 'Fizz', '2', 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz', '4']
    assert actual == expected


def test_fizz_buzz_fail():

    actual = fizz_buzz_tree(breadth_first(tree))
    expected = "Tree is Empty"
    assert actual == expected


@pytest.fixture
def tree():
    k_tree=BinaryTree()
    k_tree.root=Node(17)
    k_tree.root.left=Node(5)
    k_tree.root.center=Node(6)
    k_tree.root.right=Node(10)
    k_tree.root.left.left=Node(12)
    k_tree.root.left.right=Node(15)
    k_tree.root.right.left=Node(30)
    return k_tree
