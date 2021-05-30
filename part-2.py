# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    
    if len(array) == 0:
        return False
        
    elif array[0] == query:
        return True
        
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    
    if len(text) <= 1: 
        return True
        
    elif text[0] != text[-1]: 
        return False
        
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(apples, oranges):

    # if both apples and oranges are single digit
    if apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        return 0
    # Recursive cases if apples and ornages are double digits
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10) #add 1 if digit matches
    else:
        return digit_match(apples // 10, oranges // 10) #run the function again but do not add 1 if digits do not match

