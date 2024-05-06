"""
Implement a linked list class:
    + Append data to the tail of the list and prepend to the head
    + Search the linked list for a value and return the node
    + Remove a node
    + Pop, which means to return the first node's value and delete the node from the list
    + Insert data at some position in the list
    + Return the size (length) of the linked list
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        if self.head is None:
            self.head = Node(value)
            return
             
        second = self.head
        self.head = Node(value)
        self.head.next = second

    def append(self, value):
        """ Append a value to the end of the list. """
        if self.head is None:
            self.head = Node(value)
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(value)

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        if self.head is None:
            return None
        
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next

        raise ValueError("Value not found in the list.")

    def remove(self, value):
        """ Remove first occurrence of value. """
        current = self.head
        previous = None

        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
        
        raise ValueError("Value not found in the list.")

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        return None


    def insert(self, value, pos):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list. """
        size = self.size()
        if pos >= size:
            self.append(value)
        elif pos == 0:
            self.prepend(value)
        else:
            current = self.head
            previous = None
            count = 0
            while count != pos:
                previous = current
                current = current.next
                count += 1
            new = Node(value)
            previous.next = new
            new.next = current

    def size(self):
        """ Return the size or length of the linked list. """
        i = 0
        current = self.head
        while current:
            i += 1
            current = current.next
        return i

    def to_list(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.value)
            current = current.next
        return items

## Test implementation
if __name__ == "__main__":

    # Test prepend
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    linked_list.prepend(2)
    assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
        
    # Test append
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

    # Test search
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
    assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

    # Test remove
    linked_list.remove(1)
    assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
    linked_list.remove(3)
    assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"

    # Test pop
    value = linked_list.pop()
    assert value == 2, f"list contents: {linked_list.to_list()}"
    assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"

    # Test insert 
    linked_list.insert(5, 0)
    assert linked_list.to_list() == [5, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(2, 1)
    assert linked_list.to_list() == [5, 2, 1, 4], f"list contents: {linked_list.to_list()}"
    linked_list.insert(3, 6)
    assert linked_list.to_list() == [5, 2, 1, 4, 3], f"list contents: {linked_list.to_list()}"

    # Test size
    assert linked_list.size() == 5, f"list contents: {linked_list.to_list()}"

    print("Pass all")