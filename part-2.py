# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

#=============================================================================
# search

def search(array, query):
    # base case is when it gets to the end of the array, which is also when the array selection established below gets to a length of 0
    if len(array) == 0:
        return False

    # instead of checking each item in the entire array one at a time, this is checking the FIRST item in an incrementally smaller selection of the array 
    return query == array[0] or search(array[1:], query)

#=============================================================================
# is_palindrome

def is_palindrome(text, i=0, j=-1):

    if i == int(len(text)/2):
        return True

    if text[i] != text[j]:
        return False
    return is_palindrome(text, i+1, j-1)

#=============================================================================
# digit_match

def digit_match(value1, value2):
    str_val1 = str(value1)
    str_val2 = str(value2)
    pairs_count = 0

    if len(str_val1) == 0 or len(str_val2) == 0:
        return pairs_count
    if str_val1[-1] == str_val2[-1]:
        pairs_count += 1

    return pairs_count + digit_match(str_val1[:-1], str_val2[:-1])


