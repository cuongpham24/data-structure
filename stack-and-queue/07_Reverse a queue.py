"""
Reverse a linked-list queue using a stack
"""

# Linked list node class
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# Queue class
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
            self.tail.next = Node(value)
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
        return self.num_elements == 0

    def is_empty(self):
        return self.size() == 0

# Stack class
class Stack():
    def __init__(self):
        self.head = None
        self.num_element = 0

    # Add to the front of the stack
    def push(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            prev_head = self.head
            self.head = Node(value)
            self.head.next = prev_head

        self.num_element += 1

    def pop(self):
        if self.is_empty():
            return None
        
        value = self.head.value
        self.head = self.head.next
        self.num_element += 1
        return value

    def top(self):
        return self.head.value if self.head else None
    
    def size(self):
        return self.num_element

    def is_empty(self):
        return self.num_element == 0


def reverse_queue(queue):
    """
    Reverese the input queue

    Args:
       queue(queue): Queue to be reversed
    Returns:
       queue: Reveresed queue
    """
    if queue is None:
        return None
    
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())
    return stack

## Test code
if __name__ == "__main__":
    def test_function(test_case):
        queue = Queue()
        for num in test_case:
            queue.enqueue(num)
        
        reverse_queue(queue)
        index = len(test_case) - 1
        while not queue.is_empty():
            removed = queue.dequeue()
            if removed != test_case[index]:
                print("Fail")
                return
            else:
                index -= 1
        print("Pass")
        
    test_case_1 = [1, 2, 3, 4]
    test_function(test_case_1)

    test_case_2 = [1]
    test_function(test_case_2)