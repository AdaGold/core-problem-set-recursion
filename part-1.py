# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# reverse
def reverse(text):
    if len(text) == 0:
        return ""
    return text[-1] + reverse(text[:-1])


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    elif len(parens) == 1:
        return False
    n_parens = is_nested_parens(parens[1:-1])
    if parens[0] == "(" and parens[-1] == ")" and n_parens:
        return True
    return False

