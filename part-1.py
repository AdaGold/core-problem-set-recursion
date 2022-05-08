# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    return n * factorial(n-1)

# reverse
def reverse(text):
    if text == "":
        return ""
    try:
        reversed_text += text[-1]
    except UnboundLocalError:
        reversed_text = text[-1]
    
    return reversed_text + reverse(text[:-1])


# bunny
def bunny(count):
    if count < 0:
        raise ValueError
    elif count == 0:
        return 0
    elif count == 1:
        return 2
    return 2 + bunny(count-1)



# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    if len(parens) % 2 != 0:
        return False
    if parens[0] == "(" and parens[-1] == ")":
        new_string = parens[1:-1]
    else:
        return False
    return is_nested_parens(new_string)