# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    """Return the value of n factorial if n greater than or equal to 0, 
    otherwise will raise Value Error"""

    if n == 0:
        return 1
    elif n < 0:
        raise ValueError ("Number must greater than zero")
        
    return n * factorial(n-1)


# reverse
def reverse(text):
    """Returning the reverse of text"""
    if len(text) == 0:
        return text
    return reverse(text[1:]) + text[0]


# bunny
# Solution 1
def bunny(count):
    """Returning the total ears of bunny by 2 * count."""
    if count == 0:
        return count
    return 2 + bunny(count-1)

# Solution 2
# def bunny(count):
#   """"Returning the total ears of bunny by 2 * count.""""
#     if count == 0:
#         return 0
#     return 2 * count + 0*bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    """Returning True if those parentheses are properly nested, otherwise return False."""
    if parens == "":
        return True
    elif parens[0] == parens[-1]:
        return False
    return is_nested_parens(parens[1:-1])


