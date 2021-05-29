# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if 0 <= n <= 1:
        return 1
    return n * factorial(n - 1)

# reverse
def reverse(text):
    if len(text) == 0:
        return text
    return reverse(text[1:]) + text[0]

# bunny
def bunny(count):
    if count == 0:
        return 0
    if count == 1:
        return 2
    return bunny(1) + bunny(count - 1)

# is_nested_parens
def is_nested_parens(parens):
    a = ['()', '{}', '[]']
    if len(parens) == 0:
        return True
    elif not any([True for i in a if i in parens]):
        return False
    else:
        for i in a:
            if i in parens:
                parens = ''.join(parens.split(i))
        return is_nested_parens(parens)

