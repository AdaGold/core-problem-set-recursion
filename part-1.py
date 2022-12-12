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
        
    running_factorial = factorial(n -1)
    return running_factorial * n
    
#return factorial(n-1) * n 
     
# reverse
def reverse(text):
      #cat 
    #c #at
    if len(text) <= 1:
        return text 

    first_letter = text[0]
    rest_of_word = text[1:]

    reversed_string = reverse(rest_of_word)
    new_text = reversed_string + first_letter
    
    return new_text

# bunny
def bunny(count):
    
    if count == 0:
        return 0
#count represents one bunny, each bunny has two ears
    else:
        return 2 + bunny(count -1)

# is_nested_parens
def is_nested_parens(parens):
    #left = 0
    #right = 0
    if len(parens) == 0:
        return True
#replace loop
    elif parens[:1] != "(" or parens[-1:] != ")":
        return False      
    else:
        return is_nested_parens(parens[1:-1])
        