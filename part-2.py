# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    if len(array) == 0:
        return False
    
    if array[0] == query:
        return True
        
    return search(array[1:], query)    

# is_palindrome

def is_palindrome(text):
    if len(text) <= 1:
        return True
    
    if text[0] != text[-1]:
        return False 
    return is_palindrome(text[1:-1])   

# digit_match

def digit_match(x,y):
    x = str(x)
    y = str(y) 
    if len(x) == 0 or len(y) == 0:
        return 0

    
    if x[-1] == y[-1]:
        return 1 + digit_match(x[:-1], y[:-1])
    else: 
        return digit_match(x[:-1], y[:-1])

