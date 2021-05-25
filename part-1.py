# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(num):
    if num >= 0:
        if num == 0:
            return 1
        return num * factorial(num - 1)
    else:
        raise ValueError


# reverse


def reverse(string):
    if string == "":
        return ""
    if len(string) == 1:
        return string
    return string[-1] + reverse(string[:-1])

# bunny


def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)

# is_nested_parens


def is_nested_parens(str):
    if len(str) == 0:
        return True
    return (True if str[0] + str[-1] ==
            "()" else False) and is_nested_parens(str[1:-1])
