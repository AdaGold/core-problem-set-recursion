# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    elif num < 2:
        return 1
    return num * factorial(num - 1)
# reverse
def reverse(s):
    if len(s) < 2:
        return s
    return reverse(s[1:]) + s[:1]
# bunny
def bunny(count):
    if count == 0:
        return 0
    return bunny(count - 1) + 2
# is_nested_parens
def is_nested_parens(s):
    if not s or s == "()":
        return True
    if s[0] != "(" or s[-1] != ")":
        return False
    return is_nested_parens(s[1:-1])
