# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial

def factorial(n):
    if n == 0:
        return 1
    elif n > 0: 
        return n * (factorial(n-1))
    else:
        raise ValueError

# reverse

def reverse(text):
    
    if len(text) >= 1:
        #text[::-1] works buuuut
        #base case is text[:1]- stop at index 1
        #text [1:] -everything else
        
        first_letter = text[:1]
        remaining_letters = text[1:]
        return reverse(remaining_letters) + first_letter
        
    else: 
        return ""

# bunny

def bunny(count):
    if count == 0:
        return 0
    else:
        return 2+ bunny(count-1)

# is_nested_parens

def is_nested_parens(parens, left_i=0):
    right_i = len(parens) -1 -left_i
    
    if len(parens) == 0:
        return True
        
    if left_i >= right_i:
        return True
   
    if parens[left_i] == "(" and parens[right_i] == ")":
        return is_nested_parens(parens, left_i+1)
    else: 
        return False 
        

