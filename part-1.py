# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError()
        
    if num == 0:
        return 1
        
    return factorial(num - 1) * num


# reverse
def reverse(s):
    if len(s) <= 1:
        return s
    
    return s[-1] + reverse(s[:-1])


# bunny
def bunny(count):
    if count < 0:
        raise ValueError()
    
    if count == 0:
        return 0
    return bunny(count - 1) + 2


# is_nested_parens
def _is_nested_parens(n):
    if not n:
        return 0
    
    v = 1 if n[0] == '(' else -1
    return v + _is_nested_parens(n[1:])

def is_nested_parens(n):
    return 0 == _is_nested_parens(n)

