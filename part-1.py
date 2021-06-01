# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError 
    elif n <= 1:
        return 1
    return n * factorial(n-1)


# reverse
def reverse(text):
    str_len = len(text)
    if str_len <= 1:
        return text
    shorten_str_len = str_len - 1
    return reverse(text[-shorten_str_len:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    elif count == 1:
        return 2
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) <= 0:
        return True
    elif len(parens) % 2 != 0:
        return False
    elif parens[0] == "(" and parens[-1] ==")":
        return is_nested_parens(parens[1:-1])

