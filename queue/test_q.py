from q import *

def check_empty():
    q = Queue()
    assert q.is_empty()


def test_add():
    q = Queue()
    q.add("A")
    assert q.head.data == "A"
    q.add("B")
    assert q.head.data == "A"
    next_node = q.head.next
    assert next_node.data == "B"

def test_pop():
    q = Queue()
    q.add("A")
    assert q.head.data == "A"
    q.add("B")
    next_node = q.head.next
    assert next_node.data == "B"
    q.add("C")
    next_node = q.head.next.next
    assert next_node.data == "C"
    q.pop_left()
    q.add("D")
    next_node = q.head.next.next
    assert next_node.data == "D"
    
