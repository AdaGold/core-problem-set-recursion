# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1
    return factorial(n-1) * n


# reverse
def reverse(text):
    if text == "":
        return text
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    return bunny(count-1) + 2


# is_nested_parens in the no new string version
def is_nested_parens(text, loops=0):
    i = loops
    j = len(text) - 1 - loops
    if i == j + 1:
        return True
    elif text[i] != "(" or text[j] != ")":
        return False
    return is_nested_parens(text, loops + 1)