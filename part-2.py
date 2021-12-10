# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array,query):
    if len(array)==0:
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text)<=1:
        return True
    elif text[:1] != text[-1:]:
        return False
    else:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(int_1,int_2):
    if int_1 == 0 and int_2 == 0:
        return 1
    result = 0
    if int_1 % 10 == int_2 % 10:
        result = 1
    if int_1 // 10 == 0 or int_2 // 10 == 0:
        return result
    return result + digit_match(int_1 // 10, int_2 // 10)

