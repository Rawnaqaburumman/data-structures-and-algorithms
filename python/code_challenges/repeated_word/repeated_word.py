# from hashtable.hashtable import HashTable


class Node:

   def __init__(self,value):
       self.value=value
       self.next=None


class LinkedList:

    def __init__(self):
        self.head=None


    def append(self,value):

        node = Node(value)

        if self.head is None:
            self.head = node

        else:
            current = self.head

            while current.next != None:
                current = current.next
            current.next = node

    def __str__(self):

        result = ""

        if self.head is None:
            result += None

        else:
            current = self.head

            while(current):
                result +=str(current.value)+" -> "
                current = current.next
            result += "NULL"
            return result

class HashTable:
    """
    HashTable Class to  initialize the array size
    """
    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * self.size
        # self.key=""

    def hash(self,key):
        """
        a function to get the hash value of the key in ascii code
        """
        ascii_sum=0
        for char in key:
            ascii_sum+=ord(char)
        return ascii_sum*11 % self.size

    def add(self, key, value):

        hashed_key = self.hash(key)
        if not self.map[hashed_key]:
            self.map[hashed_key] = [key,value]
            # self.key = [key,value]
            return [key,value]
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].append([key,value])
                return [key,value]
            else:
                chain = LinkedList()
                # existing_pair = self.key
                existing_pair= self.map[hashed_key]
                new_pair =[key,value]
                self.map[hashed_key]=chain
                chain.append((existing_pair))
                chain.append(new_pair)
                return new_pair
        # if type(  self.map[hashed_key])== list:
        #      self.map[hashed_key]= self.map[hashed_key][1]

    def get(self, key):
        hashed_key=self.hash(key)
        if  self.map[hashed_key]==None:
              print("Not Found")
              return None
        else:
            if type(  self.map[hashed_key])== list:
                print(self.map[hashed_key][1])
                return self.map[hashed_key][1]

            else:
                current =  self.map[hashed_key].head
            if current!=None:
                while current.next != None:
                    if current.value[0] == key:
                        print (current.value[1])
                        return (current.value[1])
                    current = current.next

    def contains(self, key):
        hashed_key=self.hash(key)
        if  self.map[hashed_key]==None:
            return False
        else:
            if type(  self.map[hashed_key])== list:
                print (True)
                return True
            else:
                current =  self.map[hashed_key].head
            if current!=None:
                while current.next != None:
                    if current.value[0] == key:
                        print (True)
                        return (True)
                    current = current.next
                print ("false")
                return False


#====================Repeated Words ===================================================

def repeated_word(string):
    """
    a function called repeated word that finds the first word to occur more than once in a string
    """
    if not string:
        return "not a string"

    hashed_word = HashTable()
    string = string.replace('.',' ')
    string = string.replace(',',' ')


    splited_words = string.lower().split()
    for string in splited_words:
        if hashed_word.contains(string):
            return string
        else:
            hashed_word.add(string,string)
    return 'no repeated'
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
