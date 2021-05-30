# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query, left_index=0):
    if not array or left_index > len(array) - 1:
        return False
        
    elif array[left_index] != query:
        return search(array, query, left_index+1)
        
    return True
    

# is_palindrome
def is_palindrome(text, left_index=0):
    right_index = len(text) - 1 - left_index
    
    if left_index > right_index:
        return True
    elif text[left_index] == text[right_index]:
        return is_palindrome(text, left_index+1)
    
    return False

# digit_match

def digit_match(apples, oranges):
    if apples == 0 and oranges == 0:
        return 1
    
    elif apples <= 1 and oranges > 1:
        return 0
    
    elif oranges <= 1 and apples > 1:
        return 0
        
    elif apples % 10 == oranges % 10:
        return 1 + digit_match(apples//10, oranges//10)
    
    return digit_match(apples//10, oranges//10)
