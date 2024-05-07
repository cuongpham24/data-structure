"""
Using stacks to make sure the parentheses are balanced in mathematical expressions.

The function takes a string as an input and return `True` if it's parentheses are balanced or `False` if it is not. 
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()


def equation_checker(equation):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    stack = Stack()
    for char in equation:
        if char == "(":
            stack.push(1)
        elif char == ")":
            if stack.pop() == None:
                return False

    return stack.size() == 0

## Test code
if __name__ == "__main__":
    print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
    print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")