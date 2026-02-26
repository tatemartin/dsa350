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
          if self.head:
              return True

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
