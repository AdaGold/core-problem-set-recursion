# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if array == []:
        return False
    elif array[0] == query:
        return True
    else:
        return search(array[1:], query)


# is_palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])


# digit_match
def digit_match(a, b):
    a_str = str(a)
    b_str = str(b)

    if len(a_str) == 0 or len(b_str) == 0:
        return 0
  
    else:
        return (a_str[-1] == b_str[-1]) + (digit_match(a_str[:-1], b_str[:-1]))
     

