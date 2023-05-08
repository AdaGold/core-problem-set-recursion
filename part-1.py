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
    return n * factorial(n-1)


# reverse
def reverse(text):
    if len(text) == 0:
       return text
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return count
    else:
        return 2 + bunny(count -1)


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) < 2:
        return True
    if parens[0] != "(" or parens[-1] != ")":
        return False
    return is_nested_parens(parens[1:-1])

