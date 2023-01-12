# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
# def search(array,query):
#     if query in array:
#         return True

def search(array,query):
    if not len(array):
        return False
    elif array[0] == query:
        return True
    return search(array[1:],query)


# is_palindrome
def is_palindrome(text):
    if len(text) < 2:
        return True
    elif text[0] != text[len(text)-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(a1,a2):
    if a1 <10 and a2 <10:
        return int(a1 == a2)
    
    if a1 <10 or a2 <10:
        return int(a1%10 == a2%10)
        
    return digit_match(a1//10, a2//10) + int(a1%10==a2%10)

