# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.
##############################################
# search
##############################################
def search(array,query):
    # function will always check if the array  is empty
    if len(array) == 0:
        return False
    # the function will check if the first value against the value for query
    elif array[0] == query:
        return True
    else:
        # recursive function that removes the first value
        return search(array[1:],query)

##############################################
# is_palindrome
##############################################
def is_palindrome(text):
    # if the recursion empties the list it should break
    if len(text) == 0:
        return True
    elif text[0] == text[-1]:
        # recursive function that removes the first and last character
        # it will keep getting called as long as the first and last character
        # is the same
        return is_palindrome(text[1:-1])
    # if the first and last value does not equal each other
    # if you have not reached the end of string
    else:
        return False

##############################################
# digit_match
##############################################
def digit_match(first_num, second_num):
    num_match = 0
    first_str = str(first_num)
    second_str = str(second_num)
    
    num_match += count_match(first_str, second_str, num_match)
        
    return num_match

# helper function that uses recursion to keep count
def count_match (first_str, second_str,count):
    # checks if we have reached the end of one integer
    if len(first_str) == 0 or len(second_str) == 0:
        return count
    else:
        # increase count if it matches
        if first_str[-1] == second_str[-1]:
            count += 1
    # as long both strings are still populated it will remove the last
    # integer for both and also pass the current count
    return count_match(first_str[:-1], second_str[:-1], count)

