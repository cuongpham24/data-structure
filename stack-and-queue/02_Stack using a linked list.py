## Define a Node class
class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

## Create the Stack class
class Stack():
    def __init__(self):
        self.head = None
        self.num_elements = 0

    # Add elements to the top of the stack
    def push(self, value):
        # Create a new node
        node = Node(value)
        # Add connection to the front 
        if self.head is not None:
            node.next = self.head
            self.head = node
        else:
            self.head = node
        # Increase element count
        self.num_elements += 1

    # Take out the top element
    def pop(self):
        # If the stack is empty return none
        if self.num_elements == 0:
            return None
        # Update connect to the following node
        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return value
    
    # Get the current size of the stack
    def size(self):
        return self.num_elements
    
    # Check if the stack is empty
    def is_empty(self):
        return self.num_elements == 0
    
## Test code
if __name__ == "__main__":
    # Setup
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    # Test size
    print("Pass" if (stack.size() == 5) else "Fail")

    # Test pop
    print("Pass" if (stack.pop() == 50) else "Fail")

    # Test push
    stack.push(60)
    print("Pass" if (stack.pop() == 60) else "Fail")
    print("Pass" if (stack.pop() == 40) else "Fail")
    print("Pass" if (stack.pop() == 30) else "Fail")
    stack.push(50)
    print("Pass" if (stack.size() == 3) else "Fail")