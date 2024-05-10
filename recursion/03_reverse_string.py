
def reverse_string(input, index=0):
    """
    Return reversed input string
    
    Examples:
       reverse_string("abc") returns "cba"
    
    Args:
      input(str): string to be reversed
    
    Returns:
      a string that is the reverse of input
    """

    if len(input) - index == 0:
        return ""
    
    return input[len(input) - index - 1] + reverse_string(input, index + 1)

# Test Cases
if __name__ == "__main__":
    print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")
    print ("Pass" if  ("" == reverse_string("")) else "Fail")