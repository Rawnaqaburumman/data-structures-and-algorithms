from code_challenges.hashtable.hashtable import *

def test_add():
    hashtable = HashTable()
    actual=hashtable.add('ahmad', 30)
    expected=['ahmad', 30]
    assert actual==expected

def test_get():
    hashtable = HashTable()
    hashtable.add('leena', 24)
    actual=hashtable.get('leena')
    expected=24
    assert actual==expected

def test_contain():
    hashtable = HashTable()
    hashtable.add('leena', 24)
    actual=hashtable.contains('leena')
    expected=True
    assert actual==expected

def test_get_None_contain():
    hashtable = HashTable()
    hashtable.add('leena', 24)
    actual=hashtable.get('mana')
    expected=None
    assert actual==expected

def test_None_contain():
    hashtable = HashTable()
    hashtable.add('leena', 24)
    actual=hashtable.contains('mana')
    expected=False
    assert actual==expected

def test_hashtable_collision_get():
    new_hashtable = HashTable()
    new_hashtable.add('ahmad', 20)
    new_hashtable.add('hamad', 30)

    actual = new_hashtable.get('ahmad')
    expected = 20
    assert actual == expected

def test_hashtable_collision_contain():
    hashtable = HashTable()
    hashtable.add('ahmad', 20)
    hashtable.add('hamad', 30)

    actual = hashtable.contains('ahmad')
    expected =True
    assert actual == expected

def test_the_hash_size():
    hashtable = HashTable()

    assert 0<=hashtable.hash("leena")<=1024
