"""
queue will need to have the following functionality:
1. `enqueue`  - adds data to the back of the queue
2. `dequeue`  - removes data from the front of the queue
3. `front`    - returns the element at the front of the queue
4. `size`     - returns the number of elements present in the queue
5. `is_empty` - returns `True` if there are no elements in the queue, and `False` otherwise
6. `_handle_full_capacity` - increases the capacity of the array, for cases in which the queue would otherwise overflow

Also, if the queue is empty, `dequeue` and `front` operations should return `None`.
"""

class Queue():
    def __init__(self):
        self.arr = [0 for _ in range(10)]
        self.next_index = 0
        self.front_index = 0
        self.queue_size = 0

    def enqueue(self, value):
        if self.next_index == len(self.arr):
            self._handle_full_capacity()
        
        self.arr[self.next_index] = value
        self.next_index += 1
        self.queue_size += 1

    def dequeue(self):
        if self.queue_size == 0:
            self.next_index = 0
            self.front_index = 0
            return None
        
        value = self.arr[self.front_index]
        self.arr[self.front_index] = 0
        self.front_index += 1
        self.queue_size -= 1
        return value

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        return self.front_index

    def _handle_full_capacity(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(len(old_arr) * 2)]
        for id, val in enumerate(old_arr):
            self.arr[id] = val

    def get_queue(self):
        return self.arr


## Test cases
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test size
    print("Pass" if (q.size() == 3) else "Fail")

    # Test dequeue
    print("Pass" if (q.dequeue() == 1) else "Fail")

    # Test enqueue
    q.enqueue(4)
    print("Pass" if (q.dequeue() == 2) else "Fail")
    print("Pass" if (q.dequeue() == 3) else "Fail")
    print("Pass" if (q.dequeue() == 4) else "Fail")
    q.enqueue(5)
    print("Pass" if (q.size() == 1) else "Fail")