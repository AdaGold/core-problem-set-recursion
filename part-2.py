# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if query == array[0]:
        return True

    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 0:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(int1, int2):
    match = 0
    if int1 == "" or int2 == "":
        return match
        
    if str(int1)[-1] == str(int2)[-1]:
        match +=1
    
    return match + digit_match(str(int1)[:-1], str(int2)[:-1])

