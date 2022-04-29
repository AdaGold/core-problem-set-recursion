# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if n<0:
        raise ValueError ("Number should be positive")    
    if n<=1: 
        return 1
    
    return n*factorial(n-1) 

# reverse

def reverse(text):
    
    if len(text)<=1:
        return text
        
    return text[-1]+reverse(text[:-1])  


# bunny

def bunny(count):
    if count==0:
        return 0
        
    return  2+bunny(count-1)  


# is_nested_parens

# solution with creating new strings in the process
# def is_nested_parens(parens):
#     dict_parens={"(":")","{":"}","[":"]"}
    
#     if parens=="":
#         return True
        
#     return parens[0] in dict_parens and parens[-1]==dict_parens[parens[0]] and is_nested_parens(parens[1:-1])  
    
    
#challenge    
def is_nested_parens(parens):    
    left =0
    right =len(parens)-1   

    return helper(parens, left, right)          
    
def helper(parens, left, right):
    if left>right:
        return True
    dict_parens={"(":")","{":"}","[":"]"}
    return parens[left] in dict_parens and parens[right]==dict_parens[parens[left]] and helper(parens, left+1, right-1)
