class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])
    
    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
        linked_list(obj): Linked List to be reversed
        Modify the original linked list in place
    """
    prev = None
    current = linked_list.head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    linked_list.head = prev

if __name__ == "__main__":
    llist = LinkedList()
    for value in [4,2,5,1,-3,0]:
        llist.append(value)

    reverse(llist)
    print("Pass" if llist.to_list() == list([0,-3,1,5,2,4]) else "Fail")