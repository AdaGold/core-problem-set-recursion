# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1
    return n * factorial(n-1)



# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    first_letter = text[:1]
    remaining_letters = text[1:]
    return reverse(remaining_letters) + first_letter



# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)



# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    elif parens[:1] != '(' or parens[-1:] != ')':
        return False
    return is_nested_parens(parens[1:-1])