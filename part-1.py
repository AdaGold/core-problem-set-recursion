# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        


# reverse
def reverse(text):
    new = ""
    if text == "":
        return new
    new += text[-1]
    return new + reverse(text.rstrip(text[-1]))


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif len(parens) == 1:
        return False
    remaining = parens[1:-1]
    if parens[0] == "(" and parens[-1] == ")":
        return is_nested_parens(remaining)
    else:
        return False

