"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements are 
in the range [0, 9]. The number of digits in both the numbers cannot differ by 
more than 1. You're not allowed to use any sorting function that Python 
provides and the expected time complexity is O(nlog(n)).

You should implement the function body according to the rearrange_digits 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""
def mergeAbsSort(arr: list[int]) -> list[int]:
    """
    >>> mergeSort([1,2,3,4])
    [4,3,2,1]
    >>> mergeSort([])
    []
    >>> mergeSort([1])
    [1]
    >>> mergeSort([3, -2, 1, -4, 5])
    [5, -2, 3, -2, 1]
    """
    if len(arr) <= 1:
        return arr
    splits = [[x] for x in arr]
    while len(splits) != 1:
        next = []
        for i in range(0, len(splits), 2):
            if i+1 >= len(splits):
                next.append(splits[i])
            else:
                merged = []
                k = 0
                j = 0
                N = len(splits[i]) + len(splits[i+1])
                while k + j < N:
                    if k < len(splits[i]) and j < len(splits[i+1]):
                        if abs(splits[i][k]) <= abs(splits[i+1][j]):
                            merged.append(splits[i+1][j])
                            j+=1
                        else:
                            merged.append(splits[i][k])
                            k+=1
                    elif k < len(splits[i]):
                        merged.append(splits[i][k])
                        k+=1
                    else:
                        merged.append(splits[i+1][j])
                        j+=1
                next.append(merged)
        splits = next
    return splits[0]

def rearrange_digits(input_list: list[int]) -> tuple[int, int]:
    """
    Rearrange the digits of the input list to form two numbers such that their 
    sum is maximized.

    This function sorts the input list in descending order and then alternates 
    the digits to form two numbers.

    Args:
    input_list (list[int]): A list of integers to be rearranged.

    Returns:
    tuple[int, int]: A tuple containing two integers formed by rearranging the 
    digits of the input list.
    """
    ordered = mergeAbsSort(input_list)
    # print(ordered)
    i = 0
    left = []
    right = []
    for elem in ordered:
        if i % 2 == 0:
            left.append(elem)
        else:
            right.append(elem)
        i += 1
    # print("left", left)
    # print("right", right)
    
    return [sum([left[k]*(10**(len(left)-(k+1))) for k in range(0, len(left))]), sum([right[k]*(10**(len(right)-(k+1))) for k in range(0, len(right))])]
    

def test_function(test_case: tuple[list[int], list[int]]) -> None:
    """
    Test the rearrange_digits function with a given test case.

    Args:
    test_case (tuple[list[int], list[int]]): A tuple containing two elements:
        - A list of integers representing the input array to be rearranged.
        - A list of two integers representing the expected output.

    Returns:
    None: Prints "Pass" if the sum of the output from rearrange_digits matches 
    the sum of the expected output, otherwise prints "Fail".
    """
    output: tuple[int, int] = rearrange_digits(test_case[0])
    solution: list[int] = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print(output)
        print("Fail")

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # Edge case: Single element list
    test_function(([9], [9, 0]))
    # Expected output: Pass

    # Normal case: Mixed positive and negative numbers
    test_function(([3, -2, 1, -4, 5], [531, -42]))
    #[5, 3, 1, -2, -4]
    # @NOTE: I thinkt this test case is wrong, it doesn't follow the pattern
    # of alternating digits in the result
    # It might maximize 531, but it does not maximize the sum
    # 531-42 = 489
    # it woulld make more sense if the provided result was [531, -24] which still provide a bigger sum.
    # (530+-4) + (30-2) = 534
    # It seems to be sorted by magnitude? Very weird.
    #[5,-4,3,-2,1] sorted by magnitude?
    #[5,3,1][-4,-2]
    # Expected output: Pass

    # Normal case: list with zeros
    test_function(([0, 0, 0, 0, 0], [0, 0]))
    # Expected output: Pass

    # Normal case: list with repeated numbers
    test_function(([2, 2, 2, 2, 2], [222, 22]))
    # Expected output: Pass

    test_function(([1, 2, 3, 4, 5], [542, 31]))

    test_function(([4, 6, 2, 5, 9, 8], [964, 852]))
