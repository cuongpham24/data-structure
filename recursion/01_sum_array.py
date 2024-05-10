"""
Recursive function to add all elements in an array
"""

def sum_array(arr, index=0):
    if len(arr) - 1 == index:
        return arr[index]
    
    return arr[index] + sum_array(arr, index + 1)

## Test code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(sum_array(arr))