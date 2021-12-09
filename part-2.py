# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if array == []:
        return False
    
    if array[0] == query:
        return True
    
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 1:
        return True
    
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False


# digit_match
def digit_match(pos1, pos2):
    pos1 = str(pos1)
    pos2 = str(pos2)
        
    count = 0
    
    if len(pos1) == 0 or len(pos2) == 0:
        return count
    
    if pos1[-1] == pos2[-1]:
        count = 1
        
    return count + digit_match(pos1[:-1], pos2[:-1])

