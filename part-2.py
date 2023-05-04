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
    
    return search(array[1:],query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if len(text) >= 2 and text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    else:
        return False


# digit_match


