# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    """
    base case: is not array return False
    """
    if not array:
        return False
    if array[-1] == query:
        return True
    return search(array[:-1], query)

# is_palindrome

def is_palindrome(text):
    """
    base case: if not text or text == 1 return True
    """
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

# digit_match

def digit_match(a, b):
    """ 
    base case: if only one digit is left for either number
    check if the digit is matching. Return 1 if matching, 0 if not. 
    """
    
    
    if a//10 == 0 or b//10 == 0:
        if a % 10 == b % 10:
            return 1
        else:
            return 0
            
    count = 0
            
    if a % 10 == b % 10:
        count += 1
        
    count += digit_match(a // 10, b // 10)
        
    
    return count
