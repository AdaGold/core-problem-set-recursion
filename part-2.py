# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,query):
    if not array :
        return False
    elif array[0] == query:
        return True
    return search(array[1:],query)

# is_palindrome
def is_palindrome(s):
    if len(s)<=1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1]) 


# digit_match


