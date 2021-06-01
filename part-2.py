# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    '''
    Accepts an unsorted array of integers, array, and an integer value to find, query.
    It returns True if query is found in array, and False otherwise. Use Recursion
    '''
    if array == []:                 # Base Case 1
        return False
    elif array.pop() == query:      # Base Case 2
        return True
    else:                           # Recursive Case
        return search(array, query)
    
    search(array, query)


# is_palindrome
def is_palindrome(text):
    '''
    Accepts a string text as a parameter. Returns True if text is a palidrome.
    Returns False if text is not a palidrome
    '''

    if len(text) < 2: 
        return True
    if text[0] != text[-1]: 
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(apple, orange):
    num_match = 0
    
    if apple == "stop" or orange == "stop":
        return 0
    elif apple % 10 == orange % 10:
        num_match = 1
    
    if apple // 10 == 0:
        next_apple = "stop" # if a number runs out of digit from dividing by 10, then, must set number to "stop" or None to terminate.
    else:
        next_apple = apple // 10
    
    if orange // 10 == 0:
        next_orange = "stop"
    else:
        next_orange = orange // 10
    
    return num_match + digit_match(next_apple, next_orange)