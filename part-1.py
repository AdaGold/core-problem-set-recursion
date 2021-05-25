# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(num):
    if num < 0:
        raise ValueError
    if num == 1 or num == 0:
        return 1
    return num * factorial(num - 1)


# reverse

def reverse(text):
    if text == "":
        return ""
    next_letter = text[len(text)-1]
    return next_letter + reverse(text[0:-1])

# bunny

def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count - 1)

# is_nested_parens

def is_nested_parens(str):
    if str == "":
        return True
    if str[0] + str[-1] != "()":
        return False
    return is_nested_parens(str[1:-1])
