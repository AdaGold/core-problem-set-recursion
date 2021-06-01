# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
        if n < 0:
            raise ValueError("ValueError exception thrown")
        if n == 0 :
            return 1
        else:
            return n * factorial(n -1 )
    
    


# reverse
def reverse(text):
    if text:
        text = text[::-1]
        return text
    if text == "":
        return ""
    


# bunny
def bunny(count):
    if count < 1:
        return 0
    return 2 + bunny(count - 1)


# is_nested_parens
def is_nested_parens(parens, n = 0):
    if parens == "":
        return True
    if len(parens) % 2 == 1:
        return False
    
    parens_reversed = parens[::-1]
    
    if n >= len(parens):
        return True
        
    if parens[n] == parens_reversed[n]:
        return False
    
    return is_nested_parens(parens, n +1)

