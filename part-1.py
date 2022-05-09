# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    if num < 1:
        return 1
    return factorial(num-1) * num


# reverse
def reverse(text):
    if text == "":
        return ""
    return text [-1] + reverse(text[:-1])



# bunny
def bunny(count):
    if count == 0:
        return 0
    return bunny(count-1) + 2



# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])

