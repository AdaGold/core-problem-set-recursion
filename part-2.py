# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array)==0:
        return False
    elif query == array[0]:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 1:
        return True
    elif text[:1] != text[-1:]:
        return False
    else:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(int1, int2):
    
    if int1 == 0 and int2 == 0:
        return 1
    elif int1 <= 1 or int2 <= 1:
        return 0
    
    if int1 % 10 == int2 % 10:
        return 1 + digit_match(int1 // 10, int2 // 10)
    else:
        return digit_match(int1 // 10, int2 // 10)

