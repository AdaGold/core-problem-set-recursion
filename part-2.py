# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    
    if not query.isalpha():
        return False
    
    if not array:
        return False
        
    if array[0] == query:
        return True
    
    return array[1:]


# is_palindrome
def is_palindrome(text):
    
    # if not text:
    #     return False
        
    if len(text) == 1:
        return True
        
    if text[0] != text[-1]:
        return False
    
    return is_palindrome(text[1:-1])


# digit_match

def digit_match(num1, num2):
    if num1 < 0 or num2 < 0:
        return 0
        
    if num1 == 0 and num2 == 0:
        return 1
        
    if num1 == 0 or num2 == 0:
        return 0
        
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    new_num1 = 0 if not str_num1[:-1] else int(str_num1[:-1])
    new_num2 = 0 if not str_num2[:-1] else int(str_num2[:-1])
    
    
    if str_num1[-1] == str_num2[-1]:
        return 1 + digit_match(new_num1, new_num2)
        
    if new_num1 == 0 and new_num2 == 0:
        return 0
    
    return 0 + digit_match(new_num1, new_num2)
        
