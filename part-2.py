# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if array == []:
        return False
    elif query == array[0]:
        return True
        
    
    return search(array[1:], query)



# is_palindrome
def is_palindrome(text):
    if len(text) == 1:
        return True
    elif text[0] != text[-1]:
        return False
    
    return is_palindrome(text[1:-1])



# digit_match
def digit_match(num1, num2):
    if num1 == 0 and num2 == 0:
        return 1
    elif num1 == 0 or num2 == 0:
        return 0

#No clue how to write the rest of this function lol 


