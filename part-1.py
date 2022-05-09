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
    return n * factorial(n - 1)

# reverse
def reverse(text):
    if text == "":
        return ""
    return text[-1] + reverse(text[:-1])

# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count -1)

# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    if (len(parens) == 1):
        return False
    if parens[0] == '(' and parens[-1] == ')' and is_nested_parens(parens[1:-1]):
        return True
    return False


