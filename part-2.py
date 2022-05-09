# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if array == []:
        return False
    return array[0] == query or search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) < 2: 
        return True
    elif text[0] != text[-1]: 
        return False
    else:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(integer1, integer2):
    if integer1 < 10 and integer2 < 10:
        return integer1 == integer2
    elif integer1 == 0 or integer2 == 0:
        return 0
    is_last_digit_matched = integer1 % 10 == integer2 % 10
    
    return (1 if is_last_digit_matched else 0) + digit_match(integer1 // 10, integer2 // 10)
        


