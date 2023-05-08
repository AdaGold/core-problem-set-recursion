# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    elif query == array[-1]:
        return True
    
    return search(array[:-1], query)


# is_palindrome
def is_palindrome(text):
    if len(text) < 2:
        if text[0] == text[-1]:
            return True
    elif len(text) > 2:
        return is_palindrome(text[1:-1])
    
    return False


# digit_match


