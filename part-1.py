# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    
    #The factorial function (symbol: !) 
    #says to multiply all whole numbers 
    #from our chosen number down to 1.
    if n < 0:
        raise ValueError
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1) 



# reverse

def reverse(text):
    
    if text == "":
            return text
    
    last_char = text[-1]
    remaining_char = text[0:-1]
    result = last_char + reverse(remaining_char)
    
    return result



# bunny

def bunny(count):
    
    if count == 0:
        return 0
    else:
    
        return 2 + bunny(count -1)


# is_nested_parens

def is_nested_parens(parens, start = 0):
    
    if parens == "":
        return True
    if start >= len(parens)/2:
        return True

    if parens[start] != parens[len(parens) -1 - start]:
    
        if parens[start] ==  "(" and parens[len(parens) -1 - start] == ")":
            return is_nested_parens(parens, start + 1)
    return False

