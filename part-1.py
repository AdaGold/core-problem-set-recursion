# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n <0:
        raise ValueError
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)


# reverse
def reverse(text):
    if text == "":
        return ""
    elif len(text) == 1:
        return text
    
    first_char = text[:1]
    remaining_chars = text[1:]
    return reverse(remaining_chars) + first_char


# bunny
def bunny(count):
    if count <=0:
        return 0
    return bunny(count-1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True

    first_half = parens[0]
    second_half = parens[len(parens)-1]
    if first_half == "(" and second_half == ")":
        return is_nested_parens(parens[1:len(parens)-1])
    else:
        return False

