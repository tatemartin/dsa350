import random

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def pop_left(self):
        if not self.head:
            return None
        current_head = self.head
        self.head = self.head.next
        self.size -= 1
        return current_head

    def add(self,item):
         new_node = Node(item)
         if not self.head:
             self.head = new_node
         else:
             current = self.head
             while current.next:
                 if not current.next:
                     break
                 current = current.next
             current.next = new_node
         self.size += 1

    def is_empty(self):
        return self.head is None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

class Student:
    def __init__(self,first,last,sid):
        self.first = first
        self.last = last
        self.sid = random.randint(1000, 9999)

    def __str__(self):
        return f"{self.first} {self.last}, {self.sid}"

jim = Student('jim','jack',1111)
joe = Student('joe','jack',1212)
jack = Student('jack','joe',2212)

print(jim)
print(joe)
print(jack)
        
waitlist = Queue()

waitlist.add(jim)
waitlist.add(joe)
waitlist.add(jack)

print("Waitlist")
for student in waitlist:
    print(student)

while not waitlist.is_empty():
    waitlist.pop_left()

    print("Waitlist now:")
    for student in waitlist:
        print(student)
