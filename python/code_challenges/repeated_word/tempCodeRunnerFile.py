if __name__ == '__main__':
    hashtable = HashTable()
    hashtable.add('ahmad', 30)
    hashtable.add('hamad', 29)
    hashtable.add('daham', 45)
    hashtable.add('load', 45)
    hashtable.add('doal', 49)
    hashtable.add('werw', 2549)
    hashtable.add('zaid', 24)
    hashtable.add('sultan', 24)
    hashtable.get('sultan')
    # hashtable.contains("werw")
    for hashed_key, item in enumerate(hashtable.map):
        if item:
            print(hashed_key, item)