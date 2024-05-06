"""
If a loop exists in the list, the fast runner will eventually move behind the slow runner as it moves to the 
beginning of the loop. Eventually it will catch up to the slow runner and both runners will be pointing to the 
same node at the same time. If this happens then there is a loop in the linked list.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

def iscircular(linked_list):
    """
    Determine wether the Linked List is circular or not

    Args:
        linked_list(obj): Linked List to be checked
    Returns:
        bool: Return True if the linked list is circular, return False otherwise
    """

    # TODO: Write function to check if linked list is circular
    if linked_list.head:
        slow_pointer = linked_list.head
        fast_pointer = linked_list.head.next

        while slow_pointer and fast_pointer:
            if slow_pointer == fast_pointer:
                return True
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

    return False

# Test case
if __name__ == "__main__":
    list_with_loop = LinkedList([2, -1, 3, 0, 5])

    # Creating a loop where the last node points back to the second node
    loop_start = list_with_loop.head.next

    node = list_with_loop.head
    while node.next: 
        node = node.next   
    node.next = loop_start

    # Test Cases
    small_loop = LinkedList([0])
    small_loop.head.next = small_loop.head
    print ("Pass" if iscircular(list_with_loop) else "Fail")
    print ("Pass" if not iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")
    print ("Pass" if not iscircular(LinkedList([1])) else "Fail")
    print ("Pass" if iscircular(small_loop) else "Fail")
    print ("Pass" if not iscircular(LinkedList([])) else "Fail")
