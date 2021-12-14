# Singly Linked List
- Like arrays, Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2013/03/Linkedlist.png)
    
##### Why Linked List? 
- Arrays can be used to store linear data of similar types, but arrays have the following limitations. 
1. The size of the arrays is fixed: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage. 
2. Inserting a new element in an array of elements is expensive because the room has to be created for the new elements and to create room existing elements have to be shifted. 
## Challenge
- Create a Linked List class Within your Linked List class, include a head property. Upon instantiation, an empty Linked List should be created. The class should contain the following methods
- insert
1. Arguments: value
2. Returns: nothing
3. Adds a new node with that value to the head of the list with an O(1) Time performance.
- includes
1. Arguments: value
2. Returns: Boolean
3. Indicates whether that value exists as a Node’s value somewhere within the list.
- to string
1. Arguments: none
2. Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
### Write tests to prove the following functionality:

- Can successfully instantiate an empty linked list
- Can properly insert into the linked list
- The head property will properly point to the first node in the linked list
- Can properly insert multiple nodes into the linked list
- Will return true when finding a value within the linked list that exists
- Will return false when searching for a value in the linked list that does not exist
- Can properly return a collection of all the values that exist in the linked list
## Approach & Efficiency
- approaching the code using algorithemes and is efficient as a test results are shown.
- Cost of accessing an element: O(n)

## API
- insert : add a new value in the begining of linked List.
- includes : search about the values if its in the linked list or no .
- to string: Returns: a string representing all the values in the Linked List, formatted as:
`` "{ a } -> { b } -> { c } -> NULL" ``
