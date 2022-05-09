# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Number must be greater than zero")
    elif n == 0:
        return 1
    return factorial( n -1 ) * n


# reverse
def reverse(text):
    if text == "":
        return ""
    elif len(text) == 1:
        return text
    else:
        return text[-1] + reverse(text[:-1])


# bunny
def bunny(count):
    if count == 0:
        return count
    elif count == 1:
        return 2
    return bunny(1) + bunny(count -1) #bunny(1) = 2 and bunny(49) = 2 + 98


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    elif parens[0] != "(" or parens[-1] != ")":
        return False
    return is_nested_parens(parens[1:-1])

