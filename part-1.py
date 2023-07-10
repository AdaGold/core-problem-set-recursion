# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
# Write a function factorial that accepts an integer parameter n. It uses recursion to compute and return the value of n factorial (also written as n!).

# Here are the tests:

# def test_factorial_zero():
    # assert factorial(0) == 1


# def test_factorial_positive_num():
    # assert factorial(5) == 5 * 4 * 3 * 2 * 1


# def test_factorial_negative_num():
    # with pytest.raises(ValueError):
        # factorial(-1)
def factorial(num):
    
    if num == 0:
        return 1
    elif num < 0:
        raise ValueError
    
    return num * factorial(num - 1) 


# reverse
# Write a function reverse that accepts a string text as a parameter. It returns the reverse of text by reversing all characters in the string.

# Here are the tests:

# def test_reverse_word():
    # assert reverse("cat") == "tac"


# def test_reverse_single_character():
    # assert reverse("a") == "a"


# def test_reverse_empty_string():
    # assert reverse("") == ""

def reverse(text):
    
    if len(text) == 0:
        return ""
    
    return text[-1] + reverse(text[:-1])


# bunny
# Write a function bunny that accepts an integer parameter count. count represents a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

# Here are the tests:

# def test_bunny_zero_bunnies():
    # assert bunny(0) == 0


# def test_bunny_one_bunny_has_two_ears():
    # assert bunny(1) == 2


# def test_bunny_fifty_bunnies_have_100_ears():
    # assert bunny(50) == 100

def bunny(count):
    
    if count == 0:
        return 0
    return 2 + bunny(count-1)

# is_nested_parens

# Write a function is_nested_parens that accepts a string parens of only parentheses. It returns True if those parentheses are properly nested, and False if they are not. You may assume that no non-parenthesis characters will be passed to this function.

# Example parens Expected Output
# "((()))"	True
# ""	True
# "(())))"	False
# Here are the tests:

# def test_is_nested_parens():
    # parens = "((()))"

    # assert is_nested_parens(parens)


# def test_is_nested_parens_empty_str():
    # assert is_nested_parens("")


# def test_is_nested_parens_not_matching_length():
    # parens = "(())))"
#
    # assert not is_nested_parens(parens)

def is_nested_parens(parens):
    
    if not parens:
        return True
    
    elif parens[0] == "(" and parens[-1] == ")":
        
        return is_nested_parens(parens[1:-1])
        
    else:
        return False
