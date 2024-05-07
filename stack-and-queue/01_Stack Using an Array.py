"""
Implement a `Stack` class that has the following behaviors:

1. `push` - adds an item to the top of the stack
2. `pop` - removes an item from the top of the stack (and returns the value of that item)
3. `size` - returns the size of the stack
4. `top` - returns the value of the item at the top of stack (without removing that item)
5. `is_empty` - returns `True` if the stack is empty and `False` otherwise
"""

class Stack:
    def __init__(self, initial_size=10):
        self.arr = [0 for i in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, value):
        # Check stack size
        if self.next_index >= len(self.arr):
            self._handle_stack_capacity()

        self.arr[self.next_index] = value
        self.next_index += 1
        self.num_elements += 1

    def size(self):
        """Add a `size` method that returns the current size of the stack"""
        return self.num_elements
    
    def is_empty(self):
        """Add an `is_empty` method that returns `True` if the stack is empty and `False` otherwise"""
        return self.num_elements == 0
    
    def pop(self):
        if self.is_empty():
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.num_elements]

    def _handle_stack_capacity(self):
        """Add a method to expand the original array when it's full"""
        old_arr = self.arr
        self.arr = [0 for i in range(2 * len(old_arr))]
        for id, val in enumerate(old_arr):
            self.arr[id] = val


if __name__ == "__main__":
    foo = Stack()
    foo.push(1)
    foo.push(2)
    foo.push(3)
    foo.push(4)
    foo.push(5)
    foo.push(6)
    foo.push(7)
    foo.push(8)
    foo.push(9)
    foo.push(10) # The array is now at capacity!
    foo.push(11) # This one should cause the array to increase in size
    print(foo.arr) # Let's see what the array looks like now!
    print("Pass" if len(foo.arr) == 20 else "Fail") # If we successfully doubled the array size, it should now be 20.

    foo = Stack()
    print(foo.size()) # Should return 0
    print(foo.is_empty()) # Should return True
    foo.push("Test") # Let's push an item onto the stack and check again
    print(foo.size()) # Should return 1
    print(foo.is_empty()) # Should return False

    foo = Stack()
    foo.push("Test") # We first have to push an item so that we'll have something to pop
    print(foo.pop()) # Should return the popped item, which is "Test"
    print(foo.pop()) # Should return None, since there's nothing left in the stack