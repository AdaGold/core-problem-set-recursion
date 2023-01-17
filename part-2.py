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
    if len(text) < 2:
        return True
        
    if text[0] == text[-1]:
        return is_palindrome(text[1:-1])
        
    return False


# digit_match
def digit_match(number_one, number_two):
    if len(str(number_one)) == 0 or len(str(number_two)) == 0:
        return 0

    difference = int(number_one) - int(number_two)
    if difference/10 == difference//10:
        return 1 + digit_match(str(number_one)[0:-1], str(number_two)[0:-1])

    else:
        return 0 + digit_match(str(number_one)[0:-1], str(number_two)[0:-1])


