
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # adds a value to the end of the list
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        tail = self.head
        while tail.next:
            tail = tail.next
        
        tail.next = Node(value)
        return

    # Converts a linked list back into a Python list.
    def to_list(self):
        items = []
        node = self.head
        while node:
            items.append(node.value)
            node = node.next
        return items