# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    # function cal: search()
    # input: array (of unsorted integers) and query (an integer value)
    # output: True if query in array, False if it isn't
    # base case 
    if len(array) == 0:
        return False
    elif  query == array[0]:
        return True
        
    # recursive case:
    return search(array[1:], query)
        
    
# is_palindrome
def is_palindrome(text):
# function call is_palindrome(text)
# input: a string text
# output: True if the string is a palindrome and False if it isn't 
    if len(text) == "":
        return True
    elif len(text) == 1:
        return True
    if text[:1] == text[-1:] and is_palindrome(text[1:-1]):
        return True
    return False 

# digit_match
def digit_match(s_1, s_2):
# function call digit_match()
# input: two non-negative integers as parameters
# returns the number of digits that match in the two integers.
# output: returns the number of digits that match in the two integers

    # base case:
    # either strings are empty 
    str_1 = str(s_1)
    str_2 = str(s_2)
    
    if not len(str_1) or not len(str_2):
        # return matches
        return 0

    # strings are not empty but strings don't match
    if (str_1[-1]) != (str_2[-1]):
        return digit_match(str_1[:-1], str_2[:-1])
    else:
        return 1 + digit_match(str_1[:-1], str_2[:-1])
        

