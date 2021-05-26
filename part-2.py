# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    
    if array == []:
        return False 
    
    elif array[0] == query:
        return True

    else:
        return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    
    if len(text) <= 1:
        return True
    
    elif text[0] != text[-1]:
        return False
    
    else:
        return is_palindrome(text[1:-1])


# digit_match
def digit_match(num_1, num_2):

    #handle the case where one number is 0 after // 0 because digits ran out
    if num_1 == 0 or num_2 == 0:
        if num_1 > 0 or num_2 > 0:
            return 0
    
    #base case 
    if num_1 < 10 and num_2 < 10:    
        if num_1 == num_2:
            return 1
        return 0
    
    return digit_match(num_1 % 10, num_2 % 10) + digit_match(num_1 // 10, num_2 // 10)


