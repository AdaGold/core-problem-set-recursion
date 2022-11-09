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
    if str(int1)[-1] == str(int2)[-1]:
        add = 1
    else:
        add = 0
        
    if len(str(int1)) == 1 or len(str(int2)) == 1:
        return add
        
    return add + digit_match(int1//10,int2//10)

