# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    if array[0] == query:
        return True
    else:
        return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 1 or len(text) == 0:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


# digit_match
def digit_match(int_1, int_2):
    str_1 = str(int_1)
    str_2 = str(int_2)

    if str_1[-1] != str_2[-1]: 
        str_1 = str_1[:-1]
        str_2 = str_2[:-1]

        return digit_match(str_1[:-1], str_2[:-1])
  
    else:
        str_1 = str_1
        str_2 = str_2
        return digit_match(str_1[:-1], str_2[:-1])
    
    #I wasn't able to solve this one. There was a solution posted in slack, 
    #which I didn't understand and would like to discuss at my next 1:1 if 
    #possible

