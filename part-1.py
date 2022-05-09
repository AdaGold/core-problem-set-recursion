# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    if num == 0:
        return 1
    return num * factorial(num-1)

# reverse
def reverse(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse(s[:-1])

# bunny
def bunny(num):
    if num == 0:
        return 0
    return bunny(num-1) + 2

# is_nested_parens
def is_nested_parens(s):
    if len(s) == 0:
        return True
    if s[0] != '(' or s[-1] != ')':
        return False
    return is_nested_parens(s[1:-1])

