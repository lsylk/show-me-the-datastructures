"""
Problem 1: Square Root of an Integer

In this problem, you need to find the square root of a given integer without using 
any Python libraries. You should return the floor value of the square root.

Below is a function signature that serves as a starting point for your implementation. 
Your task is to complete the body of the function. Additionally, some test cases are 
provided to help you verify the correctness of your implementation. If necessary, add 
test cases to verify that your algorithm is working properly.

The expected time complexity is O(log(n)).
"""

def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number

    Args:
    number(int): Number to find the floored square root

    Returns:
    int: Floored square root
    """
    assert number >= 0, "Negative roots are invalid"
    if number == 0 or number == 1:
        return number
    est = number // 2
    while not (est ** 2 >= number and (est-1) ** 2 < number):
        adjust = est // 2 if est // 2 > 0 else 1
        est = est + (adjust if est ** 2 <= number else -adjust)
    return est - 1 if number - est**2 < 0 else est
    
    # if est*est > number:
    #     est -= adjust 
    # else:
    #     est += adjust
     
    # root = 0
    # est = number
    # while est > 0:
    #     root += 1
    #     est -= 2 * root - 1
    # return root-1 if est < 0 else root

if __name__ == "__main__":
    # Test cases
    print("Pass" if 3 == sqrt(9) else "Fail")   # Expected Output: Pass
    print("Pass" if 0 == sqrt(0) else "Fail")   # Expected Output: Pass
    print("Pass" if 4 == sqrt(16) else "Fail")  # Expected Output: Pass
    print("Pass" if 1 == sqrt(1) else "Fail")   # Expected Output: Pass
    print("Pass" if 5 == sqrt(27) else "Fail")  # Expected Output: Pass
    print("Pass" if 5 == sqrt(27) else "Fail")  # Expected Output: Pass
    print("Pass" if 32 == sqrt(1024) else "Fail")  # Expected Output: Pass
    try:
        sqrt(-4)
    except AssertionError as err:
        assert repr(err) == "AssertionError('Negative roots are invalid')"
        print("Pass assertion")
