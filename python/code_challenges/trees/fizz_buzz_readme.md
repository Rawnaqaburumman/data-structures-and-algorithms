# Challenge Summary

<!-- Description of the challenge -->

Conduct “FizzBuzz” on a k-ary tree while traversing through it to create a new tree.
Set the values of each of the new nodes depending on the corresponding node value in the source tree.

## Whiteboard Process
![](fizz_buzz.PNG)

<!-- Embedded whiteboard image -->

## Approach & Efficiency

define fizzBuzz function (KAryTree)
define traverse (node)

loop over the children then traverse(node.child[i])

if value node.child[i] % 5 and %3 = 0 , value = FizzBuzz

if value node.child[i] % 5 , value = Buzz
if value node.child[i] % 3 , value = fizz

else value node.child[i] % 3 , value = same value as string.

traverse (KAryTree.root)
then we repeat the steps for tree.root and return tree.

The Efficiency of the Big O time is O(n) The Efficiency of the Big O space is O(n)

## Solution
In tests folder follow the test_fizz_buzz_tree.py
function called fizz_buzz_tree
Arguments: k-ary tree
Return: new k-ary tree
