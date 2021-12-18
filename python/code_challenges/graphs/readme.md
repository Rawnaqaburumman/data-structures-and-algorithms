# Graphs

a graph is an abstract data type that is meant to implement the undirected graph and directed graph concepts from the field of graph theory within mathematics.

## Challenge

create a graph class to Implement methods in how to add node , add edge , get nodes , get neighbors , size .

## Approach & Efficiency

The Efficiency of the Big O time is O(n)

The Efficiency of the Big O space is O(1)

## API

### add node

    Arguments: value
    Returns: The added node
    Add a node to the graph

    The Efficiency of the Big O time is O(n)
    The Efficiency of the Big O space is O(1)

### add edge

    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing
    Adds a new edge between two nodes in the graph, If specified, assign a weight to the edge, Both nodes should already be in the Graph

    The Efficiency of the Big O time is O(n)
    The Efficiency of the Big O space is O(1)

### get nodes

    Arguments: none
    Returns all of the nodes in the graph as a collection (set, list, or similar)

    The Efficiency of the Big O time is O(n)
    The Efficiency of the Big O space is O(1)

### get neighbors

    Arguments: node
    Returns a collection of edges connected to the given node Include the weight of the connection in the returned collection

    The Efficiency of the Big O time is O(n)
    The Efficiency of the Big O space is O(1)

### size

    Arguments: none
    Returns the total number of nodes in the graph

    The Efficiency of the Big O time is O(n)
    The Efficiency of the Big O space is O(1)
