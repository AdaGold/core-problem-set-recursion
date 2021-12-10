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
    return (num *(factorial(num-1)))


# reverse
def reverse(text):
    if not text:
        return text
    return text[-1] + reverse(text[:-1])


# bunny
def bunny(count):
    if count == 0:
        return count
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    elif len(parens) == 2 and parens[0] == parens[1]:
        return False
    elif len(parens)%2 == 0:
        return is_nested_parens(parens[1:-1])
    return False

