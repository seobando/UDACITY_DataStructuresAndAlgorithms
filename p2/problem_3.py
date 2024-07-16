def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two numbers such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int, int): Two maximum sums
    """
    if not input_list:
        return (0, 0)
    
    # Sort the list in descending order
    input_list.sort(reverse=True)
    
    num1 = ""
    num2 = ""
    
    # Distribute the digits to form the two numbers
    for i, digit in enumerate(input_list):
        if i % 2 == 0:
            num1 += str(digit)
        else:
            num2 += str(digit)
    
    return (int(num1), int(num2))

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[8, 2, 3, 1, 7], [831, 72]])
