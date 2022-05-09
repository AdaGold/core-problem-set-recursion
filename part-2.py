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
    if len(text) < 2:
        return True 
    elif text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])



# digit_match
#haven't found a clue yet

