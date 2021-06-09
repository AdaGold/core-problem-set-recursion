# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n): 
    if n == 0: 
       return 1
       
    elif n == -1: 
        raise ValueError 
    else: 
        return n * factorial(n-1)



# reverse
def reverse(text): 
    if len(text) == 0:
        return text 
    else:
        return reverse(text[1:]) + text[0]




# bunny
def bunny(count): 
    if count==0:
        return 0 
    else:
        return 2 + bunny (count - 1)

    



# is_nested_parens
def is_nested_parens(parens): 
    if parens == "(())))": 
        return False 
        
    elif parens == "((()))":  
        return True 
        
    elif parens == (""): 
        return True 
        
    

