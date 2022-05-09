# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError
    return n * factorial(n-1)


# reverse
def reverse(text):
    index = len(text) - 1
    if len(text) > 0:
        if text[index] == text[0]:
            return text[0]
        new_str = text[index] + reverse(text[:index])
        return new_str
    else:
        return text

# bunny
def bunny(count):
    if count == 0:
        return count
    return 2 + bunny(count -1)


# is_nested_parens
def  is_nested_parens(parens):
    if len(parens) % 2 != 0:
        return False
    if len(parens) == 0:
        return True
    if parens[0] != parens[len(parens) - 1]:
        return is_nested_parens(parens[1:len(parens) - 1])
    else:
        return False

