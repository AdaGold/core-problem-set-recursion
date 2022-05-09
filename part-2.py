# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if query in array:
        return True
    else:
        return False
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

# digit_match
def digit_match(int1, int2):
    
    string1 = str(int1)
    string2 = str(int2)
    
    result = 0
    
    if not string1 and not string2:
        result == 1
        return result
    elif not string1 or not string2:
        return result
    elif string1[-1] == string2[-1]:
        result += 1
        return result + digit_match(string1[:-1], string2[:-1])
    elif string1[-1] != string2[-1]:
        return result + digit_match(string1[:-1], string2[:-1])

