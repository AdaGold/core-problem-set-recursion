# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    """Returning True if query is found in array, and False otherwise"""
    if len(array) == 0:
        return False
        
    elif array[len(array)-1] == query:
        return True
    return search(array[:-1], query)



# is_palindrome
def is_palindrome(text):
    """Returning True if it is palindrome, and False otherwise"""
    if len(text) <= 0:
        return True
    elif text[0] == text[-1]:
        return is_palindrome(text[1:-1])
    return False


# digit_match
def digit_match(num1, num2):
    """Return the number of matching pair digits or 0 if all digits don't mactch."""
    str_num1 = str(num1)
    str_num2 = str(num2)
    if len(str_num1) == 0 or len(str_num2) == 0:
        return 0
    elif str_num1[-1] == str_num2[-1]:
        return digit_match(str_num1[0:-1], str_num2[0:-1]) + 1
    return digit_match(str_num1[0:-1], str_num2[0:-1])

