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
    return n * factorial(n - 1)


# reverse
def reverse(text):
    size = len(text)
    if size == 0:
        return ""
    elif size == 1:
        return text
    else: 
        first_char = text[0]
        the_rest = str(text[1:])
        return reverse(the_rest) + first_char


# bunny
def bunny(count):
    if count <= 0:
        return 0
    elif count == 1:
        return 2
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    size = len(parens)
    if size == 0:
        return True
    elif str(parens[0]) == "(" and str(parens[-1]) == ")":
        inside = str(parens[1:-1])
        return is_nested_parens(inside) 
    else:
        return False

