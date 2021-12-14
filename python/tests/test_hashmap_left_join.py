from code_challenges.hashmap_left_join.hashmap_left_join import left_join
from code_challenges.hashmap_left_join.hashtable import HashTable


def test_left_join():
    hashtable = HashTable()
    hashtable.add('fond',"enamored")
    hashtable.add('wrath', "anger")
    hashtable.add('diligent', 'employed')
    hashtable.add('outifit', 'grab')
    hashtable.add('guide', 'usher')

    hashtable2 = HashTable()
    hashtable2.add('fond', 'averse')
    hashtable2.add('wrath', 'delight')
    hashtable2.add('diligent', 'idle')
    hashtable2.add('guide', 'follow')
    hashtable2.add('flow', 'jam')

    expected=left_join(hashtable,hashtable2)
    actual=[['diligent', 'employed', 'idle'], ['outifit', 'grab', 'None'], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight']]
    assert expected==actual



def test_only_left_join():
    hashtable = HashTable()
    hashtable.add('fond',"enamored")
    hashtable.add('wrath', "anger")
    hashtable.add('diligent', 'employed')
    hashtable.add('outifit', 'grab')
    hashtable.add('guide', 'usher')

    hashtable2 = HashTable()

    expected=left_join(hashtable,hashtable2)
    actual=[['diligent', 'employed', 'None'], ['outifit', 'grab', 'None'], ['fond', 'enamored', 'None'], ['guide', 'usher', 'None'], ['wrath', 'anger', 'None']]
    assert expected==actual



