# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError
    return n * factorial(n-1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    return text[len(text)-1] + reverse(text[:-1])


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    elif parens[0] == "(" and parens[-1] == ")" and is_nested_parens(parens[1:-1]):
        return True
    else:
        return False

# is_nested_parens extra challenge


def parens_helper(str, left, right):
    if left >= right:
        return True
    elif str[left] == "(" and str[right] == ")":
        return parens_helper(str, left+1, right-1)
    else:
        return False


def is_nested_parens2(parens):
    return parens_helper(parens, 0, len(parens)-1)
