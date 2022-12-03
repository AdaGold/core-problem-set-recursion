# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError("n must be greater than zero")
        
    return n * factorial(n-1)
    
# reverse
def reverse(text):
    return text[::-1]

# bunny
# def bunny(count):
#     return count*2

def bunny(count):
    if count == 0:
        return 0
    else:
        return 2 + bunny(count-1)

# is_nested_parens
def is_nested_parens(string):
    count = 0
    for i in string: 
        if i== "(":
            count += 1
        elif i == ")":
            count -= 1
    if count == 0:
        return True
    else: 
        return False
        

