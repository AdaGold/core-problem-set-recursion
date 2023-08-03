# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError("Number must be greater than zero")
    if num == 0:
        return 1
    return num * factorial(num-1)


# reverse
def reverse(text):
    if len(text) <= 1:
        return text
        
    first_char = text[:1]
    remaining_chars = text[1:]
    return reverse(remaining_chars) + first_char


# bunny
def bunny(count):
    if not count:
        return count
    else:
        return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False
    else:
        return is_nested_parens(parens[1:-1])

