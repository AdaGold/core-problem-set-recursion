# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial (n):
    if n == 0:
        return 1
    elif n > 0:
        return n* factorial(n-1)
    else:
        raise ValueError


# reverse
def reverse (text):
    if text == "":
        return ""
    else:
        return reverse (text[1:]) + text[0]


# bunny
def bunny(count):
    if count == 0:
        return 0
    return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    length = len(parens)
    if length == 0:
        return True 
    if length %2 != 0:
        return False
    
    mid = length//2
    
    if parens[mid] == '(':
        for i in range(mid+1, length):
            if parens[i] == ')':
                return is_nested_parens(parens[:mid] + parens[i+1:])
    elif parens[mid] == ')':
        for i in range(mid-1,-1,-1):
            if parens[i] == '(':
                return is_nested_parens(parens[:i] + parens[mid+1:])

