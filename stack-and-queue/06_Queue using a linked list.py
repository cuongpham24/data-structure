## Define a Node class
class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

## Define Queue class
class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        if self.num_elements == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            # Add data to the next node of the tail
            self.tail.next = Node(value)
            # Move the tail to the last node
            self.tail = self.tail.next
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements
        
    def is_empty(self):
        return self.num_elements == 0
    
    def to_list(self):
        cur_node = self.head
        items = []
        while cur_node:
            items.append(cur_node.value)
            cur_node = cur_node.next
        return items


## Test code
if __name__ == "__main__":
    # Setup
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.to_list())
    # Test size
    print ("Pass" if (q.size() == 3) else "Fail")

    # Test dequeue
    print ("Pass" if (q.dequeue() == 1) else "Fail")

    # Test enqueue
    q.enqueue(4)
    print ("Pass" if (q.dequeue() == 2) else "Fail")
    print ("Pass" if (q.dequeue() == 3) else "Fail")
    print ("Pass" if (q.dequeue() == 4) else "Fail")
    q.enqueue(5)
    print ("Pass" if (q.size() == 1) else "Fail")