# Stacks and Queues
### What is a Stack
![](https://4cawmi2va33i3w6dek1d7y1m-wpengine.netdna-ssl.com/wp-content/uploads/2018/07/Computer-science-fundamentals_6.1.png)
A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.
#### Stacks follow these concepts:

FILO ::: First In Last Out
### What is a Queue
#### Common terminology for a queue is

- Enqueue - Nodes or items that are added to the queue.
- Dequeue - Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.
- Front - This is the front/first Node of the queue.
- Rear - This is the rear/last Node of the queue.
- Peek - When you peek you will view the value of the front Node in the queue. If called when the queue is empty an exception will be raised.
- IsEmpty - returns true when queue is empty otherwise returns false.
#### Queues follow these concepts:

- FIFO ::: First In First Out

## Challenge
##### using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

- Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
- Stack
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
- This object should be aware of a default empty value assigned to top when the stack is created.
- The class should contain the following methods:
###### push
- Arguments: value
- adds a new node with that value to the top of the stack with an O(1) Time performance.
###### pop
- Arguments: none
- Returns: the value from node from the top of the stack
- Removes the node from the top of the stack
- Should raise exception when called on empty stack
###### peek
- Arguments: none
- Returns: Value of the node located at the top of the stack
- Should raise exception when called on empty stack
###### is empty
- Arguments: none
- Returns: Boolean indicating whether or not the stack is empty.
#### Queue
- Create a Queue class that has a front property. It creates an empty Queue when instantiated.
- This object should be aware of a default empty value assigned to front when the queue is created.
- The class should contain the following methods:
###### enqueue
- Arguments: value
- adds a new node with that value to the back of the queue with an O(1) Time performance.
###### dequeue
- Arguments: none
- Returns: the value from node from the front of the queue
- Removes the node from the front of the queue
- Should raise exception when called on empty queue
###### peek
- Arguments: none
- Returns: Value of the node located at the front of the queue
- Should raise exception when called on empty stack
###### is empty
- Arguments: none
- Returns: Boolean indicating whether or not the queue is empty
- You have access to the Node class and all the properties on the Linked List class.

## Approach & Efficiency
Most operation (Push,pop,enque,deque,peek) take  O(1) operation. This is because they take the same amount of time no matter how many Nodes (n) you have in the stack.

## API
###### push
- Arguments: value
- adds a new node with that value to the top of the stack with an O(1) Time performance.
###### pop
- Arguments: none
- Returns: the value from node from the top of the stack
- Removes the node from the top of the stack
- Should raise exception when called on empty stack
###### peek
- Arguments: none
- Returns: Value of the node located at the top of the stack
- Should raise exception when called on empty stack
- ###### enqueue
- Arguments: value
- adds a new node with that value to the back of the queue with an O(1) Time performance.
###### dequeue
- Arguments: none
- Returns: the value from node from the front of the queue
- Removes the node from the front of the queue
- Should raise exception when called on empty queue
###### peek
- Arguments: none
- Returns: Value of the node located at the front of the queue
- Should raise exception when called on empty stack
###### is empty
- Arguments: none
- Returns: Boolean indicating whether or not the queue is empty
- You have access to the Node class and all the properties on the Linked List class.
