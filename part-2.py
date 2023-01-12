# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query): 
    if not array or not query:
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
def digit_match(first, second): 
    if first < 10 and second < 10:
        return int(first == second)
    
    if first < 10 or second < 10:
        return int(first%10 == second%10)
        
        
    return digit_match(first//10, second//10) + int(first%10==second%10)

