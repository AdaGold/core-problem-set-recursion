# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n < 0:
        raise(ValueError)
        
    if n == 0:
        return 1
        
    return n * factorial(n-1)


# reverse
def reverse(text):
    if len(text) < 2:
        return text
    return text[-1] + reverse(text[1:-1]) + text[0]
    


# bunny
def bunny(count):
    if count == 0:
        return 0
        
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(text):
    opening_parens = ["{", "[", "("]
    closing_parens = ["}", "]", ")"]

    if len(text) == 0:
        return True

    for i in range(3):
        if text[0] == opening_parens[i]:
            if text[-1] == closing_parens[i]:
                return is_nested_parens(text[1:-1])

    return False
    

