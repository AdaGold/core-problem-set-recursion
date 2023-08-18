# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
        
    if array[0] == query:
        return True
        
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if not text or len(text) == 1:
        return True
        
    if text[0] != text[-1]:
        return False
        
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(int1, int2):
    int1 = str(int1)
    int2 = str(int2)
    
    if not int1 or not int2:
        return 0
        
    if int1[-1] != int2[-1]:
        return digit_match(int1[:-1],int2[:-1])
        
    return digit_match(int1[:-1],int2[:-1]) + 1