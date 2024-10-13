"""
Problem 3: Rearrange Array Elements

Given an input array consisting on only 0, 1, and 2, sort the array in a single 
traversal. You're not allowed to use any sorting function that Python provides.

Note that O(n) does not necessarily mean single-traversal. For e.g. if you 
traverse the array twice, that would still be an O(n) solution but it will not 
count as single traversal.

You should implement the function body according to the sort_012 function 
signature. Use the test cases provided below to verify that your algorithm is 
correct. If necessary, add additional test cases to verify that your algorithm 
works correctly.
"""

def sort_012(input_list: list[int]) -> list[int]:
    """
    Sort an array consisting only of 0s, 1s, and 2s in a single traversal.

    This function uses the Dutch National Flag algorithm to sort the array in-place.

    Args:
    input_list (list[int]): A list of integers where each integer is either 0, 1, or 2.

    Returns:
    list[int]: The sorted list with all 0s, followed by all 1s, and then all 2s.
    """
    red = 0
    white = 0
    blue = len(input_list)
    while white != blue:
        if input_list[white] == 0:
            input_list[red], input_list[white] = input_list[white], input_list[red]
            red += 1
            white += 1
        elif input_list[white] == 1:
            white += 1
        elif input_list[white] == 2:
            blue -= 1
            input_list[white], input_list[blue] = input_list[blue], input_list[white]
    return input_list

# temp = input_list[red]
# input_list[red] = input_list[white]
# input_list[white] = temp
# temp = input_list[blue]
# input_list[blue] = input_list[white]
# input_list[white] = temp

def test_function(test_case: list[list[int]]) -> None:
    """
    Test the sort_012 function with a given test case.

    Args:
    test_case (list[list[int]]): A list containing one element:
        - A list of integers where each integer is either 0, 1, or 2, 
          representing the input array to be sorted.

    Returns:
    None: Prints the sorted array and "Pass" if the output from sort_012 
    matches the sorted input array, otherwise prints "Fail".
    """
    sorted_array: list[int] = sort_012(test_case[0])
    print(sorted_array)
    if sorted_array == sorted(test_case[0]):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    # Edge case: Empty input list
    test_function([[]])
    # Expected output: Pass

    # Normal case: Mixed elements
    test_function([[0, 1, 2, 0, 1, 2]])
    # Expected output: Pass

    # Normal case: Already sorted list
    test_function([[0, 0, 1, 1, 2, 2]])
    # Expected output: Pass

    # Normal case: Reverse sorted list
    test_function([[2, 2, 1, 1, 0, 0]])
    # Expected output: Pass
