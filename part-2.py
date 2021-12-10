# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not len(array):
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)

# is_palindrome
def is_palindrome(text):
    if len(text) == 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

# digit_match
# I fully had to rely on my classmates for this one
def digit_match(digit1, digit2): 
    first = str(digit1)
    second = str(digit2)
    match_count = 0 
    
    if len(first) == 0 or len(second) == 0: 
        return match_count

    if first[-1] == second[-1]: 
        match_count += 1
    else: 
        match_count += 0
    
    return match_count + digit_match(first[:-1], second[:-1])