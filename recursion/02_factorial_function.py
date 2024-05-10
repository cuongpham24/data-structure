"""
To use recursion to write a function that will take a number and return the factorial of that number.
"""

def factorial(n):
    """
    Calculate n!
    
    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

## Test case 
if __name__ == "__main__":
    print ("Pass" if (1 == factorial(0)) else "Fail")
    print ("Pass" if  (1 == factorial(1)) else "Fail")
    print ("Pass" if  (120 == factorial(5)) else "Fail")