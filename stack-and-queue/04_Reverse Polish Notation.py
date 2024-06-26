"""
**Reverse Polish notation**, also referred to as **Polish postfix notation** is a way of laying out operators and operands. 

When making mathematical expressions, we typically put arithmetic operators (like `+`, `-`, `*`, and `/`) *between* operands. 
For example: `5 + 7 - 3 * 8`

However, in Reverse Polish Notation, the operators come *after* the operands. For example: `3 1 + 4 *`

The above expression would be evaluated as `(3 + 1) * 4 = 16`
"""

class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    operator = ("+", "-", "*", "/")
    stack = Stack()
    value = 0

    for item in input_list:
        if item not in operator:
            stack.push(int(item))
        else:
            a = stack.pop()
            b = stack.pop()
            if item == "+":
                stack.push(b + a)
            elif item == "-":
                stack.push(b - a)
            elif item == "*":
                stack.push(b * a)
            else:
                stack.push(int(b / a))
            
    return stack.pop()

## Test cases
if __name__ == "__main__":
    def test_function(test_case):
        output = evaluate_post_fix(test_case[0])
        print(output)
        if output == test_case[1]:
            print("Pass")
        else:
            print("Fail")

    test_case_1 = [["3", "1", "+", "4", "*"], 16]
    test_case_2 = [["4", "13", "5", "/", "+"], 6]
    test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
    test_function(test_case_1)
    test_function(test_case_2)
    test_function(test_case_3)