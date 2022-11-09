# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

####We did these in class...

# search
def search(array, query):
    #First base case -- if query isn't in list, returns False
    if len(array) == 0:
        return False
        
    #Second base case -- if first elem in array is query 
    # then query in list, returns True
    elif array[0] == query:
        return True
        
    # Recursive case -- returns the array from index 1 to start 
    # at array[0] with next recursive case
    return search(array[1:], query)


# is_palindrome -- this is exactly the same as parens function except
# checks for an odd center char that is ok in a palindrome
def is_palindrome(text):
    # Base case
    if len(text) <= 1:
        return True

    # Base case -- if char at opposite index do not equal, not a palindrome 
    if text[0] != text[-1]:
        return False

    # Recursive case -- returning chars inside index 0 and -1 to check
    # next chars to see if match    
    return is_palindrome(text[1:-1])



# digit_match -- I don't understand this one
def digit_match(int1, int2):
    # Base case
    if int1 == 0 and int2 == 0:
        return 1
    
    # Recursive case
    return digit_match_helper(int1, int2, 0)
    
# Helper function    
def digit_match_helper(int1, int2, count):
    if int1 == 0 or int2 == 0:
        return count
        
    if int1 % 10 == int2 % 10:
        return digit_match_helper(int1 // 10, int2 // 10, count + 1)
        
    if int1 % 10 != int2 %10:
        return digit_match_helper(int1 // 10, int2 // 10, count)

