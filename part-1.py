# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n <= 1:
        return 1
    return n * factorial(n-1)


# reverse
def reverse(text):
    if text == "":
        return ""
    if len(text) == 1:
        return text
    return text[len(text) -1] + reverse(text[:-1])


# bunny
def bunny(count):
    if count == 0:
        return 0
    if count == 1:
        return 2
    return bunny(count - 1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    if len(parens) == 1:
        return False
    first = parens[0]
    last = parens[-1]
    if first == last:
        return False
    new_str = parens[1:-1]
    return is_nested_parens(new_str)

