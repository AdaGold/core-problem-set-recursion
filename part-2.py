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
        del array[0]
        return search(array, query)


# is_palindrome

def is_palindrome(text):
    if len(text) == 0 or text[0] != text[-1]:
        return False
    if len(text) <= 2:
        return True
    return is_palindrome(text[1:-1])


# digit_match
# math? surely not

def digit_match(int_one, int_two):
    i_o = str(int_one)
    i_t = str(int_two)
    
    if not i_o or not i_o:
        return 0
    if len(i_o) == 1 and len(i_t) == 1:
        if i_o == i_t:
            return 1
    
    if i_o[-1] != i_t[-1:]:
        return digit_match(i_o[0:-1], i_t[0:-1])
    if i_o[-1] == i_t[-1]:
        return digit_match(i_o[0:-1], i_t[0:-1]) + 1


