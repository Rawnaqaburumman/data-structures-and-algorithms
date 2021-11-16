
# def test_multiple_cat_enqueue():
#     cat1 = Cat("cat1")
#     cat2= Cat("cat2")
#     cat3 =Cat("cat3")
#     shelter= AnimalShelter()
#     shelter.enqueue(cat1)
#     shelter.enqueue(cat2)
#     shelter.enqueue(cat3)
#     expected = 'front -> {cat1} -> {cat2} -> {cat3} -> Null'
#     actual =  print(shelter.cat)
#     assert actual == expected


# def test_dequeue_neither_dog_or_cat():
#     shelter= AnimalShelter()
#     expected = "Null"
#     actual= f"{shelter.dequeue('mouse')}"
#     assert actual == expected
