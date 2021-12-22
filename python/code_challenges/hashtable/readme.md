# Hashtables
Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. That makes accessing the data faster as the index value behaves as a key for the data value.

## Challenge
Hashing is a technique that is used to uniquely identify a specific object from a group of similar objects.

## Approach & Efficiency

The Efficiency of the Big O time is O(n)

The Efficiency of the Big O space is O(1)

## API

### hash

    Arguments: key
    Returns: Index in the collection for that key

### get

    Arguments: key
    Returns: Value associated with that key in the table

### add

    Arguments: key, value
    Returns: nothing
    This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

### contains

    Arguments: key
    Returns: Boolean, indicating if the key exists in the table already.
