# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search (array, query):
    if len(array) == 0:
        return False
    elif query == array[0]:
        return True
    return search(array[1:],query)


# is_palindrome
def is_palindrome(text):
    if len(text) <= 0 :
        return True
    elif text[0] != text[-1]:
        return False
    elif text[0] == text[-1]:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):
    count = 0
    app_str = str(apples)
    or_str = str(oranges)
    
    if len(app_str) == 0 or len(or_str) == 0 :
        return count
        
    elif app_str[-1] == or_str[-1]:
        count += 1
        
    return count + digit_match(app_str[:-1],or_str[:-1])

