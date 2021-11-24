from code_challenges.trees.fizz_buzz_tree import *
import pytest


@pytest.fixture
def data():

    tree2=BinaryTree()
    tree2.root=Node(19)
    tree2.root.left=Node(10)
    tree2.root.center=Node(3)
    tree2.root.right=Node(10)
    tree2.root.left.left=Node(12)
    tree2.root.left.right=Node(15)
    tree2.root.right.left=Node(30)
    return tree2






def test_all_cases(data):

    assert fizz_buzz_tree(breadth_first(data))==['19', 'Buzz', 'Fizz', 'Buzz', 'Fizz', 'FizzBuzz', 'FizzBuzz']

def test_empty_tree():
    tree2=BinaryTree()
    # tree2.root=Node()
    actual =breadth_first(tree2)
    expected='this tree is empty'
    assert actual == expected
