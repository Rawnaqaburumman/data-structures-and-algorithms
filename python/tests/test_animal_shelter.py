from code_challenges.stack_and_queue.animal_shelter import *
import pytest




def test_multiple_dog_enqueue():
    dog1 = Dog("dog1")
    dog2 = Dog("dog2")
    dog3 =Dog("dog3")
    shelter= AnimalShelter()
    shelter.enqueue(dog1)
    shelter.enqueue(dog2)
    shelter.enqueue(dog3)
    expected = "front -> {dog1} -> {dog2} -> {dog3} -> Null"
    actual =  str(shelter.dog)
    assert actual == expected


def test_multiple_cat_enqueue():
    cat1 = Cat("cat1")
    cat2= Cat("cat2")
    cat3 =Cat("cat3")
    shelter= AnimalShelter()
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    shelter.enqueue(cat3)
    expected = 'front -> {cat1} -> {cat2} -> {cat3} -> Null'
    actual =str(shelter.cat)
    assert actual == expected


def test_dequeue_cat_or_dogs():
    cat1 = Cat("cat1")
    cat2= Cat("cat2")
    cat3 =Cat("cat3")
    shelter= AnimalShelter()
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    shelter.enqueue(cat3)
    shelter.dequeue("cat")
    actual= str(shelter.cat)
    excepted = "front -> {cat2} -> {cat3} -> Null"
    assert actual==excepted


def test_enqueue_other_kinds():
    lion=OtherAnimals("lion")
    mouse=OtherAnimals("mouse")
    shelter= AnimalShelter()
    shelter.enqueue(lion)
    actual= shelter.otherAnimals
    actual= str(shelter.otherAnimals)
    excepted="Not cat or dog/empty stack"
    assert actual == excepted

def test_dequeue_other_types():

    lion=OtherAnimals("lion")
    mouse=OtherAnimals("mouse")
    shelter= AnimalShelter()
    shelter.enqueue(lion)
    shelter.enqueue(lion)
    actual=shelter.enqueue(lion)
    excepted = None
    assert actual == excepted


