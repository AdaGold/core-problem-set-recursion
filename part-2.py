# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if not text:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(int1, int2):
    str1 = str(int1)
    str2 = str(int2)
    i = 0
    if len(str1) == 1 or len(str2) == 1:
        if str1[-1] == str2[-1]:
            return 1
        else:
            return 0
    if str1[-1] == str2[-1]:
        i = 1

    int1 = int(str1[:-1])
    int2 = int(str2[:-1])
    
    return i + digit_match(int1, int2) 

