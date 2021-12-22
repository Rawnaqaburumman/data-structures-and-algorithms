from code_challenges.hashmap_left_join.hashtable import HashTable
def left_join(hash1 , hash2):
  
    array = []
    for i in hash1.map:
        if i:
            array.append(i)
    for i in range(len(array)):
        hashed = hash2.hash(array[i][0])
        if hash2.contains(array[i][0]):
            array[i].append(hash2.map[hashed][1])
        else:
            array[i].append("None")
    return array
if __name__ == "__main__":
    hash_table1 = HashTable()
    hash_table1.add("fond", "enamored")
    hash_table1.add("wrath", "anger")
    hash_table1.add("diligent", "employed")
    hash_table1.add("outfit", "grap")
    hash_table1.add("guide", "usher")
    hash_table2 = HashTable()
    hash_table2.add("fond", "averse")
    hash_table2.add("wrath", "delight")
    hash_table2.add("diligent", "idle")
    hash_table2.add("guide", "follow")
    hash_table2.add("flow", "jam")
    print(left_join(hash_table1 , hash_table2))
