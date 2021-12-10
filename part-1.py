# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        raise ValueError

    return factorial(num-1) * num

# reverse
def reverse(text): 
    if len(text) <= 1:
        return text

    return text[-1] + reverse(text[:-1])

# bunny
def bunny(count):
    if count == 1:
        return 2
    elif count == 0:
        return 0

    return bunny(count-1) + 2

# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif len(parens) == 1:
        return False
    elif parens[0]=="(" and parens[-1]==")" and is_nested_parens(parens[1:-1]):
        return True
    else:
        return False



