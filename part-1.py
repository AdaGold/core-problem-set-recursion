# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
    elif n <= 0:
        raise(ValueError)
    return n * factorial(n-1)



# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    first_char= text[:1]
    remaining_chars = text[1:]
    return reverse(remaining_chars) + first_char



# bunny
def bunny(count):
    if count == 0:
        return count
    return bunny(count-1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) == 0:
        return True
    outer = parens[0] + parens[-1]
    if outer == "()":
        parens = parens[1:-1]
        return is_nested_parens(parens)
    return False


