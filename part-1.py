# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise ValueError("Please enter a non-negative number.")
    
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)



# reverse
def reverse(text):
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count <= 0:
        return 0
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens):
    if len(parens) <= 2:
        if len(parens) == 2:
            if parens[0] != parens[1]:
                return True
            else:
                return False
        elif len(parens) == 1:
            return False
        elif len(parens) == 0:
            return True
    return is_nested_parens(parens[1:-1])

