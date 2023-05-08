# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n == 0:
        return 1
    
    if n < 0:
        raise ValueError 
    
    return n * factorial(n-1)




# reverse
def reverse(text):
    if len(text) <= 1:
        return text
        
    
    
    return reverse(text[1::]) + text[0]



# bunny
def bunny(count):
    if count <= 0:
        return 0
    else:
        return bunny(count-1) + 2
    



# is_nested_parens
#I realized I wasn't supposed to do it this way
#I understood the proper solution after I saw it

def is_nested_parens(parens):
    paren_dict = {}
    if len(parens) <= 1:
        return True
    for paren in parens:
        if paren not in paren_dict:
            paren_dict[paren] = 1
        else:
            paren_dict[paren] +=1
    if list(paren_dict.values())[0] == list(paren_dict.values())[1]:
        return True
    else:
        return False

