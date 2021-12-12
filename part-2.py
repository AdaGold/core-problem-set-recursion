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
def is_palindrome(word):
    if len(word) == 1:
        return True
    
    if word[0] != word[-1]: return False
    
    return is_palindrome(word[1:-1])


# digit_match
def digit_match(a, b): 
    if a == 0 and b == 0: 
        return 1
    else:
        result = 0
        if (a % 10) == (b % 10):
            result+=1
        if (a//10 == 0) or (b//10 == 0):
            return result
        return result + digit_match(a//10, b//10)

