# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query, n = 0):
    if not len(array):
        return False
    if n >= len(array):
        return False
    if array[n] == query:
        return True
        
    return search(array, query, n+1)


# is_palindrome
def is_palindrome(text):
    
    
    if(text == text[::- 1]):
        return True
    else:
        return False

    is_palindrome(text)


def digit_match(apples, oranges, n=0, matches=0):
        apple_str = str(apples)[::-1]
        oranges_str = str(oranges)[::-1]

        if n >= len(apple_str) or n >= len(oranges_str):
            return matches

        if apple_str[n] == oranges_str[n]:
            matches += 1

        return digit_match(apples, oranges, n+1, matches)

        # digit_match


