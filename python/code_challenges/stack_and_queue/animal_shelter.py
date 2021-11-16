class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class EmptyQueueException(Exception):
    pass
class Queue:
    """
  Queue Data structure
    """
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, value):
        node=Node(value)

        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node



    def __str__(self):
        output = "front -> "
        if self.front is None:
            output += "None"
            return "Not cat or dog/empty stack"
        else:
            current = self.front
            while(current):
                output += "{%s} -> "%(current.value)
                current = current.next
            output += "Null"
            return output


    def dequeue(self):
        if self.front == None:
              raise EmptyQueue("This stack is empty")
        else:

          temp=self.front
          self.front=self.front.next
          temp.next=None
          return temp.value

    def peek(self):

     if self.front:
      return self.front.value
     else:
            raise Emptyqueue("This queue is empty")

    def is_empty(self):
        return self.front == None


#====================Animal shelter==================================================================
#=====================Cat class==========================
class Cat():
    def __init__(self, name):
        self.name = name
        self.type = "cat"


#======================Dog class============================
class Dog():
    def __init__(self, name):
        self.name = name
        self.type = "dog"

#========================Other animals class ======================
class OtherAnimals():
    def __init__(self, name):
     self.name=name
     self.type="other_animals"

#=========================Animal shelter class ======================
class AnimalShelter() :
    """"
    This is an animal shelter class, This class depends on fifo principle to structure the data.it accept just
    two kinds of animals(Dog, cat) and reject others kinds.
    """


    def __init__(self,):
        self.cat=Queue()
        self.dog = Queue()
        self.otherAnimals=Queue()


    def enqueue(self,animal) :
        if animal.type== 'dog':
            self.dog.enqueue(animal.name)
        if animal.type== 'cat':
            self.cat.enqueue(animal.name)
        elif animal.type=="other_animals" :
             return None

    def dequeue(self, pref):
        if pref == "cat":
            self.cat.dequeue()
        elif pref == "dog":
            self.dog.dequeue()
        elif pref.type=="other_animals" :
             return None


if __name__ == "__main__":
    # dog1 = Dog("dog1")
    # dog2 = Dog("dog2")
    # dog3 =Dog("dog3")
    # cat1=Cat("cat1")
    # cat2=Cat("cat2")
    # cat3=Cat("cat3")
    # lion=OtherAnimals("lion")
    # mouse=OtherAnimals("mouse")
    # shelter= AnimalShelter()
    # shelter.enqueue(dog1)
    # shelter.enqueue(dog2)
    # shelter.enqueue(dog3)
    # shelter.enqueue(cat3)
    # shelter.enqueue(lion)





    # print(shelter.dog)
    # print(shelter.cat)
    # print(shelter.otherAnimals)
    # cat1=Cat("cat1")
    # cat2=Cat("cat2")
    # cat3=Cat("cat3")
    # lion=OtherAnimals("lion")
    # mouse=OtherAnimals("mouse")
    # shelter= AnimalShelter()
    # shelter.enqueue(cat1)
    # shelter.enqueue(cat2)

    # actual= shelter.otherAnimals
    # print(actual)


    # lion=OtherAnimals("lion")
    # mouse=OtherAnimals("mouse")
    # shelter= AnimalShelter()
    # shelter.enqueue(lion)
    # shelter.enqueue(lion)
    # print( shelter.enqueue(lion))

    cat1 = Cat("cat1")
    cat2= Cat("cat2")
    cat3 =Cat("cat3")
    shelter= AnimalShelter()
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    shelter.enqueue(cat3)
    shelter.dequeue("cat")
    print(shelter.cat)




    # # print(shelter)


    # shelter.dequeue('dog')
    # print(shelter.dog)
    # print(shelter.dequeue("lion"))

