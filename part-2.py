# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search



# is_palindrome
def is_palindrome(text):
    if reverse(text) == text:
        return True
    return False
    
def reverse(text):
    if text == "":
        return text
    else:
        return text[-1] + reverse(text[:-1])


# digit_match


