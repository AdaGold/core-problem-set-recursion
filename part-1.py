# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
    if num == 0:
        return 1
    return num * factorial(num-1)



# reverse
def reverse(text):
    if len(text) == 1:
        return text
    elif text == "":
        return ""
        
    
    return text[-1] + reverse(text[:-1])


# bunny
def bunny(count):
    sum = 0
    if count == 1:
        return 2
    elif count == 0:
        return 0
    sum += 2
        
    return sum + bunny(count-1)



# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    elif parens[0] != "(" or parens[-1] != ")":
        return False
    
    return is_nested_parens(parens[1:-1])


