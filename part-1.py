# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
    if num < 0:
        raise ValueError
        
    elif num == 0:
        return 1 

    else:
        return num * factorial(num-1)


# reverse
def reverse(word):

    if len(word) <= 1:
        return word
    else:
        return reverse(word[1:]) + word[0] 


# bunny
def bunny(num):
    if num == 0:
        return 0
    return 2 + bunny(num-1)


# is_nested_parens

def is_nested_parens(parens):
    if len(parens) == 0:
        return True
        
    
    elif len(parens) >= 2 and (parens[0] == "(" and  parens[-1] == ")"):
        
        return is_nested_parens(parens[1:-1])
    else: 
        False
        

