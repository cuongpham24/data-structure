# List has connections backwards and forwards
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return
        
        self.tail = self.head
        while self.tail.next:
            self.tail = self.tail.next

        # Create a new node at the end
        self.tail.next = DoubleNode(value)
        # Connect the new backward pointer to the previous node
        self.tail.next.previous = self.tail
        # Move tail to the newly added
        self.tail = self.tail.next