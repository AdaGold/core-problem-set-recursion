# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    
    if n<0:
        raise ValueError
    return n*factorial(n-1)


# reverse
def reverse(text):
    if len(text)<=1:
        return text
    
    return reverse(text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    
    return bunny(count-1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    match = {"(":")"}
    if match.get(parens[0], 0)==0:
        return False

    return match[parens[0]] == parens[-1] and is_nested_parens(parens[1:-1])
