# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == -1:
        raise ValueError
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n-1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    f_char = text[0]
    leftovers = text[1:]
    return reverse(leftovers) + f_char


# bunny
def bunny(count):
    if count == 0:
        return 0
    if count == 1:
        return 2
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])

