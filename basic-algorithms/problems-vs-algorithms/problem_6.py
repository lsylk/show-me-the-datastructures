"""
Problem 6: Unsorted Integer Array

In this problem, we will look for smallest and largest integer from a list of 
unsorted integers. The code should run in O(n) time. Do not use Python's 
inbuilt functions to find min and max.

You should implement the function body according to the get_min_max function 
signature. Use the test cases provided below to verify that your algorithm is 
correct. If necessary, add additional test cases to verify that your algorithm 
works correctly.
"""

from typing import Optional

def get_min_max(ints: list[int]) -> Optional[tuple[int, int]]:
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
    ints (list[int]): list of integers containing one or more integers

    Returns:
    Optional[tuple[int, int]]: A tuple containing the minimum and maximum 
    integer, or None if the list is empty
    """
    if len(ints) == 0:
        return None
    result = (ints[0], ints[0])
    for num in ints:
        if num > result[1]:
            result = (result[0], num)
        elif num < result[0]:
            result = (num, result[1])
    return result

if __name__ == '__main__':
    # Edge case: Empty input list
    print(get_min_max([]))
    # Expected output: None

    # Normal case: list with negative and positive numbers
    print(get_min_max([-10, 0, 10, -20, 20]))
    # Expected output: (-20, 20)

    # Normal case: list with large range of numbers
    print(get_min_max([1000, -1000, 500, -500, 0]))
    # Expected output: (-1000, 1000)

    # Normal case: list with already sorted numbers
    print(get_min_max([1, 2, 3, 4, 5]))
    # Expected output: (1, 5)
