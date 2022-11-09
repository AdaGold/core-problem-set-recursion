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
    return factorial(num-1) * num


# reverse
def reverse(text):
    if len(text) == 0:
        return text

    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0

    return bunny(count-1) + 2


# is_nested_parens


