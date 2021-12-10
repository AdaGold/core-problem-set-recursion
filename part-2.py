# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    elif query == array[0]:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if not text or text == 1:
        return True
    elif text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):
    if apples == 0 and oranges == 0:
        return 1
        
    result = 0
    
    if apples%10 == oranges%10:
        result = 1
        
    if apples//10 == 0 or oranges//10 == 0:
        return result
        
    return result + digit_match(apples//10, oranges//10)

