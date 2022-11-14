# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search

def search(array, query):
    if len(array) == 0:
        return False
    elif array[0] == query:
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

def digit_match(a, b):
    if a == 0 and b == 0:
        return 1
    
    elif a < 10 or b < 10:
        if a % 10 == b % 10:
            return 1
        else: 
            return 0
            
    last_digit_a = a % 10
    last_digit_b = b % 10
    
    remaining_a = a // 10
    remaining_b = b // 10
    
    if last_digit_a == last_digit_b:
        return 1+digit_match(remaining_a, remaining_b)
        
    return digit_match(remaining_a, remaining_b)


