# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if array == []:
        return False
    if array.pop() == query:
        return True
    else:
        return search(array, query)


# is_palindrome
def is_palindrome(text):
    if text[0] != text[-1]:
        return False
    if len(text) <= 1:
        return True
    
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(int1, int2):
    if int1 == 0 and int2 == 0:
        return 1
    
    if int1 < 10 or int2 < 10:
        if int1 == 0 or int2 == 0:
            return 0
        elif int1 % 10 == int2 % 10:
            return 1
        else:
            return 0
    
    if int1 % 10 == int2 % 10:
            return 1 + digit_match(int1 // 10, int2 // 10)
    else:
        return digit_match(int1 // 10, int2 // 10)

