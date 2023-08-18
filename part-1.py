# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    try:
        if n == 0:
            return 1
        return factorial(n-1) * n
    except:
        if n < 1:
            raise ValueError


# reverse
def reverse(text):
    print("Text:",text)
    if len(text) == 1 or not text:
        return text
    
    return (text[-1] + reverse(text[:-1]))


# bunny
def bunny(count):
    if count == 0:
        return 0
    return bunny(count-1) + 2


# is_nested_parens
def is_nested_parens(parens):
    if not parens:
        return True
    if len(parens) == 1:
        return False
    if len(parens) == 2:
        if parens[0] == ")" and parens[1] == "(":
            return False
        if parens[0] == parens[1]:
            return False
        
    return is_nested_parens(parens[1:-1])
