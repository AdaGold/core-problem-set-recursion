# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    '''
    input: array: unsorted list of ints;  query: int value to find
    output: True if query found in array, else False
    '''
    if len(array) == 0:
        return False
    elif array[-1] == query:
        return True
    else:
        return search(array[:-1], query)



# is_palindrome
def is_palindrome(text):
    '''
    input: string
    output: boolean indicating if palindrome (aka reversible)
    '''
    if text[0] != text[-1]:
        return False
    if len(text) <= 2:
        return True
    # slicing removes first and last letter of the string for next iteration
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(num1, num2):
    '''
    input: two non-negative integers (not necessarily same length)
    output: number of matches (same value at same location relative end)
    '''
    count = 0
    if len(str(num1)) == 0 or len(str(num2)) == 0:
        return count
    elif str(num1)[-1] == str(num2)[-1]:
        count += 1
    return count + digit_match(str(num1)[:-1], str(num2)[:-1])



