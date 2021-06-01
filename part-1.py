# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(num):
   
    
    if num==0:
        return 1
    elif num<0:
        raise ValueError
        
    else:    
        return factorial(num-1) * num


# reverse
def reverse(word):
    if len(word) ==0:
        return ""
    elif len(word) ==1:
        return word
    else:
        return reverse(word[1:]) + word[0]



# bunny
def bunny(count):
    if count == 1:
        return 2
    elif count ==0:
        return 0
        
    return bunny(count-1) +2


# is_nested_parens

def is_nested_parens(parens, left_index=0):
    right_index = len(parens) -1 -left_index
    
    if len(parens) == 0:
        return True
    
    if left_index>=right_index:
        return True
    
    if parens[left_index] == "(" and parens[right_index] == ")":
        return is_nested_parens(parens,left_index + 1)
    
    else:
        return False
